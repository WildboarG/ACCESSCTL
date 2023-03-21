/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-09 17:41:59
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-20 19:49:42
 * @Descripttion:
 */
package main

import (
	"drom/middleware"
	"drom/util"
	"log"
	"net/http"

	"github.com/gin-gonic/gin" //导入
)

func main() {

	router := gin.Default()
	//router := gin.New()
	// router.Use(gin.LoggerWithFormatter(func(param gin.LogFormatterParams) string {
	//     return fmt.Sprintf("%s - [%s] \"%s %s %s %d %s \"%s\" %s\"\n",
	//         param.ClientIP,
	//         param.TimeStamp.Format(time.RFC1123),
	//         param.Method,
	//         param.Path,
	//         param.Request.Proto,
	//         param.StatusCode,
	//         param.Latency,
	//         param.Request.UserAgent(),
	//         param.ErrorMessage,
	//     )
	// }))
	//router.Use(gin.Recovery())
	gin.DebugPrintRouteFunc = func(httpMethod, absolutePath, handlerName string, nuHandlers int) {
		log.Printf("endpoint %v %v %v %v\n", httpMethod, absolutePath, handlerName, nuHandlers)
	}
	// 写入文件
	//file,_ :=os.Create("gin.log")
	//gin.DefaultWriter = io.MultiWriter(file,os.Stdout)
	router.Use(util.Cors()) //跨域
	router.LoadHTMLGlob("templates/html/*")
	router.StaticFS("/static", http.Dir("./static"))
	router.POST("/", util.Login_in) //登陆接口
	router.GET("/", util.Redirect_call)
	user := router.Group("/user")
	{
		user.GET("/add", util.Useradd)
		user.GET("/edit", util.Userupdate)
		user.GET("/remove", util.Userremove)
		user.GET("/listpage", util.Search_choose)
	}

	router.POST("/open", util.Open,middleware.Record) //开门接口

	router.Run(":8080")
}
