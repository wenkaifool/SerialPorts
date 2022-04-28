import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.pack()

# "insert" 索引表示插入光标当前的位置
text.insert("insert", "I love ")
text.insert("end", "Python.com!")

root.mainloop()