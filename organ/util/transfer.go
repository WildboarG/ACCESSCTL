/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-19 17:33:44
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-31 18:50:18
 * @Descripttion:
 */

package util

import (
	cf "drom/config" //导入
	"encoding/json"
	"fmt"

	"github.com/gin-gonic/gin"
)

func Open(c *gin.Context) {
	var datas cf.Root
	var cards []interface{}
	var stus int
	var cars string

	body, err := c.GetRawData()
	// fmt.Println(body)
	if err != nil {
		fmt.Println(err)
	}
	err = json.Unmarshal(body, &datas)
	if err != nil {
		fmt.Println(err.Error())
	}
	// fmt.Println(datas)

	// 获取卡号 读卡器型号 做一个中间件然后记录进入时间，入口读卡器卡号
	// 从数据库中比对数据 返回车牌号，若不存在返回"ERR"
	cards = Query_card(DB_host, datas.User)   //参数分别是数据库和idr
	card := cards[0].(map[string]interface{}) //card是

	c.Set("data", datas)
	c.Set("user_card", card)

	if card["idr"] != nil {
		stus = 1
		cars = card["car"].(string)
	} else {
		stus = 2 // 不通行
		cars = "no exit"
	}

	c.JSON(200, gin.H{"name": cars, "status": stus})
	c.Next()
}
