#在for循环中，可以对每个元素执行任意操作。

#下面来扩展前面的示例，为每位魔术师打印一条消息，指出他/她的表演太精彩了：
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
#在for循环中，想包含多少行代码都可以。
#在代码行for magician in magicians后面，每行缩进的代码都是循环的一部分，将针对列表中的每个值执行一次。
#因此，可以对列表中每个值执行任意多操作。

#下面再来添加一行代码，告诉每位魔术师，我们期待他/她的下一次表演：
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")