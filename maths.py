# -*- coding: utf-8 -*-
## Author: Jin Feng
## Date: 2017-11-14
## 

from Tkinter import *
import os
import random
import time

number = 0
list_number = []
list_ques = ['','','','']

class ClickNumber():
    def __init__(self,x1,y1,x2,y2,number):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.number = number

    
def get_ques(maxnum):
    global list_ques
    list_ques[0] = random.choice(['+','-'])
    if list_ques[0] == '+':
        list_ques[1] = random.randint(0,maxnum)
        list_ques[2] = random.randint(0,maxnum-list_ques[1])
        list_ques[3] = list_ques[1]+list_ques[2]
    elif list_ques[0] == '-':
        list_ques[1] = random.randint(1,maxnum)
        list_ques[2] = random.randint(0,list_ques[1])
        list_ques[3] = list_ques[1]-list_ques[2]
    n = random.choice([1,2,3])
    result = list_ques[n]
    list_ques[n] = '□'
    return str(list_ques[1])+str(list_ques[0])+str(list_ques[2])+'='+str(list_ques[3]),result

def start():
    canvas.delete('text')
    canvas.bind('<Button-1>',click)
    string,result = get_ques(10)
    canvas.create_text(590,200,text=string,font='ComicSansMS -270 bold',fill='blue',tags='text')

def display():
    start()
    #    canvas.create_text(590,500,text='此次出错的音节有： ',font='ComicSansMS -50 bold',fill='blue',tags='text')

def click(event):
    x = event.x
    y = event.y
    print x,y
    print click_number(x,y)

def click_number(x,y):
    for xy in list_number:
        if x < xy.x2 and x > xy.x1 and y < xy.y2 and y > xy.y1:
            canvas.create_rectangle(xy.x1,xy.y1,xy.x2,xy.y2,fill='red',tags='text')
            return xy.number

def init(maxnum):
    if maxnum == 10:
        num_width = 110
        canvas.create_line(40,600-40-num_width,1180-40,600-40-num_width,fill='black',width=2,tags='init')
        canvas.create_line(40,600-40,1180-40,600-40,fill='black',width=2,tags='init')
        for n in range(maxnum):
            canvas.create_line(40+n*num_width,600-40-num_width,40+n*num_width,600-40,fill='black',width=2,tags='init')
            canvas.create_text(40+(n+0.5)*num_width,600-40-num_width*0.5,text = n+1,font='ComicSansMS -40 bold',fill='black',tags='init')
            list_number.append(ClickNumber(40+n*num_width,600-40-num_width,40+(n+1)*num_width,600-40,n+1))
            
        canvas.create_line(40+10*num_width,600-40-num_width,40+10*num_width,600-40,fill='black',width=2,tags='init')
        


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

init(10)

windows.mainloop()
