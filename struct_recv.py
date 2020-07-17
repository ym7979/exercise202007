from socket import *
import struct

# 与客户端协商后的格式 id  name age score
st = struct.Struct("i32sif")

# udp 套接字
s = socket(AF_INET, SOCK_DGRAM)
s.bind('0.0.0.0', '7979')

# 打开文件
f = open('student.txt', 'a')

while True:
    data,addr=s.recvfrom(1024)
    # data -->bytes(1.'lily',18,92.5)
    data=st.unpack(data)
    if data[3]>=90:
        info= "%d %10s %d %f \n"%data
        f.write(info)
        f.flush()



f.close()
s.close()


