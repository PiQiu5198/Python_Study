#还可以根据需要使用任意数量的elif代码块。
#假设前述游乐场要给老年人打折，
#可再添加一个条件测试，判断顾客是否符合打折条件。

#下面假设年满65岁的老人可半价（即20美元）购买门票：
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age <65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")