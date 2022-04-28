import serial.tools.list_ports
import serial

# https://blog.csdn.net/weixin_44344195/article/details/117218384?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0.pc_relevant_aa&spm=1001.2101.3001.4242.1&utm_relevant_index=3
plist = list(serial.tools.list_ports.comports())    #获取端口列表
print(plist)

for port in plist:
    print('端口号：' + port[0] + '   端口名：' + port[1])

# 打开串口
port = serial.Serial(port = 'COM3', baudrate = 2400, bytesize = 8
                         , parity = 'E', stopbits = 1 , timeout= 1.0)
print(port.isOpen())

# 通过write()函数即可向端口写如数据
data = [0x68 ,0x03 ,0x21 ,0x00 ,0x48 ,0x16]
port.write(data)

# 由于终端的特性，有时候在读取串口时无法将所有数据都读出，这边可以使用延时函数将程序延时一段时间来让返回的数据可以全部被接受到
sleep(2.0)
data = serial.read_all()