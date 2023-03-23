
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


    while True:
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
                    # 密码
                    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # 注意：没有改密码的话 默认就是这个
                    # 要操作的块序号（0~63）
                    block_num = 10
                    # 密码认证
                    if rfid.auth(rfid.AUTHENT1A, block_num, key, raw_uid) == rfid.OK:
                        stat = rfid.write(block_num, b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")
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

