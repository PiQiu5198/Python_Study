#在Python中，第一个列表元素的索引为0，而不是1。
#大多数编程语言是如此规定的，这与列表操作的底层实现有关。

#下面的代码访问索引1和索引3处的自行车：
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
#这些代码返回列表中的第二个和第四个元素。

#Python为访问最后一个列表元素提供了一种特殊语法。
#通过将索引指定为1，可让Python返回最后一个列表元素：
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
#这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素。
#这种约定也适用于其他负数索引：
#例如，索引-2返回倒数第二个列表元素，索引-3返回倒数第三个列表元素，以此类推。