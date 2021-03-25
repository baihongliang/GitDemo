

try:
    print(2/0)
except:
    print("异常")
else:
    print("正常")
finally:
    print("无论是否异常，都执行")