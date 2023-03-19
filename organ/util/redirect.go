/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-19 17:07:05
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-19 17:10:44
 * @Descripttion:
 */
package util

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func Redirect_call(c *gin.Context) {
	c.Redirect(http.StatusMovedPermanently, "http://127.0.0.1:9528/#/login")
}
