import binascii

def space_b2a_hex(data):

    new_data_list = list()
    new_data = ""

    # 返回二进制数据的十六进制表示。每个字节被转换成相应的2位十六进制表示形式。因此，得到的字符串是是原数据长度的两倍。
    hex_data = binascii.b2a_hex(data)
    print('hex_data:', hex_data, 'type:', type(hex_data))
    temp_data = ""
    for index, value in enumerate(hex_data):
        print('index:', index, 'value:', value)
        # temp_data += value
    #     if len(temp_data) == 2:
    #         new_data_list.append(temp_data)
    #         temp_data = ""
    # for index,value in enumerate(new_data_list):
    #     if index%25 == 0 and index != 0:
    #         new_data += "\n"
    #     new_data += value
    #     new_data += " "

    return new_data


def hexShow(argv):        #十六进制显示 方法1
    try:
        result = ''
        hLen = len(argv)
        for i in range(hLen):
         hvol = argv[i]
         hhex = '%02x'%hvol
         result += hhex+' '
        print('hexShow:',result)
    except:
        pass

if __name__ == '__main__':
    a = '1234'
    print(type(a.encode()))
    f = space_b2a_hex(a.encode())
    f = hexShow(a)
    f = data= str(binascii.b2a_hex(a.encode()))[2:-1]
    print(f, type(f))