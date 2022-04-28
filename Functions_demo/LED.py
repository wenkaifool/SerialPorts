import tkinter as tk

i=0
def flash(event):
    global i
    flashing_colors = [ 'yellow','green','red']
    col=flashing_colors[i]
    #将其他两个灯置黑
    for key in flashing_colors:
        if key!=col:
            w.itemconfigure(key, fill='gray')
    #改变画布属性
    w.itemconfigure(col, fill=col)
    i+=1
    if i==3:
        i=0
    window.after(150,flash,i)  #递归刷新

if __name__ == '__main__':

    window = tk.Tk()
    window.title('红绿灯')
    w = tk.Canvas(window, width=300, height=500)
    w.pack()
    #红绿灯的边框
    w.create_rectangle(80,20,200,340,fill="black")
    #create_oval的参数是外切正方形的对角线坐标
    red_rectangle = w.create_oval(100, 40, 180, 120, fill="red", tags=('red'))
    yellow_rectangle = w.create_oval(100, 140, 180, 220, fill="gray", tags=('yellow'))
    green_rectangle = w.create_oval(100, 240, 180, 320, fill="gray", tags=('green'))
    #红绿灯的柱子
    w.create_rectangle(130,340,150,500,fill="white")
    w.bind("<Button-1>", flash)
    window.mainloop()