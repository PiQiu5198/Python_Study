#有时候，需要将列表存储在字典中，而不是将字典存储在列表中。
#例如，如何描述顾客点的披萨呢？
#如果使用列表，只能存储要添加的披萨配料；
#但是如果使用字典，其中的配料列表就只是用来描述披萨的一个方面。

#在下面的示例中，存储了披萨两个方面的信息：外皮类型和配料列表。
#配料列表是一个与键'toppings'关联的值。
#要访问该列表，我们使用字典名和键'toppings'，就像访问字典中的其他值一样。
#这将返回一个配料列表，而不是单个值：
##存储顾客所点的披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

##描述顾客点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

#每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
#在本章前面有关喜欢的编程语言的示例中，如果将每个人的回答都存储在一个列表中，
#被调查者就可以选择多种喜欢的语言。
#在这种情况下，当我们遍历字典时，与每个被调查者关联的都是一个语言列表，而不是一种语言。
#因此，在遍历该字典的for循环中，需要再使用一个for循环来遍历与被调查者关联的语言列表：
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
#注意：列表和字典的嵌套层级不应太多。
#     如果嵌套层级比前面的示例多得多，很有可能有更简单的解决方案。