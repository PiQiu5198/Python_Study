#有几个Python函数可以帮你处理数值列表。
#例如，你可以轻松地找出数值列表中的最大值、最小值和总和：
digits = list(range(1,10))+[0]
min_digits = min(digits)
max_digits = max(digits)
sum_digits = sum(digits)
print(min_digits,max_digits,sum_digits)