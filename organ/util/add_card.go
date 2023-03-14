/*
 * @Author: WildboarG
 * @version: 1.0
 * @Date: 2023-03-09 20:11:43
 * @LastEditors: WildboarG
 * @LastEditTime: 2023-03-11 11:01:36
 * @Descripttion:
 */
package util

import (
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
}

// 实例化一个消息结构体
var Mes rms = rms{"卡号错误", "卡号已注册", "注册成功", "查询成功", "查询失败", "删除成功"}

func Add_card(db_host string, card string, name string) (mes string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	if len(card) != cardlen {
		fmt.Println(Mes.ID_ERR)
		return Mes.ID_ERR
	}
	ret, _ := db.Has([]byte(card), nil)
	if ret {
		fmt.Println(Mes.AL_REGISTER)
		return Mes.AL_REGISTER
	}
	err = db.Put([]byte(card), []byte(name), nil) // 写入数据库
	if err != nil {
		panic(err)
	} else {
		data, _ := db.Get([]byte(card), nil)
		fmt.Println(Mes.REGISTER + string(data))
		return Mes.REGISTER
	}

}

// 查询卡片
func Query_card(db_host string, card string) (data string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	if len(card) != cardlen {
		fmt.Println(Mes.ID_ERR)
		return
	}
	ret, _ := db.Has([]byte(card), nil)
	if ret {
		data, _ := db.Get([]byte(card), nil)
		fmt.Println(Mes.QUERY_OK + string(data))
		return string(data)
	} else {
		fmt.Println(Mes.QUERY_NO)
		return "Null"
	}

}

// 删除卡片
func Delete_card(db_host string, card string) (mes string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	if len(card) != cardlen {
		fmt.Println(Mes.ID_ERR)
		return Mes.ID_ERR
	}
	ret, _ := db.Has([]byte(card), nil)
	if ret {
		err := db.Delete([]byte(card), nil)
		if err != nil {
			panic(err)
		} else {
			fmt.Println(Mes.DELETE)
			return Mes.DELETE
		}
	} else {
		fmt.Println(Mes.ID_ERR)
		return Mes.ID_ERR
	}
}

// 遍历数据库
func Showdb(db_host string) {
	db, err := leveldb.OpenFile(db_host, nil)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	iter := db.NewIterator(nil, nil) // 创建迭代器
	for iter.Next() {                // 遍历数据库
		key := iter.Key()
		value := iter.Value()
		fmt.Printf("key=%s, value=%s\n", key, value) // 打印key和value
	}
	iter.Release()     // 释放迭代器
	err = iter.Error() // 获取迭代器错误
	if err != nil {
		panic(err)
	}
}

// func main() {
// 	Add_card("0xd218982f", "MM12123")
// }
