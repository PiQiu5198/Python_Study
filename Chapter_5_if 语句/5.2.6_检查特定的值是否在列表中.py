#有时候，执行操作前必须检查列表是否包含特定的值。
#要判断特定的值是否在列表中，可使用关键字in。

#下面看看你可能会为披萨店编写的一些代码。
#这些代码首先创建一个列表，其中包含用户点的披萨配料，
#然后检查特定的配料是否在该列表中。
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
#关键字in让Python检查列表中是否包含有你输入的值。