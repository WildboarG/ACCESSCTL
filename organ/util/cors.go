/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-19 17:04:41
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-19 17:04:43
 * @Descripttion:
 */
package util

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

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
