'''
Author: WildboarG
version: 1.0
Date: 2023-03-23 14:40:48
LastEditors: WildboarG
LastEditTime: 2023-03-23 16:46:49
Descripttion: 
'''

## 将字符串拆解2个字符为一组，转换为16进制
## 将数据分组
def group_data(hex_str :str)->list:
    list_str = []
    # 每4组添加一个列表
    for i in range(len(hex_str)):
        if i % 2 == 0:
            #print(hex_str[i:i+2], end=' ')
            list_str.append(hex_str[i:i+2])
    list_= []
    for i in range(len(list_str)):
        if i % 4 == 0:
            list_.append(list_str[i:i+4])
    return list_

## 计算出实际的整数值
def get_count(str_list :list)->str:
    sum1 = int(str_list[0], 16)
    sum2 = int(str_list[1], 16)*256+sum1
    sum3 = int(str_list[2], 16)*256*256+sum2
    sum = int(str_list[3], 16)*256*256*256+sum3
    return sum

## 将整数值转换为16进制
def get_data(count :int)->list:
    # 进位不够，补0
    sum = hex(count)
    sum = sum[2:]
    if len(sum) < 8:
        sum = '0'*(8-len(sum))+sum
    #print(sum)
    list_ = []
    for i in range(len(sum)):
        if i % 2 == 0:
            list_.append(sum[i:i+2])
    ## 列表反转
    list_.reverse()
    return list_

## 补位计算
def cover_data(lista :list)->list:
    dat = [0,0,0,0]
    dat[0] = int('ff', 16) - int(lista[0], 16)
    dat[1] = int('ff', 16) - int(lista[1], 16)
    dat[2] = int('ff', 16) - int(lista[2], 16)
    dat[3] = int('ff', 16) - int(lista[3], 16)
    #  长度不够，补0
    for i in range(len(dat)):
        dat[i] = hex(dat[i])[2:]
        if len(dat[i]) < 2:
            dat[i] = '0'*(2-len(dat[i]))+dat[i]
    return dat

## 余额修改写回
def write_data(list_ :list)->str:
    balance_ = get_count(list_[0])
    print("金额:",balance_)
    balance_ = balance_ - 1
    print("余额:",balance_)
    rel_balance = get_data(balance_) # 16进制的余额
    list_[0] = rel_balance
    list_[1] = cover_data(rel_balance)
    list_[2] = rel_balance
    return list_

##  将二维列表中的数据合并为一个字符串
def merge_group(list_ :list)->str:
    str_ = ''
    for i in range(len(list_)):
        for j in range(len(list_[i])):
            str_ = str_ + list_[i][j]
    return str_

if __name__ == '__main__':
    hex_str = '00000100fffffeff0000010099669966'
    list_ = group_data(hex_str)
    print(list_)
    balance_group= write_data(list_)
    print(balance_group)
    hex_str = merge_group(balance_group)
    print(hex_str)

