'''
Author: WildboarG
version: 1.0
Date: 2023-03-23 19:42:43
LastEditors: WildboarG
LastEditTime: 2023-03-23 22:09:25
Descripttion: 
'''
## 将对卡片中的数据操作封装成类
## 基于整数的对数据的加减操作
class Balance:
    def __init__(self,hex_str :str):
        self.hex_str = hex_str
        self.list = self.get_data()
        self.result = self.list
    ## 获取数据,分组
    def get_data(self)->list: ## 将字符串拆解2个字符为一组，转换为16进制,并分组[[整数金额],[补位],[整数金额],[地址偏移]]
        try:
            list_str = []
            list_= []
            # 每4组添加一个列表
            for i in range(len(self.hex_str)):
                if i % 2 == 0:
                    list_str.append(self.hex_str[i:i+2])
            
            for i in range(len(list_str)):
                if i % 4 == 0:
                    list_.append(list_str[i:i+4])
            return list_
        except Exception as e:
            print(e)
            return None
        
    ## 显示余额
    def get_count(self)->str:  ## 计算出实际的整数值
        try:
            str_list = self.list[0]
            sum1 = int(str_list[0], 16)
            sum2 = int(str_list[1], 16)*256+sum1
            sum3 = int(str_list[2], 16)*256*256+sum2
            sum = int(str_list[3], 16)*256*256*256+sum3
            return sum
        except Exception as e:
            print(e)
            return None

    ## 金额转换  10进制转16进制
    def _amount_conversion(self,count :int)->list:
        # 进位不够，补0
        sum = hex(count)
        sum = sum[2:]
        if len(sum) < 8:
            sum = '0'*(8-len(sum))+sum
        list_ = []
        for i in range(len(sum)):
            if i % 2 == 0:
                list_.append(sum[i:i+2])
        ## 列表反转
        list_.reverse()
        return list_
    
    ## 补位计算
    def cover_data(self,lista :list)->list:
        dat = [0,0,0,0]
        try:
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
        except Exception as e:
            print(e)
            return e
    
    ## 余额修改写回的装饰器
    def write_data(func):
        
        def wrap(self,count):
            balance_ = self.get_count()
            print("金额:",balance_)
            balance_ = func(self,count)
            print("余额:",balance_)
            rel_balance = self._amount_conversion(balance_) # 16进制的余额
            self.result[0] = rel_balance
            self.result[1]= self.cover_data(rel_balance)
            self.result[2] = rel_balance
            return self.result
        return wrap   
    
    ##  将二维列表中的数据合并为一个字符串
    def merge_data(self,list_ :list)->str:
        str_ = ''
        try:
            for i in range(len(list_)):
                for j in range(len(list_[i])):
                    str_ = str_ + list_[i][j]
            return str_
        except Exception as e:
            print(e)
            return e
    

        ## 增加余额
    
    @write_data
    def add_count(self,money:int)->int:
        count = self.get_count()
        count += money
        return count
    
    ## 减少后余额
    @write_data
    def reduce_count(self,money :int)->int:
            count = self.get_count()
            count -= money
            return count

# if __name__ == "__main__":
#     balance = Balance('00000100fffffeff0000010099669966')
#     add = balance.reduce_count(65526)
#     print(balance.merge_data(add))
   