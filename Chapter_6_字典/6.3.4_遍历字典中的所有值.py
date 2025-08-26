#如果你感兴趣的是字典包含的值，可使用values()方法。
#它会返回一个值列表，不包含任何键。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
#这条for语句提取字典中的每个值，并将它们依次赋给变量language。
#这种做法提取字典中的所有值，而没有考虑是否有重复。
#当涉及的值很少时，这也许不是问题，但如果被调查者很多，最终列表可能有大量重复项。
#为剔除重复项，可使用集合（set）。
#集合中的每个元素必须是独一无二的。
for language in set(favorite_languages.values()):
    print(language.title())
#注意：可以使用一对花括号直接创建集合，并在其中用逗号分隔元素：
languages = {'python', 'rust', 'python', 'c'}
print(languages)
#集合和字典很容易混淆，因为它们都是用一对花括号定义的。
#当花括号内没有键值对时，定义的很可能是集合。
#不同于列表和字典，集合不会以特定的顺序存储元素。