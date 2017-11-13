# -*- coding: utf-8 -*-
## Author: Jin Feng
## Date: 2017-11-5
## 

from Tkinter import *
import os
import random


number = 0

def display_letter(ls):
    letter = random.choice(ls)
    canvas.delete('text')
    canvas.create_text(590,300,text=letter,font='ComicSansMS -500 bold',fill='blue',tags='text')
    return letter

def display():
    canvas.create_text(590,500,text='此次出错的音节有： ',font='ComicSansMS -50 bold',\
                       fill='blue',tags='text')
        

#read_txt()
#print list_pinyin_txt
windows = Tk()
windows.maxsize(1200,700)
windows.minsize(1200,700)
windows.title("一年级数学练习  Version 1.0.1 ")

frame1 = Frame(windows,relief=GROOVE,borderwidth=10)
frame2 = Frame(windows,borderwidth=5)

canvas = Canvas(frame1,bg='green',width=1180,height=600)
button1 = Button(frame2,height=10,width=20,text='开始',command=display)
button2 = Button(frame2,height=10,width=20,text='结束-显示成绩',command=display)

frame1.pack()
frame2.pack()

canvas.pack()

button1.pack(side=LEFT)
button2.pack(side=RIGHT)


windows.mainloop()
