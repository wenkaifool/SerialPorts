import tkinter as tk

master = tk.Tk()
# https://blog.csdn.net/qq_41556318/article/details/85108316
# 默认情况下，LabelFrame 会在其子组件的周围绘制一个边框以及一个标题
# LabelFrame(master=None, **options) (class)
# master -- 父组件
# **options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：
# padx	1. 指定 FrameLabel 水平方向上的额外间距（内容和边框间） 2. 默认值是 0
# pady	1. 指定 FrameLabel 垂直方向上的额外间距（内容和边框间） 2. 默认值是 0
# text	1. 指定 LabelFrame 显示的文本 2. 文本可以包含换行符

group = tk.LabelFrame(master, text="你从哪里得知CSDN？", padx=10, pady=10)
group.pack(padx=10, pady=10) # 边框相对于参考坐标系的位置

group_left = tk.LabelFrame(group, text='left', bg="#292929", fg="#1E90FF")
group_left.grid(row=0, column=0, padx=5, pady=5, sticky="wesn")
group_right = tk.LabelFrame(group, text='right', bg="#292929", fg="#1E90FF")
group_right.grid(row=0, column=1, padx=5, pady=5, sticky="wesn")

v = tk.IntVar()
r1 = tk.Radiobutton(group_left, text="同学/同事介绍", variable=v, value=1).pack(anchor="w")
r2 = tk.Radiobutton(group_left, text="老婆大人介绍", variable=v, value=2).pack(anchor="w")
r3 = tk.Radiobutton(group_left, text="老师/学长介绍", variable=v, value=3).pack(anchor="w")

r4 = tk.Radiobutton(group_right, text="同学/同事介绍", variable=v, value=1).pack(anchor="w")
r5 = tk.Radiobutton(group_right, text="老婆大人介绍", variable=v, value=2).pack(anchor="w")
r6 = tk.Radiobutton(group_right, text="老师/学长介绍", variable=v, value=3).pack(anchor="w")

frm = tk.LabelFrame(master, text="Hello", bg="#292929", fg="#1E90FF")
frm.pack()

master.mainloop()