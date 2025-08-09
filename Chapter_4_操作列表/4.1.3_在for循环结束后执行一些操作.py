#在for循环后面，没有缩进的代码都只执行一次，不会重复执行。

#下面打印一条向全体魔术师致谢的消息，感谢他们的精彩表演。
#我们将相应的代码放在for循环后面，且不缩进：
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")