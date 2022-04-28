import tkinter as tk

# pack、grid 和 place 均用于管理同在一个父组件下的所有组件的布局，其中：
# pack 是按添加顺序排列组件
# grid 是按行/列形式排列组件
# place 则允许程序员指定组件的大小和位置

root = tk.Tk()
# fill 选项是告诉窗口管理器该组件将填充整个分配给它的空间，"both" 表示同时横向和纵向扩展，"x" 表示横向，"y" 表示纵向
# expand 选项是告诉窗口管理器将父组件的额外空间也填满。
listbox = tk.Listbox(root)

# Pack: https://www.jianshu.com/p/3164c90f17bd
# expand --- 1. 指定是否填充父组件的额外空间 2. 默认值是 False
# fill	 --- 1. 指定填充 pack 分配的空间
#            2. 默认值是 NONE，表示保持子组件的原始尺寸
#            3. 还可以使用的值有："x"（水平填充），"y"（垂直填充）和 "both"（水平和垂直填充）
listbox.pack(fill="both", expand=False)

for i in range(10):
    listbox.insert("end", str(i))


root.mainloop()