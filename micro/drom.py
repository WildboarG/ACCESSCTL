import network
from socket import *
import ujson
import display
import rfidc
import urequests
from machine import Pin ,SPI
from mfrc522 import MFRC522
from time import sleep_ms
import time
import _thread
from __init__ import *



class Acsystem:
        def __init__(self,ssid,password,addr,port):
            self.ssid = ssid
            self.passwd = password 
            self.server = addr 
            self.port = port
            self.admin ="http://192.168.0.105:8080/open"
            self.wlan = None
            try:
                self._connect()
                display.connect(self.wlan) 
                time.sleep(2)
                display.show("") 
            except:
                display.connect("Connect Error")
                print("[系统连接]:"+"\033[1;31m Connect Error!\033[0m")
                
                
        ### 规定消息格式，防止乱码
        ### type消息类型 M为消息 C为控制
        ### esp32clinet 发送消息类型只能为M 
        ### esp32client 接收消息类型可以为M C 
        ### 卡号不匹配 返回M类型消息 传送给tft显示
        ### 卡号匹配 返回C类型消息 传送给舵机控制
        def _mes_arr(self,mes):
            data = {
                "Username":"No1",
                "Mes":mes,
                "Type":"M"  ##M C 
            }
            return ujson.dumps(data)
            
        def _connect(self):
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            
            if not wlan.isconnected():
                print("[系统连接]:"+"\033[1;36m connecting to network...\033[0m")
                wlan.connect(self.ssid,self.passwd)
                while not wlan.isconnected():
                    display.connect("Connecting...")
                    time.sleep_ms(200)
            self.wlan = wlan.ifconfig()[0]
            print("[系统连接]:"+"\033[1;31m {}\033[0m".format(self.wlan))
        
    
        ## handle data
        def hand_data(self,data)->str:
            mes = ujson.loads(data)
            #print("%s[%s] %s"%(mes["Username"],mes["Type"],mes["Mes"]))
            text = mes["Username"]+":"+mes["Mes"]
            #print(type(mes["Mes"]))
            if mes["Type"] == "M":
                display.show(text)
            elif mes["Type"] == "C":
                pass  ## 执行舵机控制

        
        ## create a socket object
        ## short for tcp client
        def client_send(self)->None:
            while True:
                mes = input("send:")
                data = self._mes_arr(mes)
                #print(data)
                try:
                    self.cli.send(data.encode('utf-8'))
                except:
                    print("send error")
                    self.cli.close()
                    display.img("font/test4.dat")
                    return

        def tcp_client(self): 
            self.cli = socket(AF_INET, SOCK_STREAM)
            try:
                if int(self.port) < 65535 and int(self.port) > 80:
                    self.cli.connect((self.server, int(self.port)))
                    print("online")
                else:
                    print("Port number is out of range")
        
            except:
                print("[系统状态]:"+"\033[1;32m logout!\033[0m")
                print("!")
                self.cli.close()
                display.img("font/test4.dat")
                return
            
        
        def client_cv(self):
            try:
                 while True:
                    data = self.cli.recv(1024)
                    datas = data.decode('utf-8')
                    self.hand_data(datas)
            except:
                self.cli.close()
                display.img("font/test4.dat")
                return
            
        def req(self,uid:str):    
            mes = {
                    "user":uid,
                    "num":1
                }
            datas = ujson.dumps(mes)
            res = urequests.post(url=self.admin,data=datas)
            con = res.json()
            print("[User]:"+"\033[1;44;45m {}\033[0m".format(con["name"]))
            return con["name"],con["status"]
        
        def readid(self):
            # 1. 初始化
            rfid = rfidc.read_id()
            print("[检测准备]:"+"\033[1;32m {}\033[0m".format("OK"))
              # 2. 循环读取数据
            data = ""
            flag=0.00
            while True:
                # 3. 复位应答
                stat, tag_type = rfid.request(rfid.REQIDL)
                if str(stat)  == "2" and flag>0:
                    flag= flag-0.99
                    if flag <= 0:
                        display.show("") ##clear
                        print("[门控状态]:"+"\033[1;35m {}\033[0m".format("关闭"))
                        flag= 0
                if stat == rfid.OK:

                    # 4. 防冲突检测，提取id号
                    stat, raw_uid = rfid.anticoll()
                    if stat == rfid.OK:
                        _id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                        print("[认证卡片]:"+"\033[1;37m {}\033[0m".format(_id))
                        ## 如果rfid 本次读取与上一次值相同不执行函数
                        if str(_id) != str(data):  ##
                            #print("open1") ##打开门控
                            card,stus=self.req(str(_id))
                            if stus == 2:
                                display.show("soory! no find")
                                display.audio(7)
                                display.img("font/test4.dat")
                            if stus == 1:
                                print("[门控状态]:"+"\033[1;36m {}\033[0m".format("开启"))
                                display.show("welcome "+card)
                            data = str(_id)
                        else:
                            flag=flag+1
                sleep_ms(500)
                    
                
                   
            
        ## create a socket object
        def tcp_server(self,serverport:str)->None:
            tcps = socket(AF_INET, SOCK_STREAM)
            try:
                if int(serverport) < 65535 and int(serverport) > 80:
                    tcps.bind(("", int(serverport)))
                    
                else:
                    print("Port number is out of range")
                print("waiting for connection...")
                tcps.listen(128) ## set the number of connections
                ns, addr = tcps.accept()
                while True:
                    data = ns.recv(1024)  ## receive data from client
                    datas = data.decode('utf-8')
                    hand_data(datas)
                    if not data:
                        print("no data")
                        ns.close()
                        tft.fill(tft.rgb(255,0,0))
                        tft.text("NO LINK!",30,40,tft.rgb(0,0,0))
                        break
            except:
                tcps.close()



if __name__ == "__main__":
    display.clean()
    #display.img("font/text_img1.dat")
    display.Progressbar()
    #ACS = Acsystem(ssid,password,addr,port)
    ACS = Acsystem("TP-LINK_9683","13283985795",addr,port)
    #ACS.tcp_client()
    # _thread.start_new_thread(ACS.client_cv())
    # _thread.start_new_thread(ACS.client_send())
    ##time.sleep(10)
    _thread.start_new_thread(ACS.readid())
    
