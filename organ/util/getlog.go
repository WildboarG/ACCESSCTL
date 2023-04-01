/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-31 16:29:00
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-04-01 11:19:56
 * @Descripttion:
 */

// 读取data 目录下的json文件
package util

import (
	"bufio"
	"drom/config"
	"fmt"
	"os"
	"regexp"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

func Getlog(c *gin.Context) {
	var datalog config.DataLog
	err := c.ShouldBindQuery(&datalog)
	if err != nil {
		fmt.Println("[查看日志]: " + "\033[31m" + err.Error() + "\033[0m")
	}
	// fmt.Println(datalog.ID)
	today := time.Date(2023, 3, 21, 0, 0, 0, 0, time.Local)
	re_today := today.Format("2006-01-02")
	if datalog.ID == "" {
		datalog.ID = re_today
	}
	//如果输入的格式不符合正则\d\d\d\d-\d\d-\d\d 则返回错误
	if !regexp.MustCompile(`\d\d\d\d-\d\d-\d\d`).MatchString(datalog.ID) {
		c.JSON(200, config.Res{Code: 400, Total: 0, Users: "日期格式错误"})
		return
	}

	logfile := "data/record_" + datalog.ID + ".json"
	// 检查文件是否存在,不存在返回错误
	if _, err := os.Stat(logfile); err != nil {
		if os.IsNotExist(err) {
			c.JSON(200, config.Res{Code: 400, Total: 0, Users: "没有当天的通行记录"})
			return
		}
	}
	fp, err := os.Open(logfile)
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
