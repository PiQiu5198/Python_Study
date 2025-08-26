#在探索各种遍历方法之前，先来看一个新字典，它用于存储有关网站用户的信息。
#这个字典存储一个用户的用户名、名和姓：
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'feimi'
}
#利用本章前面介绍过的知识，可访问user_0的任意一项信息，
#但如果要获悉该用户字典中的所有信息，该怎么办呢？
#可使用for循环来遍历这个字典：
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#在前面例子中，字典存储了人名和他们喜欢的编程语言，
#我们使用变量name和language来表示键值对：
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
#这些代码让Python遍历字典中的每个键值对，并将键赋给变量name，将值赋给变量language。
#这些描述性名称让人能够非常轻松地明白函数调用print()是做什么的。