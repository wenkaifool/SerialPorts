import binascii
import platform
if platform.system() == "Windows":
    from serial.tools import list_ports

# temp = list(list_ports.comports())
# print(temp)

# writed_data = "123\n"
# print(type(writed_data))  # str
# print(type(writed_data.encode()))  # bytes

# data = "123\n45  6 78"
# data.strip()
# data = data.replace(" ", "").replace("\n", "")
# data = binascii.unhexlify(data)
# print(data, type(data))
# print(data[0], type(data[0]))
# changeline = '\n'.encode()
# print(changeline, type(changeline))

# data = '3132333435'
# newdata_list = []
# for index, value in enumerate(data):
#     if index%2 == 0 and index != 0:
#         newdata_list.append(' ')
#     newdata_list.append(value)
#
# newdata_list = [str(i) for i in newdata_list]
# newdata_list = ''.join(newdata_list)
# print(b)

comstate = ['No COM']
print(comstate[0])