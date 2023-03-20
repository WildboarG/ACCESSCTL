# 自动车库门禁系统

[TOC]



---

## 检测端设计

###  核心模块

该系统采用 micropython 作为核心控制单元,负责数据的处理,传送到后台,后台验证之后返回门控命令,esp32对门控命令进行解析,对显示模块,警报模块,门控设置 统一处理

```python
def req(self,uid:str):    ## 跟后台发送请求 验证身份 
            mes = {
                    "user":uid,
                    "num":1
                }
            datas = ujson.dumps(mes)
            res = urequests.post(url=self.admin,data=datas)
            con = res.json()
            print("[User]:"+"\033[1;44;45m {}\033[0m".format(con["name"]))
            return con["name"],con["status"]  
```



### 采集模块

本系统使用了一块RFID-RC522 对 ID 进行读取,当检测到有id卡靠近时, 读取到卡号,封装为JSON数据,通过HTTP协议,发送到后端,后端通过对比数据库验证之后返回相应的响应.

```python
def read_id():   ## 采集卡片信息
    sck = Pin(14, Pin.OUT)  ## SCK/SCL --GPIO18
    mosi = Pin(13, Pin.OUT) ## MOSI--GPIO23
    miso = Pin(12, Pin.OUT) ## MISO--GPIO19

    # 创建SPI对象
    spi = SPI(1,baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
    sda = Pin(15, Pin.OUT)  ##片选--GPIO5
    rfid = MFRC522(spi, sda)
    return rfid 
```





### 显示模块

采用一块TFT.44寸SPI屏幕进行显示,对门控通行`USER`进行显示,对未授权的用户显示NO FOUND 

```python
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
```



### 报警模块

采用一个MH-FMD无源蜂鸣器对未授权的用户进行报警提示

```python
def audio(num):  ##GPIO27 low sound
    sound = Pin(27,Pin.OUT)
    for i in range(num):
        sound.value =  0
        time.sleep_ms(300)
        sound.value = 1
        time.sleep(200)
    sound.value(1)
    
```





### 下位机

---

采用一颗ESP32(国产乐鑫公司)集成wifi功能的微控制器

- 处理器：Tensilica LX6 双核处理器（一核处理高速连接；一核独立应用开发）
- 主频：32 位双核处理器，CPU 正常工作速度为 80 MHz，最高可达 240 MHz
- SRAM：520KB，最大支持 8 MB 片外 SPI SRAM
- Flash：最大支持 16 MB 片外 SPI Flash
- WiFi 协议：支持 802.11 b/g/n/d/e/i/k/r 等协议，速度高达150 Mbps
- 频率范围：2.4~2.5 GHz
- 蓝牙协议：支持蓝牙 v4.2 完整标准，包含传统蓝牙 (BR/EDR) 和低功耗蓝牙 (BLE)
- 同时他还具备丰富的外设接口：比如 GPIO、ADC、DAC、SPI、I²C、I²S、UART 等常用接口一个不少

 用micropython 实现

- 丰富的第三方库平台
- 开发简单容易上手



#### 使用

---

1. 烧录好对应版本的固件(v1.7.1)

2. 将核心文件以及配置文件上传到micorpython中

3. 上电自动启动,连接对应配置的wifi,连接成功后,屏幕进入主页面,即可进入工作模式

4. 可以用pyboard工具或者thonny来对运行后的控制台进行监听

   ```shell
   pyboard --device /dev/ttyACM0 main.py
   
   ```

​	![](/home/WildboarG/Arduino/micropython/accessctl/检测端监听pyboard.png)

#### 注意

---

检测端启动前或者前端管理系统启动前都要先启动后端服务程序



### 材料清单

- ESP32
- RMFRC522(RFID检测模块,ID卡片)
- 蜂鸣器
- 杜邦线
- 步进舵机
- TTF串口屏
- ![](/home/WildboarG/Arduino/micropython/accessctl/实物设计.jpg)
