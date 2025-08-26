#在不需要使用字典中的值时，key()方法很有用。
#下面来遍历字典favorite_languages，并将每个被调查者的名字都打印出来：
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())
#在遍历字典时，会默认遍历所有的键。
#因此，如果将上述代码中的
#for name in favorite_languages.keys():
#替换为
#for name in favorite_languages:
#输出将不变。
#如果显式地使用keys()方法能让代码更容易理解，就可以选择这样做，
#但如果你愿意，也可以省略它。
#在这种循环中，可使用当前的键来访问与之关联的值。
#下面来打印两条消息，来指出两个朋友喜欢的编程语言。
#我们像前面一样遍历字典中的名字，但在名字为指定朋友的名字时，
#打印一条消息，指出其喜欢的语言：
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
#还可以使用keys()确定某个人是否接受了调查。
#下面的代码确定Erin是否接受了调查：
if 'erin' not in favorite_languages.keys():
    print("Erin, Please take our poll!")
#keys()方法并非只能用于遍历：实际上，它会返回一个列表，其中包含字典中的所有键。
#因此if语句只核实'erin'是否在这个列表中。
#因为她并不在这个列表中，所以打印一条消息，邀请她参与调查。