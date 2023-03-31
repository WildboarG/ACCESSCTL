/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-31 17:02:24
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-31 17:05:51
 * @Descripttion:
 */
package config

type Ldata struct { //数据库中的数据类型
	Date string `json:"id" form:"date"`
	Name string `json:"name" form:"name"`
	Num  string `json:"sex" form:"num"`
	User string `json:"idr" form:"user"`
}
