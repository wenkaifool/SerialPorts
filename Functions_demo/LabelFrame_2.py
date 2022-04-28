#Import required libraries
from tkinter import *
#Create an instance of tkinter frame
win= Tk()
#Define the geometry of the window
win.geometry("750x250")
#Initialize a LabelFrame Widget
labelframe= LabelFrame(win, text= "Frame 01",width= 600, height= 200, labelanchor= "n", font= ('Helvetica 14 bold'),bd= 5, background="gray71", foreground= "white")
labelframe.pack(ipadx=10, ipady=20, expand= True, fill= BOTH)

#Create a Label inside LabelFrame
Label(labelframe, text= "I am inside a LabelFrame", font=('Helvetica15 bold'), foreground= "black").pack(pady= 20)

win.mainloop()