import json

# from test_git import git_demo
# from demo import a
# from test_python.view.po import basePage

# # 模块引用
# print(a)
# basePage()
# git_demo.test_git_demo()
data1 = {
  "name": ["xiaoming","huangxianoming"],
  "age": 18,
  "sex": "f"
}
# f = open("json.json", "a")
j_str = json.dumps(data1)
# j_str = json.dump(data1, f)
print(type(j_str))
j_j = json.loads(j_str)
print(type(j_j))

def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    # inputWords = input.split(" ")
    inputWords = input

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    # output = ' '.join(inputWords)
    output = inputWords

    return output

if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)