import network
from socket import *
import ujson
import display
from machine import Pin 
import time
import _thread

class Acsystem:
        def __init__(self,ssid,password,addr,port):
            self.ssid = ssid
            self.passwd = password 
            self.server = addr 
            self.port = port
            self.wlan = None
            print("run")
            try:
                self._connect()
                display.connect(self.wlan) 
                time.sleep(2)
                display.img("font/test4.dat")
                time.sleep(1)
                display.show("")
            except:
                display.connect("Connect Error")
                time.sleep(1)
                print("Connect Error")
        
        def _mes_arr(self,mes):
            data = {
                "Username":"No1",
                "Mes":mes,
                "Type":"M"
            }
            return ujson.dumps(data)

        def _connect(self):
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            
            if not wlan.isconnected():
                print("connecting to network...")
                wlan.connect(self.ssid,self.passwd)
                while not wlan.isconnected():
                    display.connect("Connecting...")
                    time.sleep_ms(200)
            self.wlan = wlan.ifconfig()[0]
            print(self.wlan)
        
    
        ## handle data
        def hand_data(self,data)->str:
            mes = ujson.loads(data)
            #print("%s[%s] %s"%(mes["Username"],mes["Type"],mes["Mes"]))
            text = mes["Username"]+":"+mes["Mes"]
            #print(type(mes["Mes"]))
            if mes["Type"] == "M":
                display.show(text)
            elif mes["Type"] == "M":
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
                print("logout!")
                self.cli.close()
                return
            
        
        def client_cv(self):
            try:
                 while True:
                    data = self.cli.recv(1024)
                    datas = data.decode('utf-8')
                    self.hand_data(datas)
            except:
                self.cli.close()

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
    display.img("font/text_img1.dat")
    ACS = Acsystem("OpenWrt","q2w3e4r5t6y","192.168.5.187",2023)
    ACS.tcp_client()
    _thread.start_new_thread(ACS.client_cv,())
    _thread.start_new_thread(ACS.client_send())
    while True:
        pass
