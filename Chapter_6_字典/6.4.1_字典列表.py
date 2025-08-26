#字典alien_0包含一个外星人的各种信息，但无法存储第二个外星人的信息。
#如何管理成群结队的外星人呢？
#一种办法是创建一个外星人列表，其中每个外星人都是一个字典，包含有关该外星人的各种信息。
#例如，下面的代码创建一个包含三个外星人的列表：
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

alines = [alien_0, alien_1, alien_2]

for alien in alines:
    print(alien)
#更符合现实情况的是，外星人不止三个，而且每个外星人都是用代码自动生成的。
#在下面的示例中，使用range()生成了30个外星人：
##创建一个用于存储外星人的空列表
aliens = []

##创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

##显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

##显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")
#这些外星人都具有相同的特征，但在Python看来，每个外星人都是独立的，这让我们能够独立地修改每个外星人。

#在什么情况下需要处理成群结队的外星人呢？
#想象一下，随着游戏的进行，有些外星人会变色且加快速度。
#在必要时，可使用for循环和if语句来修改某些外星人的颜色。
#例如，要将前三个外星人修改为黄色、速度中等且值10分，可这样做：
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
##显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#可进一步扩展这个循环，在其中添加一个elif代码块，
#将黄色外星人改为移动速度快且值15分的红色外星人，如下所示：
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#你经常需要在列表中存储大量的字典，而且每个字典都包含特定对象的众多信息。
#例如，为网站的每个用户创建一个字典，并将这些字典存储在一个名为users的列表中。
#在这个列表中，所有字典的结构都相同，因此可以遍历这个列表，并以相同方式处理其中每个字典。