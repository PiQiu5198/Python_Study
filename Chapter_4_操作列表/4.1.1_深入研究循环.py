#循环很重要，它是让计算机自动完成重复工作的常见工作方法之一。

#例如，在前面中使用的简单循环里，Python将首先读取第一行代码：
#for magician in magicians:
#这行代码会让Python获取列表magicians中的第一个值'alice'。
#并将其与变量magician相关联。
#接下来，Python读取下一行代码：
#    print(magician)
#它让Python打印magician的值，依然是'alice'。
#鉴于该列表还包含其他值，Python返回循环的第一行：
#for magician in magicians:
#Python获取列表中的下一个名字'david'，并将其与变量magician相关联，再执行下面这行代码：
#    print(magician)
#Python再次打印变量magician的值，当前为'david'。
#接下来Python再次执行整个循环，对列表中的最后一个值'carolina'进行处理。
#至此，列表中没有其他的值，因此Python接着执行程序下一行代码。
#由于此示例中，for循环后没有其他代码，因此程序就此结束。

#刚开始使用循环时请牢记，不管列表包含多少个元素，每个元素都将被执行循环指定的步骤。
#如果列表包含100万个元素，Python就将重复执行指定的步骤100万次，而且速度很快。

#在编写for循环时，可以给将依次与列表中的每个值相关联的临时变量指定任意名称。
#然而，选择描述单个列表元素的有意义的名称大有裨益。
#例如，对于小猫小狗列表和一般性列表，像下面这么写for循环的第一行代码很不错：
#for cat in cats:
#for dog in dogs:
#for item in list_of_items:
#使用单数和复数形式的名称，可以帮助你判断代码段处理的是单个列表元素还是整个列表。