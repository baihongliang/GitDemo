import glob
import os

print(os.listdir('/'))
print(os.getcwd())

if not os.path.exists("test"):
    os.mkdir("test")

if not os.path.exists("test/test.txt"):
    f = open("test/test.txt","w")
    f.write("hello world")
    f.close()

print(glob.glob("*.py"))