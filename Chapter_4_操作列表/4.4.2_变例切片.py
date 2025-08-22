#如果要遍历列表的部分元素，可在for循环中使用切片。

#下面的示例遍历前三名队员，并打印他们的名字：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())