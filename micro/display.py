from machine import Pin,SPI,RTC
import st7735
import time


spi = SPI(2,baudrate=6000000, polarity=0,sck=Pin(18),mosi=Pin(23))

##SPI3 CS=5 CLK=18 MISO=19 MOSI=23 QUADWP=22 QUADHD=21
##SPI2 CS=15 CLK=14 MISO=12 MOSI=13 QUADWP=2 QUADHD=4
## 128x128  稍微修改大一点
## rot  0 1 2 屏幕旋转方向：1横向 0默认 2翻转 
## tft = ST7735(131,131,spi,dc=Pin(4,Pin.OUT),rst=Pin(2,Pin.OUT),cs=Pin(5,Pin.OUT),rot=1,bgr=0) 
tft = st7735.ST7735_Image(131,131,spi,dc=Pin(4,Pin.OUT),rst=Pin(2,Pin.OUT),cs=Pin(5,Pin.OUT),rot=1,bgr=0) 

##片选--GPIO15
##复位--GPIO2
##DC --GPIO4
## SCL/SCK--GPIO18
## MOSI/SDA --GPIO23

## 挂载字符库
tft.font_load("font/GB2312-12.fon")

def audio(num):  ##GPIO27 low sound
    sound = Pin(27,Pin.OUT)
    for i in range(num):
        sound.value(0)
        time.sleep_ms(300)
        sound.value(1)
        time.sleep_ms(200)
    sound.value(1)
    
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
def show(*args):
    if len(args) == 1:
        datas = args[0]
    if len(args) == 2:
        datas = args[0]
        count = args[1]
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
    lend,word = dt_len(datas)
    if len(args) == 1:
        tft.text("{}".format(datas),5,40,tft.rgb(0,0,255))
    if len(args) == 2:
        if word == 0:
            tft.text("{}".format(datas),5,40,tft.rgb(0,0,255))
        else:
            tft.text("{}".format(datas),5,40,tft.rgb(0,0,255))
            tft.text("{}".format(count),5,55,tft.rgb(0,0,255))
        
    tft.text("power by:",4,101,tft.rgb(233,233,233))
    tft.text("WildboarG",50,114,tft.rgb(233,233,233))
    tft.show()

## 连接显示
def connect(datas):
    tft.fill(tft.rgb(0,0,0)) ##清屏：刷新一次与背景相同
    tft.text("系统初始化:",20,5,tft.rgb(0,0,255))
    tft.hline(0,18,130,tft.rgb(0,255,255))
    tft.text("networkconfig:",6,27,tft.rgb(0,0,255))
    tft.text("%s"%(datas),10,47,tft.rgb(0,0,255))
    #tft.text("{}".format(datas),4,65,tft.rgb(0,0,255))
    tft.text("power by:",4,101,tft.rgb(233,233,233))
    tft.text("WildboarG",50,114,tft.rgb(233,233,233))
    tft.show()

## 图片显示
def img(img):
    with open(img, "rb") as f:
        for row in range(128):
            buffer = f.read(256)
            tft.show_img(0, row, 127, row, buffer)

## 开机进度条
def Progressbar():
    tft.show()
    for i in range(0,120,2):
        tft.fill(tft.rgb(0,0,0))
        tft.rect(5,60,120,10,tft.rgb(0,255,255))
        tft.text("系统初始化",18,18,tft.rgb(200,200,200))
        a = i/120*100
        tft.fill_rect(5,60,i,10,tft.rgb(1,1,255))
        tft.text("%d%%"%a,50,50,tft.rgb(240,240,240))
        tft.show()
        time.sleep_ms(20)

