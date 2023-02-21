from machine import Pin,SPI,RTC
import st7735
import time


spi = SPI(2,baudrate=6000000, polarity=0,sck=Pin(18),mosi=Pin(23))

## 128x128  稍微修改大一点
## rot  0 1 2 屏幕旋转方向：1横向 0默认 2翻转 
## tft = ST7735(131,131,spi,dc=Pin(4,Pin.OUT),rst=Pin(2,Pin.OUT),cs=Pin(5,Pin.OUT),rot=1,bgr=0) 
tft = st7735.ST7735_Image(131,131,spi,dc=Pin(4,Pin.OUT),rst=Pin(2,Pin.OUT),cs=Pin(5,Pin.OUT),rot=1,bgr=0) 

## 挂载字符库
tft.font_load("font/GB2312-12.fon")

## 颜色顺序 b r g
def dt_len(text)->int:
    count=0
    flag=0
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            count = count +2
            flag = flag+1
        else:
            count =count + 1
            
    return count,flag

## 清除屏幕
def clean():
    tft.fill(tft.rgb(0,0,0,))
    tft.show()

## 主屏幕显示
def show(show_data):
    rtc = RTC()
    wek = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    if rtc.datetime()[0] != 2023:
        rtc.datetime((2023,02,19,6,15,54,0,0))
    data = rtc.datetime()
    year = data[0]
    mon = data[1]
    day = data[2]
    week = data[3]
    #print("%.2d"%m)
    #time.sleep(1)
    tft.fill(tft.rgb(0,0,0)) ##清屏：刷新一次与背景相同
    tft.text("车库门禁系统",32,5,tft.rgb(0,0,255))
    tft.hline(0,18,130,tft.rgb(0,255,255))
    tft.hline(0,21,130,tft.rgb(0,255,255))
    tft.text("%.2d-%.2d-%.2d:"%(year,mon,day),10,27,tft.rgb(0,0,255))
    tft.text("%s"%(wek[week]),85,27,tft.rgb(233,233,0))    
    tft.hline(0,38,130,tft.rgb(255,255,255))
    tft.vline(3,38,60,tft.rgb(255,255,255))
    tft.vline(129,38,60,tft.rgb(255,255,255))
    tft.hline(0,98,130,tft.rgb(255,255,255)) 
    ## 38-98之间的框内作为输入显示区域  以5 40作为起点 120个像素
    lend,word = dt_len(show_data)
    if lend<=20:
        tft.text("{}".format(show_data),5,40,tft.rgb(0,0,255))
    if 20<lend<=40: 
        tft.text("{}".format(show_data[:20-word]),5,40,tft.rgb(0,0,255))
        tft.text("{}".format(show_data[21-word:]),5,53,tft.rgb(0,0,255))
    #tft.text("{}".format(show_data),4,65,tft.rgb(0,0,255))
    if 40<lend<=60:
        tft.text("{}".format(show_data[:20]),5,40,tft.rgb(0,0,255))
        tft.text("{}".format(show_data[20:40]),5,54,tft.rgb(0,0,255))
        tft.text("{}".format(show_data[40:]),5,68,tft.rgb(0,0,255))
    if lend>60:
        tft.text("{}".format(show_data[:20]),5,40,tft.rgb(0,0,255))
        tft.text("{}".format(show_data[20:40]),5,55,tft.rgb(0,0,255))
        tft.text("{}".format(show_data[40:60]),5,70,tft.rgb(0,0,255))
        tft.text("{}".format(show_data[61:]),5,85,tft.rgb(0,0,255))
        
    tft.text("power by:",4,101,tft.rgb(233,233,233))
    tft.text("WildboarG",50,114,tft.rgb(233,233,233))
    tft.show()

## 连接显示
def connect(show_data):
    tft.fill(tft.rgb(0,0,0)) ##清屏：刷新一次与背景相同
    tft.text("系统初始化:",20,5,tft.rgb(0,0,255))
    tft.hline(0,18,130,tft.rgb(0,255,255))
    tft.text("networkconfig:",6,27,tft.rgb(0,0,255))
    tft.text("%s"%(show_data),10,47,tft.rgb(0,0,255))
    #tft.text("{}".format(show_data),4,65,tft.rgb(0,0,255))
    tft.text("power by:",4,101,tft.rgb(233,233,233))
    tft.text("WildboarG",50,114,tft.rgb(233,233,233))
    tft.show()

## 图片显示
def img(img):
    with open(img, "rb") as f:
        for row in range(128):
            buffer = f.read(256)
            tft.show_img(0, row, 127, row, buffer)
   

