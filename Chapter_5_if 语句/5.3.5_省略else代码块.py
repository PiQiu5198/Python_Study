#Python并不要求if-elif结构后面必须有else代码块。
#在一些情况下，else代码块很有用；
#而在其他情况下，使用一条elif语句来处理特定的情形更清晰：
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
#elde是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，
#其中的代码就会执行。
#这可能引入无效甚至恶意的数据。
#如果知道要最终测试的条件，应考虑使用一个elif代码块来代替else代码块。
#这样就可以肯定，仅当满足相应的条件时，代码才执行。