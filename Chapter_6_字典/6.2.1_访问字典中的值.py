#要获取与键关联的值，可指定字典名并把键放在后面的方括号里，如下所示：
alien_0 = {'color': 'green'}
print(alien_0['color'])
#这将返回字典alien_0中与键'color'关联的值。

#字典中可包含任意数量的键值对。
#例如，最初的字典alien_0就包含两个键值对：
alien_0 = {'color': 'green', 'points': 5}
#现在，你可以访问外星人alien_0的颜色和分数。
#如果玩家消灭了这个外星人，就可以使用下面的代码来确定玩家应获得多少分：
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
#如果在外星人被消灭时运行这段代码，就将获取外星人的分数。