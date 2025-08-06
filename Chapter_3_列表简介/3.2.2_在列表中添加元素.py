##1.在列表末尾添加元素

#在列表中添加新元素时，最简单的方法是将元素追加（append）到列表末尾。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
#append()方法将元素'ducati'添加到列表末尾，而不影响列表中的其他所有元素。

#append()方法让动态地创建列表易如反掌。
#例如你可以先创建一个空列表，再使用一系列函数调用append()添加元素。
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)



##2.在列表中插入元素

#使用insert()方法可在列表中的任意位置添加新元素。
#为此，需要指定新元素的索引和值：
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
#在这个示例中，值'ducati'被插入到了列表开头。
#这种操作将导致列表中每个既有元素都右移一个位置。