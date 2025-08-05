name = "ada lovelace"
print(name.title())
#方法(method)是Python可对数据执行的操作。
#在name.title()中，name后面的句点(.)让Python对name变量执行title()方法指定的操作。
#方法后面都跟着一对括号()，这是因为方法通常需要额外的信息来完成工作。
#title()方法以首字母大写的方式显示每个单词。

name = "Ada Lovelace"
print(name.upper()) #全大写 
print(name.lower()) #全小写
#在存储数据时，lower()方法很有用。
#用户通常不能像你期望的那样提供正确的大小写，因此可以先全转化成小写再储存。