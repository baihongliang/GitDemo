import random

print("11111")
print('222')

s = "hello"
# 打印字符串hello
print(s)
# 打印变量内存地址140529612393328
print(id(s))
# 打印%格式化字符串 Python has 002 quote types.
print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})
# 打印f格式化字符串 hello world
print(f'{s} world')
print('abc\n')
# r 忽略转义
print(r'abc\n')

a = 1
if a == 1:
    print('a=1')
elif a == 2:
    print('a=2')
else:
    print('asdfsdf')

if 0 < a < 2:
    print(232)

while a<5:
    print(a)
    a+=1

result =0;
for i in range(2,101,2):
    result+=i
    # print(result)

pc_num = random.randint(1,100)
print(pc_num)

while True:
    p_num = int(input('请输入一个数字'))
    if p_num > pc_num:
        print("小一点")
    elif p_num < pc_num:
        print("大一点")
    elif p_num == pc_num:
        print("猜对了")
        break
