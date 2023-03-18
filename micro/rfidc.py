'''
Author: WildboarG
version: 1.0
Date: 2023-03-14 18:06:42
LastEditors: WildboarG
LastEditTime: 2023-03-14 18:26:42
Descripttion: 
'''
import urequests
from machine import Pin ,SPI
from mfrc522 import MFRC522
from time import sleep_ms
import display
##读取id
def read_id():
    sck = Pin(14, Pin.OUT)  ## SCK/SCL --GPIO18
    mosi = Pin(13, Pin.OUT) ## MOSI--GPIO23
    miso = Pin(12, Pin.OUT) ## MISO--GPIO19

    # 创建SPI对象
    spi = SPI(1,baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
    sda = Pin(15, Pin.OUT)  ##片选--GPIO5
    rfid = MFRC522(spi, sda)
    return rfid 