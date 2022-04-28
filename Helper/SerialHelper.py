#! /usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import binascii
import time

class SerialHelper(object):
    def __init__(self, Port="COM1", BaudRate="9600", ByteSize="8", Parity="N", Stopbits="1"):
        self.receive_data = ''
        self.alive = False
        self.l_serial = None
        self.port = Port
        self.baudrate = BaudRate
        self.bytesize = ByteSize
        self.parity = Parity
        self.stopbits = Stopbits
        self.thresholdValue = 64

    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = self.baudrate
        self.l_serial.bytesize = int(self.bytesize)
        self.l_serial.parity = self.parity
        self.l_serial.stopbits = int(self.stopbits)
        self.l_serial.timeout = 2

        try:
            self.l_serial.open()
            if self.l_serial.isOpen():
                self.alive = True
        except:
            print('l_serial.open is failed')
            self.alive = False

        # print('alive:', self.alive)
        # print('l_serial.isOpen:', self.l_serial.isOpen())

    def stop(self):
        self.alive = False
        if self.l_serial.isOpen():
            self.l_serial.close()

    def read(self):
        while self.alive:
            try:
                # 返回接收缓存中的字节数
                number = self.l_serial.inWaiting()
                if number:
                    # binascii.unhexlify(hexstr)： 从十六进制字符串hexstr返回二进制数据
                    self.receive_data += self.l_serial.read(number).replace(binascii.unhexlify("00"), "")

                    if self.thresholdValue <= len(self.receive_data):
                        # print(self.receive_data)
                        self.receive_data = ""
            except Exception as ex:
                print(ex.message)
                pass

    def write(self, data, isHex=False):
        if self.alive:
            if self.l_serial.isOpen():
                if isHex:
                    # 消除数据间隔
                    data.strip()
                    data = data.replace(" ", "").replace("\n", "").replace("\r", "")

                    # 从十六进制字符串hexstr返回二进制数据。
                    # hexstr必须包含偶数个十六进制数字（可以是大写或小写），否则报TypeError。
                    data = binascii.unhexlify(data)
                self.l_serial.write(data)

if __name__ == '__main__':
    import threading

    ser = SerialHelper()
    NEWLINE = False
    i = 1
    ser.start()
    if i == 0:
        writed_data = "123\n"
        encoded_data = writed_data.encode()
        [ser.write(encoded_data, isHex=False) for i in range(1)]
    else:
        writed_data = "123\n45  6 "
        # writed_data = writed_data.encode()
        # str(writed_data, 'utf-8')
        print(type(writed_data))
        if NEWLINE:
            send_data = (writed_data.strip() + "\n").encode("gbk")
            # send_data = str(writed_data.strip() + "\r\n")
        else:
            send_data = writed_data.encode("gbk").strip()
        send_data = send_data.decode()
        [ser.write(send_data, isHex=True) for i in range(1)]

    thread_read = threading.Thread(target=ser.read)
    thread_read.setDaemon(True)
    thread_read.start()


    time.sleep(1)
    ser.stop()


