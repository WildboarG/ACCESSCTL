
from time import sleep_ms, sleep
from machine import Pin, SPI
from mfrc522 import MFRC522

sck = Pin(14, Pin.OUT)
mosi = Pin(13, Pin.OUT)
miso = Pin(12, Pin.OUT)
spi = SPI(1,baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

sda = Pin(15, Pin.OUT)

## 读取卡片内容
def read_all_data():
    
    # 1. 创建RFID操作对象
    rfid = MFRC522(spi, sda)
    
    # 2. 循环
    while True:
        print("-------测试------1")
        
        # 3. 检测卡片
        stat, tag_type = rfid.request(rfid.REQIDL)
        print("-------测试------2")
        if stat == rfid.OK:  # 如果有卡片
            print("-------测试------3")
            stat, raw_uid = rfid.anticoll()  # 读取id
            print("-------测试------4")
            if stat == rfid.OK:
                print("-------测试------5")
                uid = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                print("uid>>>", uid)
                if rfid.select_tag(raw_uid) == rfid.OK:  # 确定要对这个卡片操作
                    print("-------测试------6")
                    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                    keya=[0x99, 0x11,0x04,0x02,0x09,0x04]
                    keyb=[0x02,0x09,0x04,0x99,0x11,0x04]
                    for i in range(64):
                        
                        if i>3:
                            keys=keyb
                        else:
                            keys=key
                        if rfid.auth(rfid.AUTHENT1B, i, keys, raw_uid) == rfid.OK:
                            print("%d-->" % i, rfid.read(i))
                        else:
                            print("%d-->" % i, " error...")
                            
                    rfid.stop_crypto1()
        
        sleep(1)


if __name__ == "__main__":
    read_all_data()

