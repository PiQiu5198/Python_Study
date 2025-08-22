#最简单的if语句只有一个条件测试和一个操作：
#if conditional_test:
#   do something
#第一行可包含任意条件测试，而在紧跟在测试后面的缩进代码块中，可执行任意操作。
#如果条件测试的结果为True，Python就会执行紧跟在if语句后面的代码，
#否则Python将忽略这些代码。

#假设有一个表示某个人年龄的变量，而你想知道这个人是否到了投票的年龄，
#可使用如下代码
age = 19
if age >= 18:
    print("You are old enough yo vote!")
#在if语句中，缩进的作用与for循环中相同。
#如果条件测试通过了，将执行if语句后面所有缩进的代码行，
#否则将忽略它们。

#可根据需要，在紧跟在if语句后面的代码块中添加任意数量的代码行。
#下面在一个人已到投票年龄时再打印一行输出，问他是否登记了：
age = 19
if age >= 18:
    print("You are old enough yo vote!")
    print("Have you registered to vote yet?")