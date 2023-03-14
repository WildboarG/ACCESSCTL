from time import sleep_ms
from ustruct import pack
from machine import SPI,Pin
from micropython import const
import framebuf
 
#   ST7735V寄存器定义
#   一些常量
NOP     = const(0x00) # No Operation  无操作
SWRESET = const(0x01) # Software reset 软件复位

SLPIN   = const(0x10) # Sleep in & booster off 睡眠模式
SLPOUT  = const(0x11) # Sleep out & booster on 退出睡眠模式
PTLON   = const(0x12) # Partial mode on 部分模式
NORON   = const(0x13) # Partial off (Normal) 普通模式

INVOFF  = const(0x20) # Display inversion off 关闭显示反转
INVON   = const(0x21) # Display inversion on 打开显示反转
DISPOFF = const(0x28) # Display off 关闭显示
DISPON  = const(0x29) # Display on 打开显示 
CASET   = const(0x2A) # Column address set 列地址设置
RASET   = const(0x2B) # Row address set 行地址设置 
RAMWR   = const(0x2C) # Memory write 内存写入
RGBSET  = const(0x2D) # Display LUT set 显示LUT设置

PTLAR   = const(0x30) # Partial start/end address set 部分开始/结束地址设置
COLMOD  = const(0x3A) # Interface pixel format 设置接口像素格式
TEOFF   = const(0x34) # Tearing effect line off 关闭撕裂效果线
TEON    = const(0x35) # Tearing effect mode set 撕裂效果模式设置
MADCTL  = const(0x36) # Memory data access control 内存数据访问控制
VSCSAD  = const(0x37) # Vertical scroll start address of RAM 垂直滚动RAM的起始地址
IDMOFF  = const(0x38) # Idle mode off 关闭空闲模式
IDMON   = const(0x39) # Idle mode on 打开空闲模式

# panel function commands 面板功能命令
FRMCTR1 = const(0xB1) # In normal mode (Full colors) 正常模式（全彩色）
FRMCTR2 = const(0xB2) # In Idle mode (8-colors) 空闲模式（8色）
FRMCTR3 = const(0xB3) # In partial mode + Full colors 部分模式+全彩色
INVCTR  = const(0xB4) # Display inversion control 显示反转控制

PWCTR1  = const(0xC0) # Power control settings 电源控制设置 GVDD 电压
PWCTR2  = const(0xC1) # Power control settings 电源控制设置 VGH 电压
PWCTR3  = const(0xC2) # In normal mode (Full colors) 正常模式（全彩色）
PWCTR4  = const(0xC3) # In Idle mode (8-colors) 空闲模式（8色）
PWCTR5  = const(0xC4) # In partial mode + Full colors 部分模式+全彩色
VMCTR1  = const(0xC5) # VCOM control 1 VCOM控制1


GMCTRP1 = const(0xE0)  # Gamma correction settings 伽马校正设置
GMCTRN1 = const(0xE1) # Gamma correction settings 伽马校正设置



