#要确保字符串右端没有空白，可使用rstrip()方法：
favorite_language = ' Python '
print(f"A{favorite_language}A")
print(f"A{favorite_language.rstrip()}A")

#要确保字符串左端没有空白，可使用lstrip()方法：
print(f"A{favorite_language.lstrip()}A")

#要确保字符串两端都没有空白，可使用strip()方法：
print(f"A{favorite_language.strip()}A")