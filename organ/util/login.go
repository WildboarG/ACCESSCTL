/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-19 16:58:00
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-19 17:30:43
 * @Descripttion:
 */
package util

import (
	cf "drom/config" //导入
	"fmt"
	"log"

	"github.com/gin-gonic/gin"
)

func Login(c *gin.Context) {
	if c.Request.Method == "GET" {
		c.HTML(200, "login.html", nil)
		// c.JSON(200, gin.H{"message": "登陆成功"})
	}
}

// 登陆接口
func Login_in(c *gin.Context) {
	var userinfo cf.UserInfo

	err := c.ShouldBind(&userinfo)
	// fmt.Println(userinfo.User)
	// fmt.Println(userinfo.Password)
	if err != nil {
		log.Println("[用户登陆]: " + "\033[31m" + err.Error() + "\033[0m")
		return
	}
	if userinfo.User == "WildboarG" && userinfo.Password == "959586" {
		fmt.Println("[用户登陆]: " + "\033[32m" + "登陆成功" + "\033[0m")
		c.JSON(200, cf.Response{Code: 200, Res: "0", Msg: "登陆成功"})
	} else {
		fmt.Println("[用户登陆]: " + "\033[31m" + "账号或密码错误" + "\033[0m")
		c.JSON(201, cf.Response{Code: 201, Res: "-1", Msg: "账号或密码错误"})
	}
}
