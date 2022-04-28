import binascii
data = '12  4  \n5'
print(data)
data1 = data.replace(" ", "").replace("\n", "")
print(data1)
data2 = binascii.unhexlify(data1)
print(data2)