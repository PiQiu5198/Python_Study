#Python方法sort()让你能够较为轻松地对列表进行排序。

#假设你有一个汽车列表，并要让其中的汽车按字母顺序排列。
#为简化这项任务，假设列表中的所有值都是全小写的。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#sort()方法能永久地修改列表元素的排列顺序。
#现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序。

#还可以按与字母顺序相反的顺序排列元素，只需向sort()方法传递参数 reverse=true即可。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#同样，对列表元素排列顺序的修改也是永久的。