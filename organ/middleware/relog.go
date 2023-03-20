/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-20 17:21:28
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-20 20:24:33
 * @Descripttion:
 */
package middleware

import (
	//导入

	cf "drom/config" //导入
	"encoding/json"
	"os"
	"time"

	"github.com/gin-gonic/gin"
)

func Record(c *gin.Context) {
	data, _ := c.Get("data")
	datas := data.(cf.Root)
	card, _ := c.Get("user_card")
	cards := card.(map[string]interface{})
	//fmt.Printf("%s : %s : %s :%d", time.DateTime, datas.User, cards["name"], datas.Num)
	//构建json数据
	Data := map[string]interface{}{
		"date": time.Now().Format("2006-01-02 15:04:05"),
		"user": datas.User,
		"name": cards["name"],
		"num":  datas.Num,
	}
	//格式化json数据
	jsonData, err := json.Marshal(Data)
	if err != nil {
		panic(err)
	}
	//以追加的形式写入到json文件中
	//获取当前文件的路径
	filepath := "./data/record.json"
	//打开文件
	file, err := os.OpenFile(filepath, os.O_RDWR|os.O_CREATE|os.O_APPEND, 0644)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	//追加写入
	file.Write(jsonData)
	file.WriteString("\n")
}
