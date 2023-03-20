/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-19 17:00:13
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-20 17:30:24
 * @Descripttion:
 */

package util

import (
	"drom/config"
	"encoding/json"
	"fmt"

	"github.com/gin-gonic/gin"
)

var DB_host string = "leveldb_test"

// 查询接口
func Search_card(DB_host string, c *gin.Context, card string) {
	dat := Query_card(DB_host, card)
	// json.Marshal(dat)
	c.JSON(200, config.Res{Code: 200, Total: 1, Users: dat})
}

// 查询所有
// 想分组的 在这里修改
func Search_all(DB_host string, c *gin.Context) {
	dat := Query_all(DB_host)
	//将切片转换为json
	// fmt.Println(dat)
	b, err := json.Marshal(dat)
	if err != nil {
		fmt.Println("[查询所有]: " + "\033[31m" + err.Error() + "\033[0m")
	}
	// fmt.Println(string(b))
	var datak []config.Adata
	if err := json.Unmarshal(b, &datak); err != nil {
		// fmt.Println(err.Error())
		fmt.Println("[查询所有]: " + "\033[31m" + "失败" + "\033[0m")
	} else {
		c.JSON(200,
			config.Res{Code: 200,
				Total: len(datak),
				Users: datak,
			}) //返回json数据
	}
}

// 查询选择
func Search_choose(c *gin.Context) {
	var querys config.Query

	//绑定查询参数
	err := c.ShouldBindQuery(&querys)

	if err != nil {
		c.JSON(200, gin.H{"mes": "参数错误"})
		fmt.Println("[查询用户]: " + "\033[31m" + "绑定参数错误" + "\033[0m")
		return
	}

	if querys.Idr == "" { //查询所有
		Search_all(DB_host, c)
		fmt.Println("[查询所有]: " + "\033[32m" + "成功" + "\033[0m")
	} else {
		Search_card(DB_host,
			c,
			string(querys.Idr),
		)
		fmt.Println("[查询用户]: " + "\033[32m" + querys.Idr + "\033[0m")
	}
}

// 添加用户
func Useradd(c *gin.Context) {
	var data config.Adata
	err := c.ShouldBind(&data)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	// fmt.Println(data)
	fmt.Println("[添加用户]: "+"\033[32m", "成功", "\033[0m")
	Add_cards(DB_host,
		data.Id,
		data.Name,
		data.Sex,
		data.Age,
		data.Idr,
		data.Car,
	)
	c.JSON(200, config.Response{Code: 200, Res: "0", Msg: "添加成功"})
}

// 移除用户
func Userremove(c *gin.Context) {
	var data config.Delquery
	err := c.ShouldBindQuery(&data)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	//终端彩色输出
	fmt.Println("[删除用户]: "+"\033[32m", "成功", "\033[0m")
	//fmt.Println(data)
	Remove_cards(DB_host, data.Idr)
	c.JSON(200, config.Response{Code: 200, Res: "0", Msg: "ok"})
}

// 修改用户
func Userupdate(c *gin.Context) {
	var data config.Adata
	err := c.ShouldBindQuery(&data)
	if err != nil {
		fmt.Println("[修改用户]: "+"\033[31m", err.Error(), "\033[0m")
		return
	}
	// fmt.Println(data)
	fmt.Println("[修改用户]: "+"\033[32m", "成功", "\033[0m")
	Update_cards(DB_host,
		data.Id,
		data.Name,
		data.Sex,
		data.Age,
		data.Idr,
		data.Car,
	)
	c.JSON(200, config.Response{Code: 200, Res: "0", Msg: "ok"})
}
