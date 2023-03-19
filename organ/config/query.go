/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-18 23:23:30
 * @LastEditorps: WildboarG
 * @LastEditTime: 2023-03-18 23:39:57
 * @Descripttion:
 */
package config

type Query struct {
	Page int    `json:"page" form:"page"`
	Idr  string `json:"idr" form:"idr"`
}

type Delquery struct {
	Idr string `json:"idr" form:"idr"`
}
