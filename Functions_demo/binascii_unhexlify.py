import binascii

# binascii.b2a_hex(data)和binascii.hexlify(data)：
# 返回二进制数据的十六进制表示。每个字节被转换成相应的2位十六进制表示形式。因此，得到的字符串是是原数据长度的两倍。
# binascii.a2b_hex(hexstr) 和binascii.unhexlify(hexstr)：
# 从十六进制字符串hexstr返回二进制数据。是b2a_hex的逆向操作。
# hexstr必须包含偶数个十六进制数字（可以是大写或小写），否则报TypeError。

a = 'worker'
A = 0x4244
B = '0x424'

b = binascii.b2a_hex(a.encode())
print('b2a_hex:', b)

c = binascii.hexlify(a.encode())
print('hexlify:', c)

d = binascii.a2b_hex(b.decode())
print('b2a_hex:', d)

e = binascii.unhexlify(b.decode())
print('unhexlify', e)

