"""从单词本里 查单词"""

word=input("请输入单词")

f=open("dict.txt")

# 每次取一行
for line in f:
    w=line.split(" ",1)[0] #取单词
    if w>word:
        print("没有找到该单词")
        break
    if w==word:
        print(line)
        break

else:
    print("没有找到该单词")