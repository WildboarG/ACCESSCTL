from time import sleep_ms
from machine import Pin, SPI

# 导入自定义模块
from mfrc522 import MFRC522


##SPI3 CS=5 CLK=18 MISO=19 MOSI=23 QUADWP=22 QUADHD=21
##SPI2 CS=15 CLK=14 MISO=12 MOSI=13 QUADWP=2 QUADHD=4

# 创建对应的引脚对象
sck = Pin(14, Pin.OUT)  ## SCK/SCL --GPIO18
mosi = Pin(13, Pin.OUT) ## MOSI--GPIO23
miso = Pin(12, Pin.OUT) ## MISO--GPIO19

# 创建SPI对象
spi = SPI(1,baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
sda = Pin(15, Pin.OUT)  ##片选--GPIO5


def readcard():
    # 1. 创建RFID操作对象
    rfid = MFRC522(spi, sda)
    print("rfid准备就绪")
    # 2. 循环读取数据
    data = ""
    flag=0
    # 2. 循环读取数据
    while True:
        # 3. 复位应答
        stat, tag_type = rfid.request(rfid.REQIDL)
        if stat == rfid.OK:
            print("复位应答:"+stat)
            # 4. 防冲突检测，提取id号
            stat, raw_uid = rfid.anticoll()
            if stat == rfid.OK:
                _id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                print("rfid卡片的id:", _id)
                ## 如果rfid 本次读取与上一次值相同不执行函数
                if str(_id) != str(data) and flag==0:
                    print("open1")
                    display.show("welcome "+_id)
                    data = str(_id)
                else:
                    flag+=1
            sleep_ms(500)
            #display.show("")
                    


##if __name__ == "__main__":
##   read_id()


