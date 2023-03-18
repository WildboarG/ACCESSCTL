/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-09 17:41:59
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-18 18:05:51
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

type Response struct {
	Code int    `json:"code"`
	Res  any    `json:"res"`
	Msg  string `json:"msg"`
}

type Res struct {
	Code  int `json:"code"`
	Total int `json:"total"`
	Users any `json:"users"`
}

type Adata struct { //数据库中的数据类型
	Id   int    `json:"id" form:"id"`
	Name string `json:"name" form:"name"`
	Sex  int    `json:"sex" form:"sex"`
	Age  int    `json:"age" form:"age"`
	Idr  string `json:"idr" form:"idr"`
	Car  string `json:"car" form:"car"`
}

type Query struct {
	Page int    `json:"page" form:"page"`
	Idr  string `json:"idr" form:"idr"`
}

type Delquery struct {
	Idr string `json:"idr" form:"idr"`
}

var db_host string = "leveldb_test"

// func Open(c *gin.Context) {
// 	var datas Root
// 	body, err := c.GetRawData()
// 	// fmt.Println(body)
// 	if err != nil {
// 		fmt.Println(err)
// 	}
// 	err = json.Unmarshal(body, &datas)
// 	if err != nil {
// 		fmt.Println(err.Error())
// 	}
// 	fmt.Println(datas)
// 	var cards interface{}
// 	// 获取卡号 读卡器型号 做一个中间件然后记录进入时间，入口读卡器卡号
// 	// 从数据库中比对数据 返回车牌号，若不存在返回"No"
// 	cards = Search_card(c, datas.User)
// 	var dat map[string]interface{}
// 	err = json.Unmarshal(string(cards), &dat)
// 	if err != nil {
// 		fmt.Println(err.Error())
// 	}
// 	var stus int
// 	if dat["err"] != nil {
// 		stus = 1 // 通行
// 	} else {
// 		stus = 2 // 不通行
// 	}
// 	c.JSON(200, gin.H{"name": cards, "status": stus})
// }

func Login(c *gin.Context) {
	if c.Request.Method == "GET" {
		c.HTML(200, "login.html", nil)
		// c.JSON(200, gin.H{"message": "登陆成功"})
	}
}

// 登陆接口
func Login_in(c *gin.Context) {
	var userinfo UserInfo

	err := c.ShouldBind(&userinfo)
	// fmt.Println(userinfo.User)
	// fmt.Println(userinfo.Password)
	if err != nil {
		fmt.Println("[用户登陆]: " + "\033[31m" + err.Error() + "\033[0m")
		return
	}
	if userinfo.User == "WildboarG" && userinfo.Password == "959586" {
		fmt.Println("[用户登陆]: " + "\033[32m" + "登陆成功" + "\033[0m")
		c.JSON(200, Response{200, "0", "登陆成功"})
	} else {
		fmt.Println("[用户登陆]: " + "\033[31m" + "账号或密码错误" + "\033[0m")
		c.JSON(201, Response{201, "-1", "账号或密码错误"})
	}
}

// 查询接口
func Search_card(db_host string, c *gin.Context, card string) {
	dat := util.Query_card(db_host, card)
	// json.Marshal(dat)
	c.JSON(200, Res{200, 1, dat})
}

// 查询所有
// 想分组的 在这里修改
func Search_all(db_host string, c *gin.Context) {
	dat := util.Query_all(db_host)
	//将切片转换为json
	// fmt.Println(dat)
	b, err := json.Marshal(dat)
	if err != nil {
		fmt.Println("[查询所有]: " + "\033[31m" + err.Error() + "\033[0m")
	}
	// fmt.Println(string(b))
	var datak []Adata
	if err := json.Unmarshal(b, &datak); err != nil {
		// fmt.Println(err.Error())
		fmt.Println("[查询所有]: " + "\033[31m" + "失败" + "\033[0m")
	} else {
		c.JSON(200,
			Res{200, len(datak),
				datak,
			}) //返回json数据
	}
}

// 查询选择
func Search_choose(c *gin.Context) {
	var querys Query

	//绑定查询参数
	err := c.ShouldBindQuery(&querys)

	if err != nil {
		c.JSON(200, gin.H{"mes": "参数错误"})
		fmt.Println("[查询用户]: " + "\033[31m" + "绑定参数错误" + "\033[0m")
		return
	}

	if querys.Idr == "" { //查询所有
		Search_all(db_host, c)
		fmt.Println("[查询所有]: " + "\033[32m" + "成功" + "\033[0m")
	} else {
		Search_card(db_host,
			c,
			string(querys.Idr),
		)
		fmt.Println("[查询用户]: " + "\033[32m" + querys.Idr + "\033[0m")
	}
}

// 添加用户
func Useradd(c *gin.Context) {
	var data Adata
	err := c.ShouldBind(&data)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	// fmt.Println(data)
	fmt.Println("[添加用户]: "+"\033[32m", "成功", "\033[0m")
	util.Add_cards(db_host,
		data.Id,
		data.Name,
		data.Sex,
		data.Age,
		data.Idr,
		data.Car,
	)
	c.JSON(200, Response{200, "0", "添加成功"})
}

// 移除用户
func Userremove(c *gin.Context) {
	var data Delquery
	err := c.ShouldBindQuery(&data)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	//终端彩色输出
	fmt.Println("[删除用户]: "+"\033[32m", "成功", "\033[0m")
	//fmt.Println(data)
	util.Remove_cards(db_host, data.Idr)
	c.JSON(200, Response{200, "0", "ok"})
}

// 修改用户
func Userupdate(c *gin.Context) {
	var data Adata
	err := c.ShouldBindQuery(&data)
	if err != nil {
		fmt.Println("[修改用户]: "+"\033[31m", err.Error(), "\033[0m")
		return
	}
	// fmt.Println(data)
	fmt.Println("[修改用户]: "+"\033[32m", "成功", "\033[0m")
	util.Update_cards(db_host,
		data.Id,
		data.Name,
		data.Sex,
		data.Age,
		data.Idr,
		data.Car,
	)
	c.JSON(200, Response{200, "0", "ok"})
}

func main() {

	// router := gin.Default()
	router := gin.New()
	router.Use(gin.Recovery())
	router.Use(Cors())
	router.LoadHTMLGlob("templates/html/*")
	router.StaticFS("/static", http.Dir("./static"))
	//路由分组
	// v1 := router.Group("/v1")
	// {
	// 	v1.POST("/login", Login_in)
	// 	v1.POST("/open", Open)
	// }
	user := router.Group("/user")
	{
		user.GET("/add", Useradd)
		user.GET("/edit", Userupdate)
		user.GET("/remove", Userremove)
		user.GET("/listpage", Search_choose)
	}
	router.POST("/", Login_in) //登陆接口

	// router.POST("/open", Open)

	router.Run(":8080")
}

func Cors() gin.HandlerFunc { //解决跨域问题
	return func(c *gin.Context) {
		method := c.Request.Method
		c.Header("Access-Control-Allow-Origin", "*")                                                     // 可将将 * 替换为指定的域名
		c.Header("Access-Control-Allow-Headers", "Content-Type,AccessToken,X-CSRF-Token, Authorization") //你想放行的header也可以在后面自行添加
		c.Header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE, UPDATE")              //我自己只使用 get post 所以只放行它
		c.Header("Access-Control-Expose-Headers", "Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Content-Type")
		c.Header("Access-Control-Allow-Credentials", "true")

		// 放行所有OPTIONS方法
		if method == "OPTIONS" {
			c.AbortWithStatus(http.StatusNoContent)
		}

		// 处理请求
		c.Next()
	}
}
