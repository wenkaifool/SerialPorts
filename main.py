#! /usr/bin/env python
# -*- coding: utf-8 -*-

import binascii
import datetime
import platform
import tkinter as tk
import tkinter.ttk as ttk
from CustomizedUI import SerialTool
import threading
from Helper import SerialHelper

if platform.system() == "Windows":
    from serial.tools import list_ports


class CustomizedSerialToolUI(SerialTool.CustomizedSerialToolUI):
    def __init__(self, master=None):
        super(CustomizedSerialToolUI, self).__init__()

        self.list_box_serial = list()
        self.comstate = ['No detected COM']
        self.ser = None
        self.receive_count = 0
        self.receive_data = ""
        self.find_all_serial()
        self.select_detected_serialport()

        self.port = None
        self.thread_findserial = None
        self.currentStrCom = None
        self.stopbit = None
        self.databit = None
        self.parity = None
        self.baudrate = None
        self.thread_read = None
        self.sendIStext = True

    def __del__(self):
        pass

    # 获取到串口列表
    def find_all_serial(self):
        if platform.system() == "Windows":
            try:
                self.list_box_serial = list()
                temp = list(list_ports.comports())  # 返回当前windows中的端口列表
                # print(temp)
                for i in range(len(temp)):
                    self.list_box_serial.append(temp[i][0])

                # class threading.Timer(interval, function, args=[], kwargs={})
                # 创建一个timer，在interval秒过去之后，它将以参数args和关键字参数kwargs运行function 。
                # 如果某个子线程的daemon属性为False，主线程结束时会检测该子线程是否结束，如果该子线程还在运行，则主线程会等待它完成后再退出；
                # 如果某个子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检查而直接退出，同时所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成。
                # 属性daemon的值默认为False，如果需要修改，必须在调用start()方法启动线程之前进行设置。
                self.thread_findserial = threading.Timer(1, self.find_all_serial)
                self.thread_findserial.setDaemon(True)
                self.thread_findserial.start()

            except:
                pass
        else:
            print('The operation system is not windows!')

    def select_detected_serialport(self):
        if len(self.list_box_serial) == 0:
            self.frm_left_combobox_serialports = ttk.Combobox(self.frm_left_serial_set,
                                                              width=15,
                                                              values=self.comstate)
            self.frm_left_combobox_serialports.current(0)
            self.frm_left_combobox_serialports.grid(row=0, column=1, padx=2, pady=2, sticky="e")
        else:
            self.frm_left_combobox_serialports = ttk.Combobox(self.frm_left_serial_set,
                                                              width=15,
                                                              values=self.list_box_serial)
            self.frm_left_combobox_serialports.grid(row=0, column=1, padx=2, pady=2, sticky="e")
            self.frm_left_combobox_serialports.current(0)

    # 打开关闭串口
    def toggle(self):
        if self.frm_left_btn["text"] == "Open":
            try:
                # self.currentStrCom = self.frm_left_listbox.get(self.frm_left_listbox.curselection())
                self.currentStrCom = self.frm_left_combobox_serialports.get()
                if platform.system() == "Windows":
                    self.port = self.currentStrCom.split(":")[0]
                    print('Selected current port:'+self.port)

                # 波特率；奇偶；数据位；停止位设置
                self.baudrate = self.frm_left_combobox_baudrate.get()
                self.parity = self.frm_left_combobox_parity.get()
                self.databit = self.frm_left_combobox_databit.get()
                self.stopbit = self.frm_left_combobox_stopbit.get()
                self.ser = SerialHelper.SerialHelper(Port=self.port,
                                                     BaudRate=self.baudrate,
                                                     ByteSize=self.databit,
                                                     Parity=self.parity,
                                                     Stopbits=self.stopbit)

                self.ser.start()
                if self.ser.alive:
                    self.frm_status_label["text"] = "Open [{0}] Successful!".format(self.currentStrCom)
                    self.frm_status_label["fg"] = "#66CD00"
                    self.frm_left_btn["text"] = "Close"
                    self.frm_left_btn["bg"] = "#F08080"

                    self.frm_left_LED.itemconfigure(self.frm_left_LEDstate, fill='green')

                    self.thread_read = threading.Thread(target=self.serialread)
                    self.thread_read.setDaemon(True)
                    self.thread_read.start()

            except Exception:
                try:
                    self.frm_status_label['text'] = 'Open [{0}] Failed. Try to select the desired serial port above.'.format(self.currentStrCom)
                    self.frm_status_label["fg"] = "#DC143C"
                except:
                    pass

        elif self.frm_left_btn["text"] == "Close":
            try:
                self.ser.stop()
                self.receive_count = 0
            except:
                pass
            self.frm_left_btn["text"] = "Open"
            self.frm_left_btn["bg"] = "#008B8B"
            self.frm_status_label["text"] = "Close Serial Successful!"
            self.frm_status_label["fg"] = "#8DEEEE"
            self.frm_left_LED.itemconfigure(self.frm_left_LEDstate, fill='red')
        else:
            self.frm_left_LED.itemconfigure(self.frm_left_LEDstate, fill='yellow')

    def open(self, event):
        self.toggle()

    def clear(self):
        self.frm_right_receive.delete("0.0", "end")
        self.receive_count = 0

    # 向已打开的串口发送数据: 如果为Hex发送，示例："31 32 33" [即为字符串 "123"]
    def send(self):
        if self.ser:
            try:
                # writed_data = "123\n"
                # encoded_data = writed_data.encode()
                # [self.ser.write(encoded_data, isHex=False) for i in range(10)]

                # 发送新行
                if self.new_line_cbtn_var.get() == 0:
                    # strip()移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
                    # tkinter.Text.get('1.2', END)这个函数，其中第一个参数‘1.2’是指从第一行第2列进行读取
                    # （‘1.0’表示第一行第一列，即第一个字符），第二个End表示最后一个字符，输出框便如左图所截取。
                    send_data = self.frm_right_send.get("0.0", "end").encode("gbk").strip()
                    # send_data = str(self.frm_right_send.get("0.0", "end").encode("gbk")).strip()
                else:
                    send_data = (self.frm_right_send.get("0.0", "end").strip() + "\r\n").encode("gbk")
                    # send_data = str(self.frm_right_send.get("0.0", "end")).strip() + "\r\n"
                # print('getted data:', send_data) # 1212-->b'1212\n'
                # print('type:', type(send_data))

                # 是否十六进制发送
                if self.send_hex_cbtn_var.get() == 1:
                    send_data = send_data.decode()
                    # print('step2 sent_data:', send_data, 'type:', type(send_data))
                    self.ser.write(send_data, isHex=True)
                else:
                    self.ser.write(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")

    def Hex_Btn01(self):
        if self.ser:
            try:
                send_data = '01'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")

    def Hex_Btn02(self):
        if self.ser:
            try:
                send_data = '02'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")
    def Hex_Btn03(self):
        if self.ser:
            try:
                send_data = '03'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")
    def Hex_Btn04(self):
        if self.ser:
            try:
                send_data = '04'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")
    def Hex_Btn05(self):
        if self.ser:
            try:
                send_data = '05'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")
    def Hex_Btn06(self):
        if self.ser:
            try:
                send_data = '06'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")
    def Hex_Btn07(self):
        if self.ser:
            try:
                send_data = '07'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")
    def Hex_Btn08(self):
        if self.ser:
            try:
                send_data = '08'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")
    def Hex_Btn09(self):
        if self.ser:
            try:
                send_data = '09'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")
    def Hex_Btn0A(self):
        if self.ser:
            try:
                send_data = '10'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")

    def Hex_Btn0B(self):
        if self.ser:
            try:
                send_data = '11'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")

    def Hex_Btn0C(self):
        if self.ser:
            try:
                send_data = '12'
                self.ser.write(send_data, isHex=True)
                self.frm_status_label["text"] = "Your command [{0}] is sent out".format(send_data)
            except Exception as ex:
                self.frm_right_receive.insert("end", str(ex) + "\n")

    # 线程读取串口发送的数据
    def serialread(self):
        while self.ser.alive:
            try:
                n = self.ser.l_serial.inWaiting()
                # print('可接受的字节数:' + str(n))
                if True:
                    self.receive_data = self.ser.l_serial.readline()
                    # self.receive_data += self.ser.l_serial.read(2).replace(binascii.unhexlify("00"), "")
                    print('self.receive_data:', self.receive_data, 'type:', type(self.receive_data))
                    if self.thresholdValue <= len(self.receive_data):
                        self.receive_count += 1
                        print('self.receive_count:', self.receive_count)
                        # 接收显示是否为Hex
                        if self.receive_hex_cbtn_var.get() == 1:
                            if self.sendIStext:
                                self.receive_data = str(binascii.b2a_hex(self.receive_data))[2:-1]
                                newdata_list = []
                                for index, value in enumerate(self.receive_data):
                                    if index % 2 == 0 and index != 0:
                                        newdata_list.append(' ')
                                    newdata_list.append(value)

                                newdata_list = [str(i) for i in newdata_list]
                                self.receive_data = ''.join(newdata_list)
                                print(self.receive_data)
                                # self.receive_data = self.space_b2a_hex(self.receive_data)
                            self.frm_right_receive.insert("end", "[" + str(datetime.datetime.now()) + " - "
                                                          + str(self.receive_count) + "]:\n", "red")
                            self.frm_right_receive.insert("end", self.receive_data + "\n")
                            self.frm_right_receive.see("end")
                        else:
                            self.frm_right_receive.insert("end", "[" + str(datetime.datetime.now()) + " - "
                                                          + str(self.receive_count) + "]:\n", "red")

                            # self.frm_right_receive.insert("end", self.receive_data + "\n")
                            # 返回二进制数据的十六进制表示
                            # mystr=int(binascii.b2a_hex(self.receive_data),16)

                            astr = ''.join([chr(b) for b in self.receive_data])
                            self.frm_right_receive.insert("end", astr + "\n")
                            self.frm_right_receive.see("end")
                        self.receive_data = ""
                else:
                    self.frm_right_receive.insert("end", "未接收到数据\n")


            except Exception:
                print('here is Exception')
                self.receive_data = ""

    # 格式化接收到的数据字符串, 示例：123 --> 31 32 33
    def space_b2a_hex(self, data):

        new_data_list = list()
        new_data = ""

        hex_data = binascii.b2a_hex(data)
        temp_data = ""
        for index,value in enumerate(hex_data):
            temp_data += value
            if len(temp_data) == 2:
                new_data_list.append(temp_data)
                temp_data = ""
        for index,value in enumerate(new_data_list):
            if index%25 == 0 and index != 0:
                new_data += "\n"
            new_data += value
            new_data += " "

        return new_data

if __name__ == '__main__':
    window_root = tk.Tk()
    window_root.title("Serial Tool UI")

    customized_style = ttk.Style()

    # 如果给出了 parent，则新主题将从父主题继承样式、元素和布局。
    # 若给出了 settings ，则语法应与 theme_settings() 的相同。
    customized_style.theme_create('CustomizedStyle', parent=None,
                                  settings={'TCombobox': {'configure': {
                                      "selectbackground": "#292929",
                                      "fieldbackground": "#292929",
                                      "background": "#292929",
                                      "foreground": "#FFFFFF"
                                  }}})
    customized_style.theme_use('CustomizedStyle')
    CustomizedSerialToolUI(master=window_root)
    window_root.resizable(False, False)
    window_root.mainloop()
