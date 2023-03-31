/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-31 16:29:00
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-31 18:52:12
 * @Descripttion:
 */

// 读取data 目录下的json文件
package util

import (
	"bufio"
	"drom/config"
	"fmt"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func Getlog(c *gin.Context) {

	fp, err := os.Open("data/record_2023-03-21.json")
	if err != nil {
		fmt.Println(err) //打开文件错误
		return
	}
	defer fp.Close()
	buf := bufio.NewScanner(fp)
	var datal []config.Ldata
	var datas []config.Ldata
	for {
		if !buf.Scan() {
			break //文件读完了,退出for
		}
		line := buf.Text() //获取每一行
		misleft := strings.Split(line, "{")
		misright := strings.Split(misleft[1], "}")
		misdou := strings.Split(misright[0], ",")
		date := strings.SplitAfterN(misdou[0], ":", 2)[1]
		name := strings.Split(misdou[1], ":")[1]
		num := strings.Split(misdou[2], ":")[1]
		user := strings.Split(misdou[3], ":")[1]
		datal = append(datal, config.Ldata{Date: date, Name: name, Num: num, User: user})
		datas = append(datal, config.Ldata{Date: date, Name: name, Num: num, User: user})
	}
	c.JSON(200, config.Res{Code: 200, Total: len(datas), Users: datas}) //返回json数据
	fmt.Println("[查看日志]: " + "\033[32m" + "成功" + "\033[0m")
}
