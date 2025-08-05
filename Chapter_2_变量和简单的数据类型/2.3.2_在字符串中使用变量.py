first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
#这种字符串称为f字符串。
#f是format(设置格式)的简写，因为Python通过把花括号内的变量替换为其值来设置字符串的格式。

#使用f字符串可以完成很多任务，如利用与变量关联的信息来创建完整的信息，如下所示：
print(f"Hello, {full_name.title()}!")

#还可以使用f字符串来创建信息，再把整条信息赋给变量：
message = f"Hello, {full_name.title()}!"
print(message)