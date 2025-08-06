##1.使用del语句删除元素

#如果你知道要删除的元素在列表中的位置，可以使用del语句：
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
#这里使用del语句删除了列表motorcycles中的第一个元素'honda'。
#使用del语句可删除任意位置的列表元素，只需知道其索引即可。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
#在这两个示例中，使用del语句将值从列表中删除以后，你就无法再访问它了。



##2.使用pop()方法删除元素

#有时候，你要将元素从列表中删除，并接着使用它的值。
#pop()方法删除列表末尾的元素，并让你能接着使用它。
#术语弹出（pop）源自这样的类比：
#列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。

#下面来从列表motorcycles中弹出一款摩托车：
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
#首先定义并打印了列表motorcycles。
#接下来，从这个列表中弹出一个值，并将其赋给变量popped_motorcycle。
#然后打印这个列表，以核实从中删除了一个值。
#最后打印弹出的值，以证明依然能够访问被删除的值。
#输出表明，列表末尾的值'suzuki'已删除，它现在被赋给了变量popped_motorcycle。

#方法pop()有什么用呢？
#假设列表中的摩托车是按购买时间存储的，就可用方法pop()来打印一条信息，指出最后购买的是哪款摩托车：
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
#输出是一个简单的句子，指出了最新购买的是哪款摩托车。


##3.删除列表中任意位置的元素

#实际上，也可以用pop()删除列表中任意位置的元素，只需要再括号中指定要删除的元素的索引即可。
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
#别忘了，每当你使用pop()时，被弹出的元素就不在列表中了。

#如果不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：
#如果要从列表中删除一个元素，且不再以任何方式使用它，就用del语句；
#如果要在删除元素后继续使用它，就使用pop()方法。



##4.根据值删除元素

#如果只知道要删除的元素的值，可使用remove()方法。
#假设要从列表motorcycles中删除'ducati'：
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#remove()方法让Python确定'ducati'出现在列表的什么地方，并将该元素删除。

#使用remove()方法从列表中删除元素后，也可以继续使用它的值。
#下面删除值'ducati'并打印一条消息，指出将其从列表中删除的原因：
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
#注意：remove()方法只删除第一个指定的值。
#     如果要删除的值可能在列表中出现多次，就需要使用循环，确保将每个值都删除。