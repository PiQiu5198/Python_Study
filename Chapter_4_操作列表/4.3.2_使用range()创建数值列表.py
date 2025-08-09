#要创建数值列表，可使用list()函数将range()的结果直接转换为列表。

#如果将range()作为list()的参数，输出将是一个数值列表，例如：
numbers = list(range(1,6))
print(numbers)
#在使用range()函数时，还可以指定步长。
#为此，可以给这个函数指定第三个参数，Python将根据这个步长来生成数。

#例如，下面的代码打印1~10的偶数：
even_numbers = list(range(2,11,2))
print(even_numbers)
#使用range()函数，几乎能够创建任意数值集合。

#例如，创建一个列表，包含前10个整数（1~10）的平方和：
#在Python中，用两个（**）表示乘方运算：
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)
#为了让代码更简洁，可不使用临时变量square，而是直接将计算得到的每个值追加到列表末尾：
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

#在创建更复杂的列表时，可使用上述两种方法的任意一种。
#有时候，使用临时变量会让代码更易懂；
#而在其他时候，这样做只会让代码无谓地变长。
#你首先应该考虑的是，编写清晰易懂且能完成所需功能的代码，等待审核代码时，再考虑更高效的方法。S