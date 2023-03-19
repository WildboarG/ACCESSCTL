/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-18 23:21:38
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-18 23:21:40
 * @Descripttion:
 */
package config

type Response struct {
	Code int    `json:"code"`
	Res  any    `json:"res"`
	Msg  string `json:"msg"`
}

type Res struct {
	Code  int `json:"code"`
	Total int `json:"total"`
	Users any `json:"users"`
}
