from mfrc522 import MFRC522
from machine import Pin, SPI


def write_date():
    
    # 创建对应引脚
    sck = Pin(14, Pin.OUT)
    mosi = Pin(13, Pin.OUT)
    miso = Pin(12, Pin.OUT)
    spi = SPI(1,baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
    sda = Pin(15, Pin.OUT)
    
    # 创建rfid操作对象
    rfid = MFRC522(spi, sda)

    block_num = [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63]

    ##while True:
    for i in range(7,64,4):
        #print(i)
        # 检测卡片
        stat, tag_type = rfid.request(rfid.REQIDL)
        if stat == rfid.OK:
            
            # 读取id
            stat, raw_uid = rfid.anticoll()
            if stat == rfid.OK:
                print("检测到卡片：")
                print("  - 类型: 0x%02x" % tag_type)
                print("  - id号: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                
                # 选择要操作的本卡片
                if rfid.select_tag(raw_uid) == rfid.OK:
                    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # 注意：没有改密码的话 默认就是这个
                    # 要操作的块序号（0~63）
                    ##block_num = [ i for i in range(7,64,4)]  # 注意这个块是密码，!!! 务必小心操作 !!!
                    ##block_num = [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63]
                    block = i 
                    # 密码认证
                    # 密码\x99\x11\x04\x02x09\x04
                    if rfid.auth(rfid.AUTHENT1B, block, key, raw_uid) == rfid.OK:
                        stat = rfid.write(block, b"\x99\x11\x04\x02\x09\x04\xff\x07\x80\x69\x02\x09\x04\x99\x11\x04")
                        if stat == rfid.OK:
                            print("数据已经写入到卡片...")
                        else:
                            print("error:数据写入失败...")       
                            # 操作完之后，清除对这个卡片的操作标记，直白点：就是告诉这个卡片 不操作了，可以拿走了...
                        rfid.stop_crypto1()
                    else:
                        print("密码错误...")


if __name__ == "__main__":
    write_date()


