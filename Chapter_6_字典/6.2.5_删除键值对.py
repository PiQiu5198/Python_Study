#对于字典中不再需要的信息，可使用del语句将相应的键值对彻底删除。
#在使用del语句时，必须指定字典名和要删除的键。

#例如，下面的代码从字典alien_0中删除键'points'及其值：
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
#注意：删除的键值对永远消失了。