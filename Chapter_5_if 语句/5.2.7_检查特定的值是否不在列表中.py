#还有些时候，确定特定的值不在列表中很重要。
#这种情况下，可使用关键字not in。
#例如有一个列表包含被禁止在论坛上发表评论的用户，
#这样就可以在允许用户提交评论前检查他是否被禁言了：
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")