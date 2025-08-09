#Python函数range()让你能够轻松地生成一系列的数。

#例如，可以像下面这样使用range()函数来打印一系列的数：
for value in range(1,5):
    print(value)
#在这个示例中，range()只打印1~4，这是编程语言中常见的差一行为的结果。
#range()函数让Python从指定的第一个值开始数，并在到达指定的第二个值时停止，因此不包含第二个值（这里为5）。
#要打印1~5，需要使用range(1,6)：
for value in range(1,6):
    print(value)
#在调用range()函数时，也可以只指定一个数，这样它将从0开始，例如range(6)返回数0~5（含）。