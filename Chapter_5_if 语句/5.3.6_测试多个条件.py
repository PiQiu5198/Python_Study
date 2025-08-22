#if-elif-else语句虽然功能强大，但仅适用于只有一个条件满足的情况：
#在遇到通过了的条件测试后，Python就会跳过余下的条件测试。
#这种行为很好，效率很高，让你能够测试一个特定的条件。

#然而，有时候必须检查你关心的所有条件。
#在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。
#在可能有多个条件为True，
#且需要在每个条件为True时都采取相应措施时，适合使用这种方法

#下面再来看看前面的披萨店示例。
#如果顾客点了两种配料，就需要确保在其披萨中放入这些配料：
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#如果像下面这样转而使用if-elif-else语句，代码将不能正确运行，
#因为只要有一个条件测试通过，就会跳过余下的条件测试：
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
#代码执行将忽略第一个if条件测试之后的所有语句。

#总之，如果只想运行一个代码块，就是用if-elif-else语句；
#如果要运行多个代码块，就使用一系列独立的if语句。