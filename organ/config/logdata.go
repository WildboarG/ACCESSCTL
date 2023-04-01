/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-31 17:02:24
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-04-01 11:19:43
 * @Descripttion:
 */
package config

type Ldata struct { //数据库中的数据类型
	Date string `json:"id" form:"date"`
	Name string `json:"name" form:"name"`
	Num  string `json:"sex" form:"num"`
	User string `json:"idr" form:"user"`
}

type DataLog struct {
	ID   string `json:"id" form:"id"`
	Page int    `json:"page" form:"page"`
}
