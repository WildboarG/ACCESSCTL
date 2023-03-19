/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-18 23:22:14
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-18 23:22:16
 * @Descripttion:
 */
package config

type Adata struct { //数据库中的数据类型
	Id   int    `json:"id" form:"id"`
	Name string `json:"name" form:"name"`
	Sex  int    `json:"sex" form:"sex"`
	Age  int    `json:"age" form:"age"`
	Idr  string `json:"idr" form:"idr"`
	Car  string `json:"car" form:"car"`
}