class ST7735(framebuf.FrameBuffer): # 定义类ST7735，继承自framebuf.FrameBuffer
    def __init__(self, width, height, spi, dc, rst, cs, rot=0, bgr=0): # 初始化函数
        if dc is None: 
            raise RuntimeError('TFT must be initialized with a dc pin number')
        dc.init(dc.OUT, value=0)
        if cs is None:
            raise RuntimeError('TFT must be initialized with a cs pin number')
        cs.init(cs.OUT, value=1)
        if rst is not None:
            rst.init(rst.OUT, value=1)
        else:
            self.rst =None
        self.spi = spi
        self.rot = rot
        self.dc = dc
        self.rst = rst
        self.cs = cs
        self.height = height
        self.width = width
        ## FrameBuffer needs 2 byte for every RGB565 pixel
        self.buffer = bytearray(self.height * self.width*2)
        ## FrameBuffer(buffer,width,height,format,stride=width)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565,self.width) # 调用父类的初始化函数
        ## 继承了父类的方法和属性fill pixel hline vline line rect ellpise poly text  
        if (self.rot ==0): # 根据旋转角度设置MADCTL
            madctl=0x00
        elif (self.rot ==1):
            madctl=0xa0
        elif (self.rot ==2):
            madctl=0xc0
        else :
            madctl=0x60  ## 默认方向

        if bgr==0: # 根据BGR设置MADCTL
            madctl|=0x08
        self.madctl = pack('>B', madctl) # 将MADCTL转换为字节流
        self.reset() 

        self._write(SLPOUT) # 退出睡眠模式
        sleep_ms(120) 
        for command, data in ( 
            (COLMOD,  b"\x05"), ## 3-12bit/pixel , 5-16bit/pixel, 6-18bit/pixel
            (MADCTL,  pack('>B', madctl)),  ## '>B' 大端，无符号char
            ): # 设置显示模式
            self._write(command, data)  ## 写入屏显示方向
        if self.width==80 or self.height==80: 
            self._write(INVON, None) 
        else:
            self._write(INVOFF, None)  
        buf=bytearray(128) 
        for i in range(32): 
            buf[i]=i*2
            buf[i+96]=i*2
        for i in range(64):
            buf[i+32]=i
        self._write(RGBSET, buf) 
        #self._write(NORON)
        #sleep_ms(10)
        self.show()
        self._write(DISPON) # 开启显示
        #sleep_ms(100)
    def reset(self):  
        if self.rst is None:
            self._write(SWRESET)
            sleep_ms(50)
            return
        self.rst.off()
        sleep_ms(50)
        self.rst.on()
        sleep_ms(50)
    def _write(self, command, data = None): # 向TFT写入数据
        self.cs.off() # 使能片选
        self.dc.off() # 选择命令
        self.spi.write(bytearray([command])) # 写入命令
        self.cs.on() # 禁止片选
        if data is not None: # 如果有数据
            self.cs.off() # 使能片选
            self.dc.on() # 选择数据
            self.spi.write(data) # 写入数据
            self.cs.on() # 禁止片选 
    def show(self): # 显示函数
        if self.width==80 or self.height==80:  # 80*80的屏幕
            if self.rot==0 or self.rot==2:  # 根据旋转角度设置窗口
                self._write(CASET,pack(">HH", 26, self.width+26-1)) 
                self._write(RASET,pack(">HH", 1, self.height+1-1))
            else:
                self._write(CASET,pack(">HH", 1, self.width+1-1))
                self._write(RASET,pack(">HH", 26, self.height+26-1))
        else: # 其他屏幕
            if self.rot==0 or self.rot==2:  # 根据旋转角度设置窗口
                ## pack函数打包（fmt,value）
                self._write(CASET,pack(">HH", 0, self.width-1)) # 设置列地址
                self._write(RASET,pack(">HH", 0, self.height-1)) # 设置行地址
            else:
                self._write(CASET,pack(">HH", 0, self.width-1)) # 设置列地址
                self._write(RASET,pack(">HH", 0, self.height-1)) # 设置行地址
            
        self._write(RAMWR,self.buffer) # 写入数据
    def rgb(self,r,g,b): # 将RGB转换为565格式
        return ((r&0xf8)<<8)|((g&0xfc)<<3)|((b&0xf8)>>3) 



class ST7735_Image(ST7735): # 图片显示类
    
    def _set_columns(self,start,end): # 设置列地址
        if start <= end:
            self._write(CASET,pack(">HH",start,end))
    
    def _set_rows(self,start,end): # 设置行地址
        if start <= end:
            self._write(RASET,pack(">HH",start,end))
    
    def _set_window(self,x0,y0,x1,y1): # 设置窗口
        self._set_columns(x0,x1)
        self._set_rows(y0,y1)
        #self._write(RAMWR,self.buffer)
    
    def show_img(self,x0,y0,x1,y1,img_data): # 显示图片
        self._set_window(x0,y0,x1,y1)
        self._write(RAMWR,img_data)     
