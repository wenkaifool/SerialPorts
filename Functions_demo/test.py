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

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()