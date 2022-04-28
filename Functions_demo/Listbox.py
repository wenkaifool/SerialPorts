import tkinter as tk

master = tk.Tk()

# 创建一个空列表
theLB = tk.Listbox(master)
theLB.pack()

# 往列表里添加数据
for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
    theLB.insert("end", item)

master.mainloop()