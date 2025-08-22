#顾客的要求五花八门，在披萨配料方面尤其如此。
#如果顾客要求在披萨中添加炸薯条（French fries），该怎么办呢？
#可以使用列表和if语句来确定能否满足顾客的要求。

#我们来看看如何在制作披萨前拒绝怪异的配料要求。
#这次对于requested_toppings中的每个元素，都先检查它是否是披萨点供应的配料，
#再决定是否在披萨中添加它：
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")