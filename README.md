# 项目说明

---

#### 项目目录:bookmark_tabs:

```
accessctl
    1. micro
    2. nx-admin
    3. organ
    	-cmd     命令文件
        -config  配置文件和定义
        -data    数据
        -doc     说明文档
        -example 例子
        -leveldb 数据库
        -pkg
        -static  静态文件
        -templates 模板文件
        -text    测试函数
        -verdor  临时文件
        -util    工具函数
```

### micropython:snake:

​		[MicroPython](https://micropython.org/)是Python的一个精简版本，它是为了运行在单片机这样的性能有限的微控制器上，最小体积仅256K，运行时仅需16K内存。

> MicroPython是基于Python 3.4的语法标准。因为要适应嵌入式微控制器，所以裁剪了大部分标准库，仅保留部分模块如`math`、`sys`的部分函数和类。此外，很多标准模块如`json`、`re`等在MicroPython中变成了以`u`开头的`ujson`、`ure`，表示针对MicroPython开发的标准库。
>
> 目前，MicroPython除了可以运行在最初开发的[pyboard](https://store.micropython.org/pyb-features)微控制器上外，还可以运行在大量基于ARM的嵌入式系统，如[Arduino](https://www.arduino.cc/)，这样我们就可以通过Python来非常方便地开发自动控制、机器人这样的应用。

### nx-admin:necktie:

​		Vue（发音为，like view）是一个用于构建用户界面**的渐进式框架**。它从头开始设计为可增量采用，并且可以根据不同的用例在库和框架之间轻松扩展。它由一个仅关注视图层的平易近人的核心库和一个由支持库组成的生态系统组成，可帮助您解决大型单页应用程序中的复杂性。

> 前端采用[nx-admin](https://mgbq.github.io/vue-permission/#/login) 是一个开源的管理系统前端集成方案，它基于 [vue](https://github.com/vuejs/vue) 和 [element](https://github.com/ElemeFE/element)。它使用了最新的前端技术栈，内置了i18国际化解决方案，动态路由，权限验证，提炼了典型的业务模型，提供了丰富的功能组件，它可以帮助你快速搭建企业级中后台产品原型。最大程度上帮助个人，企业节省时间成本和费用开

### organ:mouse:

​     Go 是一种开源编程语言，可以轻松构建简单、可靠和高效的软件。

> 后端采用golang 开发,golang属于第二梯队的编译型语言,同时又支持解释运行,,方便调试,继承了c的大部分语言,且关键字少,代码易于阅读.可以跨平台交叉编译,方便快速部署. 使用了gin 高性能的web框架, 多线程使用起来简单.
