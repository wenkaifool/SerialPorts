from tkinter import ttk
import tkinter as tk
from CustomizedUI import Adaptive

font = Adaptive.monaco_font
root = tk.Tk()
root.title('Ciao')

frm_status = tk.LabelFrame(root, text='', bg="#292929", fg="#1E90FF")
frm_status.pack()

frm_status_label = tk.Label(frm_status, text="Ready",
                                         bg="#292929", fg="#8DEEEE",
                                         font=font)
# frm_status_label.grid(row=0, column=0, padx=5, pady=5, sticky="wesn")
frm_status_label.pack()
v = tk.IntVar()
r1 = tk.Radiobutton(frm_status, text="同学/同事介绍", variable=v, value=1).pack(anchor="w")
r2 = tk.Radiobutton(frm_status, text="老婆大人介绍", variable=v, value=2).pack(anchor="w")
r3 = tk.Radiobutton(frm_status, text="老师/学长介绍", variable=v, value=3).pack(anchor="w")

root.mainloop()

