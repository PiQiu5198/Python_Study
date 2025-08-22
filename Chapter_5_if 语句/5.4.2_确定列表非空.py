#到目前为止，我们对于要处理的每个列表都做了一个简单的假设————它们都至少包含一个元素。
#因为马上就要让用户来提供存储在列表中的信息，所以不能再假设循环运行时刻列表非空。
#有鉴于此，在运行for循环前确定列表非空很重要。

#下面在制作披萨前检查顾客点的配料列表是否为空。
#如果列表为空，就向顾客确认是否要点原味披萨（plain pizza）；
#如果列表非空，就像前面示例那样制作披萨：
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#Python将在列表至少包含一个元素时返回True。
#在列表为空时返回False。
#注：对于数值0、空值None、单引号空字符串''、双引号空字符串""、
#    空列表[]、空元组()、空字典{}，Python都会返回False。