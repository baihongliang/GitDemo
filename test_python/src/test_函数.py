"""
# 最旧的字符串格式化写法
print('name is : %s, age is %d'%(name,age))
# 旧的
print('name is : {}, age is {}'.format(name, age))
# 新的，官方推荐
print(f'name is : {name}, age is {age}')

"""
name,age = 'xiaoxio', 18
# 最旧的字符串格式化写法
print('name is : %s, age is %d'%(name,age))
# 旧的
print('name is : {}, age is {}'.format(name, age))
# 新的，官方推荐
print(f'name is : {name}, age is {age}')

x = 1
# f-String也支持表达式
print(f'这是一个lambda表达式{(lambda x:x+1)(x)}')

print(f'这是一个lambda表达式{(lambda x,y:x*y)(x,x)}')

data = [1,2]
print(f'这是一个lambda表达式{(lambda x,y:x*y)(data[0],data[1])}')
# * **解包
print(f'这是一个lambda表达式{(lambda x,y:x*y)(*data)}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 'sttt'}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:s}'.format(**table))

# print(data[-1::-1]) # 倒序
data.reverse()
print(data)
data.sort()
print(data)

data.append(3)
print(data)
data.reverse()
print(data.pop())
print(data)