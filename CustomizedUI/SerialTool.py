#! /usr/bin/env python
# -*- coding: utf-8 -*-

from CustomizedUI import Adaptive
import tkinter as tk
from tkinter import ttk
import webbrowser

# set size and font
size_dict = Adaptive.size_dict
font = Adaptive.monaco_font


class CustomizedSerialToolUI(object):
    def __init__(self, master=None):
        self.frm_left_combobox_serialports = None
        self.menu_buttons = None
        self.button_0x01 = None
        self.title_status = None
        self.title = None
        self.frm_status_label = None
        self.frm_right_clear_btn = None
        self.frm_right_hex_checkbtn = None
        self.receive_hex_cbtn_var = None
        self.frm_right_threshold_entry = None
        self.thresholdStr = None
        self.frm_right_threshold_label = None
        self.frm_right_clear_label = None
        self.frm_right_send_btn = None
        self.frm_right_reset_btn = None
        self.frm_right_reset_hex_checkbtn = None
        self.frm_right_reset_newLine_checkbtn = None
        self.send_hex_cbtn_var = None
        self.new_line_cbtn_var = None
        self.frm_right_reset_label = None
        self.frm_right_receive = None
        self.frm_right_clear = None
        self.frm_right_send = None
        self.frm_right_reset = None
        self.frm_left_combobox_stopbit = None
        self.frm_left_combobox_databit = None
        self.frm_left_combobox_parity = None
        self.frm_left_combobox_baudrate = None
        self.frm_left_btn = None
        self.frm_left_serial_set = None
        self.frm_right = None
        self.frm_left = None
        self.frm_status = None
        self.frm = None

        self.root = master
        self.button_width = 10
        self.create_frame()
        self.thresholdValue = 1

    # 新建窗口，分为上下4个部分，第一部分为标题栏，第二部分为选项栏，第三部分为菜单栏，第四部分为状态栏，下半部分为状态栏
    def create_frame(self):
        self.title = tk.LabelFrame(self.root, text='', bg="#292929", fg="#1E90FF")
        self.frm = tk.LabelFrame(self.root, text='', bg="#292929", fg="#1E90FF")
        self.menu_buttons = tk.LabelFrame(self.root, text='', bg="#292929", fg="#1E90FF")
        self.frm_status = tk.LabelFrame(self.root, text='', bg="#292929", fg="#1E90FF")

        self.title.grid(row=0, column=0, sticky="wesn")
        self.frm.grid(row=1, column=0, sticky="wesn")
        self.menu_buttons.grid(row=2, column=0, sticky="wesn")
        self.frm_status.grid(row=3, column=0, sticky="wesn")

        self.create_title()
        self.create_frm()
        self.create_menu_buttons()
        self.create_frm_status()

    def create_title(self):
        self.title_status = tk.Text(self.title, autoseparators=False, height=1, highlightthickness=0, width=95,
                                     bg="#292929", fg="white", # #008B8B
                                     font=('Monaco', 11, 'bold'))
        self.title_status.pack()
        self.title_status.insert(tk.INSERT, '满洲里国峰电子科技 www.guofengdianzi.com 微信：guofengdianzi 邮箱：techsupport@guofengdianzi.com')

        self.title_status.tag_add("link", '1.10', '1.31')
        self.title_status.tag_config('link', underline=True)

        # 鼠标指向
        self.title_status.tag_bind('link', '<Enter>', self.show_hand_cursor)
        # 鼠标离开
        self.title_status.tag_bind('link', '<Leave>', self.show_xterm_cursor)
        # 左键点击
        self.title_status.tag_bind('link', '<Button-1>', self.title_click)

    # 上半部分窗口分为左右2个部分
    def create_frm(self):
        self.frm_left = tk.LabelFrame(self.frm, text="", bg="#292929", fg="#1E90FF")
        self.frm_right = tk.LabelFrame(self.frm, text="", bg="#292929", fg="#1E90FF")

        self.frm_left.grid(row=0, column=0, padx=5, pady=5, sticky="wesn")
        self.frm_right.grid(row=0, column=1, padx=5, pady=5, sticky="wesn")

        self.create_frm_left()
        self.create_frm_right()

    # 上半部分左边窗口：Listbox显示可用的COM口 + Button按钮点击连接设备
    def create_frm_left(self):
        self.frm_left_serial_set = tk.LabelFrame(self.frm_left, text="串口配置",
                                                 bg="#292929", fg="#E0EEEE",
                                                 labelanchor='n',
                                                 font=('Monaco', 11, 'bold'))
        blank1 = tk.Canvas(self.frm_left, width=5, height=5, bg="#292929")
        blank1.config(highlightthickness=0)
        self.frm_left_reciveset = tk.LabelFrame(self.frm_left, text="接收设置",
                                                bg="#292929", fg="#E0EEEE",
                                                labelanchor='n',
                                                font=('Monaco', 11, 'bold'))
        blank2 = tk.Canvas(self.frm_left, width=5, height=5, bg="#292929")
        blank2.config(highlightthickness=0)
        self.frm_left_sendset = tk.LabelFrame(self.frm_left, text="发送设置",
                                              bg="#292929", fg="#E0EEEE",
                                              labelanchor='n',
                                              font=('Monaco', 11, 'bold'))

        self.frm_left_serial_set.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="wesn")
        blank1.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky="wesn")
        self.frm_left_reciveset.grid(row=2, column=0, padx=5, pady=5, sticky="wesn")
        blank2.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky="wesn")
        self.frm_left_sendset.grid(row=4, column=0, padx=5, pady=5, sticky="wesn")

        self.create_frm_left_serial_set()
        self.create_frm_left_reciveset()
        self.create_frm_left_sendset()

    # 串口配置，比如波特率，奇偶校验等
    def create_frm_left_serial_set(self):
        setting_label_list = ['端口：', "波特率：", "校验位：", "数据位：", "停止位："]
        baudrate_list = ["1200", "2400", "4800", "9600", "14400", "19200", "38400",
                         "43000", "57600", "76800", "115200", "12800"]
        # PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
        parity_list = ["N", "E", "O", "M", "S"]
        bytesize_list = ["5", "6", "7", "8"]
        stopbits_list = ["1", "1.5", "2"]

        for index, item in enumerate(setting_label_list):
            frm_left_label_temp = tk.Label(self.frm_left_serial_set, text=item,
                                           bg="#292929", fg="#E0EEEE",
                                           font=('Monaco', 10))
            frm_left_label_temp.grid(row=index, column=0, padx=1, pady=2, sticky="e")

        self.frm_left_combobox_baudrate = ttk.Combobox(self.frm_left_serial_set,
                                                       width=15,
                                                       values=baudrate_list)

        self.frm_left_combobox_parity = ttk.Combobox(self.frm_left_serial_set,
                                                     width=15,
                                                     values=parity_list)

        self.frm_left_combobox_databit = ttk.Combobox(self.frm_left_serial_set,
                                                      width=15,
                                                      values=bytesize_list)

        self.frm_left_combobox_stopbit = ttk.Combobox(self.frm_left_serial_set,
                                                      width=15,
                                                      values=stopbits_list)

        self.frm_left_LED = tk.Canvas(self.frm_left_serial_set, width=5, height=5, bg="#292929")
        self.frm_left_LED.config(highlightthickness=0)
        self.frm_left_LEDstate = self.frm_left_LED.create_oval(15, 5, 35, 25, outline='white', stipple='question',
                                                               fill="red", tags=('red'))

        self.frm_left_btn = tk.Button(self.frm_left_serial_set, text="Open",
                                      width=10,
                                      activebackground="#00B2EE",
                                      activeforeground="#E0EEEE",
                                      bg="#008B8B", fg="#FFFFFF",
                                      font=font,
                                      command=self.toggle)

        # self.frm_left_combobox_serialports.grid(row=0, column=1, padx=2, pady=2, sticky="e")
        self.frm_left_combobox_baudrate.grid(row=1, column=1, padx=2, pady=2, sticky="e")
        self.frm_left_combobox_parity.grid(row=2, column=1, padx=2, pady=2, sticky="e")
        self.frm_left_combobox_databit.grid(row=3, column=1, padx=2, pady=2, sticky="e")
        self.frm_left_combobox_stopbit.grid(row=4, column=1, padx=2, pady=2, sticky="e")
        self.frm_left_LED.grid(row=5, column=0, padx=2, pady=2, sticky="wesn")
        self.frm_left_btn.grid(row=5, column=1, padx=2, pady=2, sticky="wesn")

        self.frm_left_combobox_baudrate.current(3)
        self.frm_left_combobox_parity.current(0)
        self.frm_left_combobox_databit.current(3)
        self.frm_left_combobox_stopbit.current(0)

    def create_frm_left_reciveset(self):
        self.receive_hex_cbtn_var = tk.IntVar()
        self.frm_right_hex_checkbtn = tk.Checkbutton(self.frm_left_reciveset,
                                                     text="十六进制显示",
                                                     variable=self.receive_hex_cbtn_var,
                                                     bg="#292929", fg="#FFFFFF",
                                                     activebackground="#292929",
                                                     relief="flat",
                                                     selectcolor="#292929",
                                                     font=('Monaco', 10))
        self.frm_right_hex_checkbtn.grid(row=0, column=0, padx=2, pady=2, sticky="w")

        self.frm_right_clear_btn = tk.Button(self.frm_left_reciveset, text="清空接收显示",
                                             activebackground="#00B2EE",
                                             activeforeground="#E0EEEE",
                                             bg="#008B8B", fg="#FFFFFF",
                                             width=20,
                                             font=('Monaco', 10),
                                             command=self.clear)
        self.frm_right_clear_btn.grid(row=1, column=0, padx=7, pady=2, sticky="w")

    def create_frm_left_sendset(self):
        self.send_hex_cbtn_var = tk.IntVar()
        self.frm_right_reset_hex_checkbtn = tk.Checkbutton(self.frm_left_sendset,
                                                           text="十六进制发送",
                                                           variable=self.send_hex_cbtn_var,
                                                           bg="#292929", fg="#FFFFFF",
                                                           activebackground="#292929",
                                                           selectcolor="#292929",
                                                           font=('Monaco', 10))
        self.frm_right_reset_hex_checkbtn.grid(row=0, column=0, padx=2, pady=2, sticky="w")

        self.new_line_cbtn_var = tk.IntVar()
        self.frm_right_reset_newLine_checkbtn = tk.Checkbutton(self.frm_left_sendset,
                                                               text="换行",
                                                               variable=self.new_line_cbtn_var,
                                                               bg="#292929", fg="#FFFFFF",
                                                               activebackground="#292929",
                                                               selectcolor="#292929",
                                                               font=('Monaco', 10))
        self.frm_right_reset_newLine_checkbtn.grid(row=1, column=0, padx=2, pady=2, sticky="w")

        self.frm_right_reset_btn = tk.Button(self.frm_left_sendset, text="清空发送数据",
                                             activebackground="#00B2EE",
                                             activeforeground="#E0EEEE",
                                             bg="#008B8B", fg="#FFFFFF",
                                             width=20,
                                             font=('Monaco', 10),
                                             command=self.reset)
        self.frm_right_reset_btn.grid(row=2, column=0, padx=7, pady=2, sticky="w")

        self.frm_right_send_btn = tk.Button(self.frm_left_sendset, text="发送",
                                            activebackground="#00B2EE",
                                            activeforeground="#E0EEEE",
                                            bg="#008B8B", fg="#FFFFFF",
                                            width=20,
                                            font=('Monaco', 10, 'bold'),
                                            command=self.send)
        self.frm_right_send_btn.grid(row=3, column=0, padx=7, pady=2, sticky="w")

    def create_frm_right(self):
        self.frm_right_reset = tk.Label(self.frm_right, text='', bg="#292929", fg="#1E90FF")
        self.frm_right_send = tk.Text(self.frm_right,
                                      width=95, height=size_dict["send_text_height"],
                                      bg="#292929", fg="#1E90FF",
                                      font=("Monaco", 10))
        self.frm_right_clear = tk.LabelFrame(self.frm_right, text="",
                                             bg="#292929", fg="#1E90FF")
        self.frm_right_receive = tk.Text(self.frm_right,
                                         width=95, height=size_dict["receive_text_height"],
                                         bg="#292929", fg="#1E90FF",
                                         font=("Monaco", 10))

        self.frm_right_reset.grid(row=2, column=0, padx=1, sticky="wesn")
        self.frm_right_send.grid(row=3, column=0, padx=1, sticky="wesn")
        self.frm_right_clear.grid(row=0, column=0, padx=1, sticky="wesn")
        self.frm_right_receive.grid(row=1, column=0, padx=1, sticky="wesn")

        self.frm_right_receive.tag_config("green", foreground="#228B22")
        # self.frm_right_send.tag_config("green", foreground="#228B22")

        self.create_frm_right_reset()
        self.create_frm_right_clear()

    # Label显示和重置按钮和发送按钮
    def create_frm_right_reset(self):
        self.frm_right_reset_label = tk.Label(self.frm_right_reset,
                                              text="发送数据显示",
                                              bg="#292929", fg="#E0EEEE",
                                              font=("Monaco", 10, 'bold'))
        self.frm_right_reset_label.pack()

    def create_frm_right_clear(self):
        self.frm_right_clear_label = tk.Label(self.frm_right_clear,
                                              text="接收数据显示",
                                              bg="#292929", fg="#E0EEEE",
                                              font=("Monaco", 10, 'bold'))
        self.frm_right_clear_label.pack()

        self.frm_right_threshold_label = tk.Label(self.frm_right_clear,
                                                  text="Threshold:",
                                                  bg="#292929", fg="#E0EEEE",
                                                  font=font)
        self.thresholdStr = tk.StringVar()
        self.frm_right_threshold_entry = tk.Entry(self.frm_right_clear,
                                                  textvariable=self.thresholdStr,
                                                  width=6,
                                                  bg="#292929", fg="#E0EEEE",
                                                  font=font)
        # self.frm_right_threshold_label.grid(row=0, column=1, padx=5, pady=5, sticky="wesn")
        # self.frm_right_threshold_entry.grid(row=0, column=2, padx=5, pady=5, sticky="wesn")

        self.thresholdStr.set(1)
        self.thresholdStr.trace('w', self.getthresholdvalue)

    # 第三部分为菜单栏
    def create_menu_buttons(self):

        self.button_0x01 = tk.Button(self.menu_buttons, text="参数01",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn01)
        self.button_0x02 = tk.Button(self.menu_buttons, text="参数02",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn02)
        self.button_0x03 = tk.Button(self.menu_buttons, text="参数03",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn03)
        self.button_0x04 = tk.Button(self.menu_buttons, text="参数04",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn04)
        self.button_0x05 = tk.Button(self.menu_buttons, text="参数05",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width = self.button_width,
                                     font=font,
                                     command=self.Hex_Btn05)
        self.button_0x06 = tk.Button(self.menu_buttons, text="参数06",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn06)
        self.button_0x07 = tk.Button(self.menu_buttons, text="参数07",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn07)
        self.button_0x08 = tk.Button(self.menu_buttons, text="参数08",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn08)
        self.button_0x09 = tk.Button(self.menu_buttons, text="参数09",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn09)
        self.button_0x0A = tk.Button(self.menu_buttons, text="参数10",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn0A)

        self.button_0x0B = tk.Button(self.menu_buttons, text="参数11",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn0B)

        self.button_0x0C = tk.Button(self.menu_buttons, text="参数12",
                                     activebackground="#00B2EE",
                                     activeforeground="#E0EEEE",
                                     bg="#008B8B", fg="#FFFFFF",
                                     width=self.button_width,
                                     font=font,
                                     command=self.Hex_Btn0C)

        self.button_0x01.grid(row=0, column=0, padx=32, pady=5, sticky="wesn")
        self.button_0x02.grid(row=0, column=1, padx=26, pady=5, sticky="wesn")
        self.button_0x03.grid(row=0, column=2, padx=26, pady=5, sticky="wesn")
        self.button_0x04.grid(row=0, column=3, padx=26, pady=5, sticky="wesn")
        self.button_0x05.grid(row=0, column=4, padx=26, pady=5, sticky="wesn")
        self.button_0x06.grid(row=0, column=5, padx=26, pady=5, sticky="wesn")
        self.button_0x07.grid(row=1, column=0, padx=32, pady=5, sticky="wesn")
        self.button_0x08.grid(row=1, column=1, padx=26, pady=5, sticky="wesn")
        self.button_0x09.grid(row=1, column=2, padx=26, pady=5, sticky="wesn")
        self.button_0x0A.grid(row=1, column=3, padx=26, pady=5, sticky="wesn")
        self.button_0x0B.grid(row=1, column=4, padx=26, pady=5, sticky="wesn")
        self.button_0x0C.grid(row=1, column=5, padx=26, pady=5, sticky="wesn")


    # 第四部分状态栏窗口
    def create_frm_status(self):
        self.frm_status_label = tk.Label(self.frm_status, text="Ready",
                                         bg="#292929", fg="#8DEEEE",
                                         font=font)
        self.frm_status_label.grid(row=0, column=0, padx=5, pady=5, sticky="wesn")

    def toggle(self):
        pass

    def Hex_Btn01(self):
        pass
    def Hex_Btn02(self):
        pass
    def Hex_Btn03(self):
        pass
    def Hex_Btn04(self):
        pass
    def Hex_Btn05(self):
        pass
    def Hex_Btn06(self):
        pass
    def Hex_Btn07(self):
        pass
    def Hex_Btn08(self):
        pass
    def Hex_Btn09(self):
        pass
    def Hex_Btn0A(self):
        pass
    def Hex_Btn0B(self):
        pass
    def Hex_Btn0C(self):
        pass

    def open(self, event):
        pass

    def reset(self):
        self.frm_right_send.delete("0.0", "end")

    def send(self):
        pass

    def clear(self):
        self.frm_right_receive.delete("0.0", "end")

    def getthresholdvalue(self, *args):
        try:
            self.thresholdValue = int(self.thresholdStr.get())
        except:
            pass

    # 绑定事件一定要传入event
    def show_hand_cursor(self, event):
        self.title_status.config(cursor='trek')

    def show_xterm_cursor(self, event):
        self.title_status.config(cursor='xterm')

    def title_click(self,event):
        webbrowser.open('www.guofengdianzi.com')

if __name__ == '__main__':
    root = tk.Tk()
    combostyle = ttk.Style()
    combostyle.theme_create("combostyle", parent="alt",
                            settings={
                                "TCombobox":
                                    {
                                        "configure":
                                            {
                                                "selectbackground": "#292929",
                                                "fieldbackground": "#292929",
                                                "background": "#292929",
                                                "foreground": "#FFFFFF"
                                            }
                                    }
                            })
    combostyle.theme_use('combostyle')
    root.title("Serial Tool")
    CustomizedSerialToolUI(master=root)
    root.resizable(False, False)
    root.mainloop()
