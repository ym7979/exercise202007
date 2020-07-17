"""
拷贝文件
"""
filename=input("文件:")

fr=open(filename,"rb")
filename=filename.split("/")[-1]
fw=open("/home/yuanchao/ym/month06/myp/exercise/file/"+filename,"wb")

# 边读边写
while True:
    data=fr.read(1024)
    if not data:
        break

    fw.write(data) # 写入新文件
