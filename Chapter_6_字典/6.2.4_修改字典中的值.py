#要修改字典中的值，可依次指定字典名、用方括号括起来的键和与该键关联的新值。
#假设随着游戏的进行，需要将一个外星人从绿色改为黄色：
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

#来看一个更有趣的例子：对一个能够以不同速度移动的外星人进行位置跟踪。
#为此，存储该外星人的当前速度，并据此确定该外星人应该向右移动多远：
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Origional position: {alien_0['x_position']}")

#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的移动速度为快
    x_increment = 3

#新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")
#这种技巧很棒：通过修改外星人字典中的值，可改变外星人的行为。
#例如，要将这个速度中等的外星人变成速度很快的外星人，可添加如下代码行：
#alien_0['speed'] = 'fast'
#这样，再次运行这些代码，if-elif-else语句将把一个更大的值赋给变量x_incerment。