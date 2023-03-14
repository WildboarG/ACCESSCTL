/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-09 17:41:59
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-11 20:51:49
 * @Descripttion:
 */
package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"

	// leveldbutil "github.com/syndtr/goleveldb/leveldb/util"
	"drom/util"
)

type Root struct {
	User string `json:"user"`
	Num  int    `json:"num"`
}

type Drom struct {
	Name   string `json:"name"`
	Status int    `json:"status"`
}
type UserInfo struct {
	User     string `json:"user" form:"user"`
	Password string `json:"password" form:"password"`
}

func Open(c *gin.Context) {
	var datas Root
	body, err := c.GetRawData()
	// fmt.Println(body)
	if err != nil {
		fmt.Println(err)
	}
	err = json.Unmarshal(body, &datas)
	if err != nil {
		fmt.Println(err.Error())
	}
	fmt.Println(datas)

	var cards string
	// 获取卡号 读卡器型号 做一个中间件然后记录进入时间，入口读卡器卡号
	// 从数据库中比对数据 返回车牌号，若不存在返回"No"
	cards = Search_card(datas.User)
	print(cards)
	var stus int
	if cards != "Null" {
		stus = 1 // 通行
	} else {
		stus = 2 // 不通行
	}
	c.JSON(200, gin.H{"name": cards, "status": stus})
}

func Login(c *gin.Context) {
	if c.Request.Method == "GET" {
		c.HTML(200, "login.html", nil)
	}
}

func Login_in(c *gin.Context) {
	// fmt.Println(c.PostForm("user"))
	// fmt.Println(c.PostForm("password"))
	var userinfo UserInfo
	err := c.ShouldBind(&userinfo)
	fmt.Println(userinfo.User)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	if userinfo.User == "WildboarG" && userinfo.Password == "959586" {
		c.HTML(200, "index.html", nil)
	} else {
		//c.HTML(200, "login.html", gin.H{"meg": "用户名或密码错误！"})
		c.String(200, "么么密码")
	}
}

func Search_card(card string) (name string) {
	return util.Query_card("leveldb", card)
}

// 遍历数据库
func Search_all() {
	util.Showdb("leveldb")
}

func Update(c *gin.Context) {
	msg := map[string]string{"time": "18:18", "cardNumber": "001", "name": "zhangsan"}
	c.HTML(200, "index.html", msg)
}
func main() {
	//Search_all()
	router := gin.Default()
	router.LoadHTMLGlob("templates/html/*")
	router.StaticFS("/static", http.Dir("./static"))
	router.GET("/", Login)
	router.POST("/", Login_in)
	router.POST("/index", Update)
	router.POST("/open", Open)

	router.Run(":8080")
}
