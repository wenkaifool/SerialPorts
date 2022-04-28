from tkinter import *
import webbrowser


root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'www.baidu.com')

text.tag_add("link", '1.0', '1.9')
text.tag_config('link', foreground='blue', underline=True)


#绑定事件一定要传入event
def show_hand_cursor(event):
    text.config(cursor='arrow')

def show_xterm_cursor(event):
    text.config(cursor='xterm')

def click(event):
    webbrowser.open('www.baidu.com')


#鼠标指向
text.tag_bind('link', '<Enter>', show_hand_cursor)
#鼠标离开
text.tag_bind('link', '<Leave>', show_xterm_cursor)
#左键点击
text.tag_bind('link', '<Button-1>', click)




mainloop()

