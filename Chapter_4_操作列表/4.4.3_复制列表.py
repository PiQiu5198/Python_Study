#要复制列表，可以创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引([:])。
#这让Python创建一个起始于第一个元素，终止于最后一个元素的切片，即复制整个列表。

#假设有一个列表包含你最喜欢的四种视频，而你想再创建一个列表，并在其中包含你的一个朋友喜欢的所有食品。
#巧的是，你喜欢的视频，这个朋友也都喜欢，因此可以通过复制这个列表来创建新的列表：
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#为了核实确实有两个列表，下面在每个列表中都添加一种食品，并确认每个列表都记录了相应人喜欢的食品：
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#如果只是将my_foods赋给friend_foods，就不能得到两个列表。
#例如，下面演示了在不适用切片的情况下复制列表的情况：
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
#这里将my_foods赋给friend_foods，而不是将my_foods的副本赋给friend_foods。
#这种做法实际上是让python将新变量friend_foods关联到已与my_foods相关联的列表，因此这两个变量指向同一个列表。
#有鉴于此，当我们将'cannoli'添加到my_foods中时，他也将出现在friend_foods中。
#同样，虽然'ice cream'好像只被加入了friend_foods，但它也将同时出现在这两个列表中。