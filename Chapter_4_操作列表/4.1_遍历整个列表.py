#你经常要遍历列表的所有元素，对每个元素执行相同的操作。
#如果要对列表中的每个元素都执行相同的操作，可使用Python中的for循环。

#假设我们有一个魔术师名单，需要将其中每个魔术师的名字都打印出来。
#为此，我们可以分别获取名单中的每个名字。
#使用for循环，可以让Python去处理每个元素。
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
#首先，像第3章那样定义了一个列表。
#接下来，定义一个for循环。
#这行代码让Python从列表magicians中取出一个名字，并将其与变量magican相关联。
#最后，让Python打印前面赋给变量magician的名字。
#这样，对于列表中的每个名字，Python都将重复执行最后两行代码。