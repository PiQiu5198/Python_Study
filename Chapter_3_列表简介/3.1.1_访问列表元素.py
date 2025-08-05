#列表是有序集合，因此要访问列表的任意元素，只需要将该元素的位置（索引）告诉Python即可。
#要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在方括号内。

#例如，下面代码从列表bicycles中提取第一款自行车：
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
#当你请求获取列表元素时，Python只返回该元素，而不包括方括号。

#你还可以对任意列表元素调用第2章介绍的字符串方法。
#例如，可使用title()方法让元素'trek'的格式更标准：
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())