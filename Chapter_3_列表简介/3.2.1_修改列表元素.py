#要修改列表元素，可指定列表名和要修改的元素的索引，再指定该索引位置上的新值。

#假设有一个摩托车列表，其中的第一个元素为'honda'，那么可在创建列表后修改这个元素的值：
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#首先定义列表motorcycles，其中的第一个元素为'honda'。
#接下来将第一个元素的值改为'ducati'。
#输出表明，第一个元素的值变了，但其他列表元素的值没变。
#你可以修改任意列表元素的值，而不只是第一个元素的值。