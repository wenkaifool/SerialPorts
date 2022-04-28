#! /usr/bin/env python
# -*- coding: utf-8 -*-

import platform

g_systemName = platform.system()
# print(g_systemName)
g_systemInfo = platform.platform()
# print(g_systemInfo[:10])
g_pyVersion = platform.python_version()
# print(g_pyVersion)
size_dict = dict()

if g_systemName == "Linux":
    pass
else:
    if g_systemInfo[:10]== "Windows-10":
        size_dict = {
                        "list_box_height": 12,
                        "send_text_height": 12,
                        "receive_text_height": 14,
                        "reset_label_width": 7,
                        "clear_label_width": 5
                     }
    elif g_systemInfo[:9]== "Windows-8":
        size_dict = {
                        "list_box_height": 14,
                        "send_text_height": 6,
                        "receive_text_height": 18,
                        "reset_label_width": 7,
                        "clear_label_width": 5
                     }

    elif g_systemInfo[:9]== "Windows-7":
        size_dict = {
                        "list_box_height": 13,
                        "send_text_height": 12,
                        "receive_text_height": 15,
                        "reset_label_width": 7,
                        "clear_label_width": 5
                     }

    elif g_systemInfo[:10]== "Windows-XP":
        size_dict = {
                        "list_box_height": 20,
                        "send_text_height": 12,
                        "receive_text_height": 22,
                        "reset_label_width": 7,
                        "clear_label_width": 5
                     }

# font
monaco_font = ('Monaco', 12)
# print(monaco_font)
# print(size_dict)
# print("Data Send" + " "*size_dict["reset_label_width"])
