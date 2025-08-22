#要判断两个值是否不等，可使用不等运算符（!=）。
#下面使用一条if语句来演示如何使用不等运算符。

#我们将把顾客点的披萨配料（topping）存储在一个变量中，
#再打印一条消息，指出这名顾客点的配料是否是意式小银鱼（anchovies）：
request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print("Hold the anchovies!")
#你编写的大多数条件表达式会检查两个值是否相等，
#但有时候检查两个值是否不等的效率更高。