#虽然不能修改元组的元素，但可以给表示元组的变量赋值。
#例如，要修改前述矩形的尺寸，可重新定义整个元组：
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#相比于列表，元组是更简单的数据结构。
#如果要存储一组在程序的整个生命周期内都不变的值，就可以使用元组。