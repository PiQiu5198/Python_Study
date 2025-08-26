#遍历字典时将按插入元素的顺序返回其中的元素，但是在一些情况下，
#你可能要按与此不同的顺序遍历字典。
#要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序。
#为此，可使用sorted()函数来获得按特定顺序排列的键列表的副本：
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
#这条for语句类似于其他for语句，但对方法dictionary.keys()的结果调用了sorted()函数。
#这让Python获取字典中的所有键，并在遍历前对这个列表进行排序。
#输出表明，按字母顺序显示了所有被调查者的名字。