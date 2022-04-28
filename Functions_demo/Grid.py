from tkinter import (Tk, Button)
from tkinter.constants import RIGHT, LEFT, X, Y, BOTH

# Grid: https://blog.csdn.net/weixin_43708622/article/details/107134216
# pack、grid 和 place 均用于管理同在一个父组件下的所有组件的布局，其中：
# pack 是按添加顺序排列组件
# grid 是按行/列形式排列组件
# place 则允许程序员指定组件的大小和位置

# column
# row
# columnspan
# rowspan
# ipadx
# ipady
# padx
# pady
# sticky
# sticky: sticky类似于pack的anchor，决定控件在cell中锚点，
#         也就是控件在cell中的起始位置，可设置的值为’n’, ‘ne’, ‘e’, ‘se’, ‘s’, ‘sw’, ‘w’, ‘nw’;
#         ‘e’、‘w’、‘s’、'n’分别表示东西南北。

main_win = Tk()
main_win.title('渔道的pack布局')
width = 300
height = 300
main_win.geometry(f'{width}x{height}')

selection_list = ['default', 'column', 'row', 'columnspan', 'rowspan', 'ipadx', 'ipady', 'padx', 'pady', 'sticky']

apple_color = 'Crimson'
banana_color = 'Yellow'
orange_color = 'Orange'
grape_color = 'Purple'

fruit = {'apple':'Crimson', 'banana':'Yellow', 'orange':'Orange', 'grape':'Purple'}

def selection_demo(demo):

    if demo == 'default':
        for k,v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid()
    # 结论：可以看出4个按钮默认分布在第0列(column属性)，然后依次分布在第0-3行(row属性)，
    # 列间隔(columnspan)为1，行间隔(rowspan)为1，
    # sticky属性相当于pack的anchor属性但是不完全相同
    elif demo == 'column':
        i = 0
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid(column=i)
            i += 1
    elif demo == 'row':
        i = 0
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid(row=0, column=i)
            i += 1
    elif demo == 'columnspan':
        i = 0
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid(column=i, columnspan=3)
            i += 1
    elif demo == 'rowspan':
        i = 0
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid(column=i, rowspan=3)
            i += 1
    elif demo == 'ipadx': # 水平方向内边距
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid(ipadx=20)
            print(bt.grid_info())
    elif demo == 'ipady': # 垂直方向内边距
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid()
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid(ipady=20)
            print(bt.grid_info())
    elif demo == 'padx':
        i = 1
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            if i % 2 == 0:
                bt.grid(padx=20, column=1)
            else:
                bt.grid(padx=20)
            i += 1
            print(bt.grid_info())
    elif demo == 'pady':
        i = 1
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            if i % 2 == 0:
                bt.grid(pady=20, column=1)
            else:
                bt.grid(pady=20)
            i += 1
            print(bt.grid_info())
    elif demo == 'sticky':
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid()
            print(bt.grid_info())

        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid(sticky='nw')
            print(bt.grid_info())
        for k, v in fruit.items():
            bt = Button(main_win, text=k, fg='black', bg=v)
            bt.grid(sticky='se')

if __name__ == '__main__':
    selection_demo(selection_list[-1])
    main_win.mainloop()