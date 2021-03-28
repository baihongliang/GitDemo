
def provider():
    for i in range(10):
        print('开始操作')
        yield i
        print('结束操作')

p = provider()
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
for i in p:
    print(i)