#假设有一个URL包含常见的前缀 https://
#而你想要删除这个前缀，只关注用户需要输入地址栏的部分。
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))
#这里在变量名后面加上了句点和removeprefix()方法，并在在括号内输入了要从原始字符串中删除的前缀。