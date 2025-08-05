#你可以像使用其他变量一样使用列表中的各个值。
#例如，可以使用f字符串根据列表中的值来创建消息。

#下面尝试从列表中提取第一款自行车，并使用这个值创建一条消息：
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
#这里使用bicycle[0]的值生成了一个句子，并将其赋给变量message。