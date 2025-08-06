#要保留列表元素原来的排列顺序，并以特定的顺序呈现它们，可使用sorted()函数。
#sorted()函数让你能够按特定顺序显示列表元素，同时不影响它们在列表中的排列顺序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
#注意，在调用sorted()函数后，列表元素的排列顺序并没有变。
#如果要按与字母顺序相反的顺序显示列表，也可向sorted()函数传递参数reverse=True。

#注意：在并非所有的值都是全小写的时，按字母顺序排列列表要复杂一些。
#在确定排列顺序时，有多种解读大写字母的方式，此时要指定准确的排列顺序，可能会比这里所做的更复杂。
#然而，大多数排列方式是以本书介绍的知识为基础的。