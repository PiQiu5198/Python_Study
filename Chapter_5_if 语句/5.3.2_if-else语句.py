#你经常需要在条件测试通过时执行一个操作，在没有通过时执行另一个操作。
#在这种情况下，可使用Python提供的if-else语句。
#if-else语句块类似于简单的if语句，
#但其中的else语句让你能够指定条件测试未通过时要执行的操作。

#下面的代码在一个人已到投票年龄时显示与前面相同的消息，
#在不到投票年龄时显示一条新消息：
age = 17
if age >= 18:
    print("You are old enough yo vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")