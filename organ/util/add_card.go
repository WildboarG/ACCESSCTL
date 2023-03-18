/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-09 20:11:43
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-18 18:05:59
 * @Descripttion:
 */
package util

// package main

import (
	"encoding/json"
	"fmt"

	"github.com/syndtr/goleveldb/leveldb"
)

var cardlen int = 10

type rms struct {
	ID_ERR      string
	AL_REGISTER string
	REGISTER    string
	QUERY_OK    string
	QUERY_NO    string
	DELETE      string
	UPDATE      string
}

var Mes rms = rms{"卡号错误",
	"卡号已注册",
	"注册成功",
	"查询成功",
	"查询失败",
	"删除成功",
	"更新成功",
}

func Add_card(db_host string, card string, name string) (mes string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	if len(card) != cardlen {
		// fmt.Println(Mes.ID_ERR)
		fmt.Println("\033[31m" + Mes.ID_ERR + "\033[0m")
		return Mes.ID_ERR
	}
	ret, _ := db.Has([]byte(card), nil)
	if ret {
		fmt.Println("\033[36m" + Mes.AL_REGISTER + "\033[0m")
		return Mes.AL_REGISTER
	}
	err = db.Put([]byte(card), []byte(name), nil) // 写入数据库
	if err != nil {
		panic(err)
	} else {
		data, _ := db.Get([]byte(card), nil)
		fmt.Println("\033[32m" + Mes.REGISTER + string(data) + "\033[0m")
		return Mes.REGISTER
	}
}

// 添加卡片
func Add_cards(db_host string, idd int, name string, sex int, age int, idr string, car string) (mes string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	if len(idr) != cardlen {
		fmt.Println("[添加信息]: " + "\033[31m" + Mes.ID_ERR + "\033[0m")
		return Mes.ID_ERR
	}
	ret, _ := db.Has([]byte(idr), nil)
	if ret {
		fmt.Println("[添加信息]: " + "\033[36m" + Mes.AL_REGISTER + "\033[0m")
		return Mes.AL_REGISTER
	}

	var data = map[string]interface{}{
		"idd":  idd,
		"name": name,
		"sex":  sex,
		"age":  age,
		"idr":  idr,
		"car":  car,
	}
	// fmt.Println(data)
	dx, _ := json.Marshal(data)
	err = db.Put([]byte(string(idr)), []byte(dx), nil) // 写入数据库
	if err != nil {
		panic(err)
	} else {
		data, _ := db.Get([]byte(idr), nil)
		fmt.Println("[" + Mes.REGISTER + "]" + "\033[32m" + string(data) + "\033[0m")
		return Mes.REGISTER
	}
}

// 更新卡片
func Update_cards(db_host string, idd int, name string, sex int, age int, idr string, car string) (mes string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	if len(idr) != cardlen {
		fmt.Println("[变更信息]:" + "\033[31m" + Mes.ID_ERR + "\033[0m")
		return Mes.ID_ERR
	}
	ret, _ := db.Has([]byte(idr), nil)
	if !ret {
		fmt.Println("[变更信息]: " + "\033[36m" + Mes.ID_ERR + "\033[0m")
		return Mes.ID_ERR
	}
	// var  dt []byte
	// var dt = fmt.Sprintf("{\"idd\":\"%d\", \"name\":\"%s\", \"sex\":\"%d\", \"age\":\"%d\",  \"idr\":\"%s\",  \"car\":\"%s\"}", idd, name, sex, age, idr, car)
	var content = map[string]interface{}{
		"idd":  idd,
		"name": name,
		"sex":  sex,
		"age":  age,
		"idr":  idr,
		"car":  car,
	}

	content_data, _ := json.Marshal(content)
	err = db.Put([]byte(string(idr)), []byte(content_data), nil) // 写入数据库
	if err != nil {
		panic(err)
	} else {
		data, _ := db.Get([]byte(idr), nil)
		// fmt.Println(Mes.UPDATE + string(data))
		fmt.Println("[变更信息]: " + "\033[32m" + string(data) + "\033[0m")
		return Mes.UPDATE
	}
}

// 查询卡片
func Query_card(db_host string, idr string) []interface{} {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	// if len(idr) != cardlen {
	// 	fmt.Println(Mes.ID_ERR)
	// 	return
	// }
	ret, _ := db.Has([]byte(idr), nil) // 判断是否存在
	if ret {
		var dat []interface{}
		var dt interface{}
		data, _ := db.Get([]byte(idr), nil)
		json.Unmarshal(data, &dt) // 将value转换为json格式
		dat = append(dat, dt)     // 将json格式的value添加到list中
		// fmt.Println(Mes.QUERY_OK + string(data))
		fmt.Println("[查询信息]: " + "\033[32m" + string(data) + "\033[0m")
		return dat
	} else {
		// fmt.Println(Mes.QUERY_NO)
		fmt.Println("[查询信息]: " + "\033[31m" + Mes.QUERY_NO + "\033[0m")
		a := map[string]string{"err": "查询失败"}
		return append([]interface{}{}, a)
	}
}

// 删除卡片
func Delete_card(db_host string, card string) (mes string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	res, _ := db.Has([]byte(card), nil)
	if res {
		err := db.Delete([]byte(card), nil)
		if err != nil {
			panic(err)
		} else {
			// fmt.Println(Mes.DELETE)
			fmt.Println("[删除信息]: " + "\033[32m" + Mes.DELETE + "\033[0m")
			return Mes.DELETE
		}
	} else {
		// fmt.Println(Mes.ID_ERR)
		fmt.Println("[删除信息]: " + "\033[31m" + Mes.ID_ERR + "\033[0m")
		return Mes.ID_ERR
	}
}

// 删除卡片
func Remove_cards(db_host string, idr string) (mes string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	res, _ := db.Has([]byte(idr), nil)
	// fmt.Println(res)
	if res {
		err := db.Delete([]byte(idr), nil)
		if err != nil {
			panic(err)
		} else {
			//fmt.Println(Mes.DELETE)
			fmt.Println("[删除信息]: " + "\033[32m" + Mes.DELETE + "\033[0m")
			return Mes.DELETE
		}
	} else {
		// fmt.Println(Mes.ID_ERR)
		fmt.Println("[删除信息]: " + "\033[31m" + Mes.ID_ERR + "\033[0m")
		return Mes.ID_ERR
	}
}

// 遍历数据库
func Query_all(db_host string) []interface{} {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}

	defer db.Close()

	var dta []interface{}
	var dt interface{}
	iter := db.NewIterator(nil, nil) // 创建迭代器
	for iter.Next() {                // 遍历数据库
		//key := iter.Key()
		value := iter.Value()
		json.Unmarshal(value, &dt)
		//fmt.Printf("idr=%s, data=%v\n", key, value) // 打印key和value
		dta = append(dta, dt) // 将value添加到切片中
	}

	iter.Release()     // 释放迭代器
	err = iter.Error() // 获取迭代器错误
	if err != nil {
		panic(err)
	}
	return dta
}

// func main() {
// 	Add_cards("leveldb1", 1, "李斯", 1, 18, "0x12345178", "京A12345")
// 	Update_card("leveldb1", 1, "李斯", 1, 18, "0x12345178", "京A12345")
// 	Query_card("leveldb1", "0x12345178")
// 	Remove_card("leveldb1", "0x12345178")
// 	Query_all("leveldb1")
// }
