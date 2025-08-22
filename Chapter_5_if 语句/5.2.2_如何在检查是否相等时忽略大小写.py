#在Python中检查是否相等时是区分大小写的。
#例如，两个大小写不同的值被视为不相等：、
car = 'Audi'
print(car == 'audi')
#但如果大小写无关紧要，你只想要检查变量的值，
#可以先将变量的值转换为全小写的，再进行比较：
car = 'Audi'
print(car.lower()=='audi')