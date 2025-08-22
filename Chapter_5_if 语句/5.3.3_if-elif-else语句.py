#你经常需要检查两个以上的情形，此时可以使用Python提供的if-elif-else语句。
#Python只执行if-elif-else结构中的一个代码块。
#它依次检查每个条件测试，直到遇到通过了的条件测试。
#条件测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的条件测试。

#在现实世界中，需要考虑的情形通常会超过两个。
#例如，来看一个根据年龄阶段收费的游乐场。
#1.四岁以下免费。
#2.4（含）~18岁收费25美元。
#3.年满18岁收费40美元。

#如果只使用一条if语句，该如何确定门票价格呢？
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
#第一个条件测试未通过，执行下面的条件测试，
#第二个条件测试通过，执行第二个条件测试后面的代码，
#忽略第三个条件测试。

#为了让代码更简洁，可不在if-elif-else代码块中打印门票价格，
#而是只在其中设置门票价格，并在他们后面添加一个函数调用print():
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
#这些代码的输出与上一个示例相同，但if-elif-else语句所做的事情更少：
#它只确定门票价格，而不是在确定门票价格的同时打印一条消息。
#除了效率更高意外，这些修订后的代码还更容易修改：
#要调整输出消息的内容，只需修改一个而不是三个函数调用print()。