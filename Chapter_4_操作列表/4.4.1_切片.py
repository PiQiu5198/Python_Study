#处理列表的部分元素，在python中称为切片（slice）

#要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
#与range()函数一样，Python在到达指定的第二个索引之前的元素时停止。
#要输出列表中的前三个元素，需要指定索引0和3，这将返回索引分别为0、1和2的元素。

#下面的示例处理的是一个运动员成员列表：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#你可以生成列表的任意子集。
#例如，如果要提取列表的第二、第三和第四个元素，可将起始索引指定为1，并将终止索引指定为4：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

#如果没有指定第一个索引，Python将自动从列表开头开始：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

#要让切片终止于列表末尾，也可使用类似的语法。
#例如，如果要提取从第三个元素到列表末尾的所有元素，可将起始索引指定为2，并省略终止索引：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

#无论列表多长，这种语法都能让你输出从特定位置到列表末尾的所有元素。
#负数索引返回与列表末尾有相应距离的元素，因此可以输出列表末尾的任意切片。
#如果要输出名单上最后三名队员的名字，可使用切片：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#注意：可在表示切片的方括号内指定第三个值。
#这个值告诉Python在指定范围内每隔多少元素提取一个。