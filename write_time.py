import time

f = open('file.txt', 'a+')
f.seek(0) # 将文件偏移量 移动到开始位置 参数(0,0)第二个0表示从开始位置，可省略

# 计算文件有多少行
n = 0
for line in f:
    n+=1

while True:
    n += 1
    d="%d. %s\n"%(n, time.time())
    data = f.write(d)
    time.sleep(2)
    f.flush()
    print(data)

