# <Button-1>表示鼠标左键，
# <Button-2>表示鼠标中键，
# <Button-3>表示鼠标右键，
# <Button-4>表示滚轮上滑（Linux）,
# <Button-5>表示滚轮下滑（Linux）,
# 而fun表示点击后发生的事件
from tkinter import *

root = Tk()

def callback(event):
    print(event.x,event.y)

frame = Frame(root,width=200,height=200)
frame.bind('<Double-Button-1>',callback)
frame.pack()

mainloop()
