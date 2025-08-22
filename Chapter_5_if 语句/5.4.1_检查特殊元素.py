#本章开头通过一个简单的示例演示了如何处理特殊值'bmw'————需要采用不同的格式打印它。
#现在你对条件测试和if语句有了大致的认识，
#下面来进一步研究如何检查列表中的特殊值，并对其做合适的处理。

#继续使用前面的披萨店示例。
#这家披萨店在制作披萨时，每添加一种配料都打印一条消息。
#要以极高的效率编写这样的代码，可以创建一个包含顾客所点配料的列表，
#并使用一个循环来指出添加到披萨中的配料：
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#然而，如果披萨店的青椒（green peppers）用完了，如何处理呢？
#为了妥善地处理这种情况，可在for循环中包含一条if语句：
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are ot of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")