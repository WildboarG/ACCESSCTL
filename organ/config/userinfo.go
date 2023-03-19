/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-18 23:20:17
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-18 23:20:19
 * @Descripttion:
 */
package config

type UserInfo struct {
	User     string `json:"user" form:"user"`
	Password string `json:"password" form:"password"`
}
