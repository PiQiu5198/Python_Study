#前面介绍的生成列表squares的方法包含三四行代码，而列表推导式让你只需编写一行代码就能生成这样的列表。
#列表推导式（list comprehension）将for循环和创建新元素的代码合并成一行，并自动追加新元素。
squares = [value * 2 for value in range(1, 11)]
print(squares)