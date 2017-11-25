# -*- coding: utf-8 -*-
## Author: Jin Feng
## Date: 2017-11-14
## 

from Tkinter import *
import os
import random
import time
import codecs

number = 0
list_number = []
list_question = ['','','','']
list_result = [-1]

class ClickNumber():
    def __init__(self,x1,y1,x2,y2,number):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.number = number

    
def get_question(maxnum):
    global list_question
    global list_result
    global model_list
    canvas.delete('text')
    list_question[0] = random.choice(['+','-'])
    if list_question[0] == '+':
        list_question[1] = random.randint(0,maxnum)
        list_question[2] = random.randint(0,maxnum-list_question[1])
        list_question[3] = list_question[1]+list_question[2]
    elif list_question[0] == '-':
        list_question[1] = random.randint(1,maxnum)
        list_question[2] = random.randint(0,list_question[1])
        list_question[3] = list_question[1]-list_question[2]
    n = random.choice([1,2,3])
    result = list_question[n]
    list_result[0] = result
    list_question[n] = '□'
    string = str(list_question[1])+str(list_question[0])+str(list_question[2])+'='+str(list_question[3])
    canvas.bind('<Button-1>',click)
    canvas.create_text(590,200,text=string,font='ComicSansMS -270 bold',fill='blue',tags='text')

def start():
    get_question(10)
    init(20)
    button1.configure(text='下一题',command=nextquestion)
    R1.configure(state = 'disabled')
    R2.configure(state = 'disabled')
    R3.configure(state = 'disabled')

def nextquestion():
    global list_result
    get_question(10)
    
def display():
    canvas.delete('text')
    canvas.delete('init')
    button1.configure(text='开始',command=start)
    R1.configure(state = 'normal')
    R2.configure(state = 'normal')
    R3.configure(state = 'normal')

def click(event):
    x = event.x
    y = event.y
    for xy in list_number:
        if x < xy.x2 and x > xy.x1 and y < xy.y2 and y > xy.y1:
            canvas.unbind('<Button-1>')
            canvas.create_rectangle(xy.x1,xy.y1,xy.x2,xy.y2,fill='red',tags='text')
            if xy.number == list_result[0]:
                canvas.create_text(700,400,text='正确',font='ComicSansMS -40 bold',fill='red',tags='text')
            else:
                canvas.create_text(700,400,text='错误，正确答案应为'+str(list_result[0]),font='ComicSansMS -40 bold',fill='red',tags='text')
            print xy.number,list_result[0]

def init(maxnum):
    num_width = 50
    canvas.create_line(65,580-45-num_width,1180-65,580-45-num_width,fill='black',width=2,tags='init')
    canvas.create_line(65,580-45,1180-65,580-45,fill='black',width=2,tags='init')
    for n in range(maxnum+1):
        canvas.create_line(65+n*num_width,580-45-num_width,65+n*num_width,580-45,fill='black',width=2,tags='init')
        canvas.create_text(65+(n+0.5)*num_width,580-45-num_width*0.5,text = n,font='ComicSansMS -40 bold',fill='black',tags='init')
        list_number.append(ClickNumber(65+n*num_width,580-45-num_width,65+(n+1)*num_width,580-45,n))
        
    canvas.create_line(65+(maxnum+1)*num_width,580-45-num_width,65+(maxnum+1)*num_width,580-45,fill='black',width=2,tags='init')
    

windows = Tk()
windows.maxsize(1200,700)
windows.minsize(1200,700)
windows.title("一年级数学练习  Version 1.0.3 ")

frame = Frame(windows,relief=GROOVE,borderwidth=10)
canvas = Canvas(frame,bg='green',width=1180,height=580)
model_list = StringVar()
model_list.set(1)
button1 = Button(windows,height=3,width=15,font='ComicSansMS -20 bold',text='开始',command=start)
button2 = Button(windows,height=3,width=15,font='ComicSansMS -20 bold',text='结束-显示成绩',command=display)
R1 = Radiobutton(windows,width=12,indicatoron = False ,text="10以内加减", variable=model_list, value=1)  
R2 = Radiobutton(windows,width=12,indicatoron = False ,text="20以内不进位", variable=model_list, value=2)  
R3 = Radiobutton(windows,width=12,indicatoron = False ,text="20以内进位", variable=model_list, value=3)  
 
frame.grid(row=0,column=0,columnspan=9,rowspan=6)
canvas.grid(row=0,column=0,columnspan=9,rowspan=6)
R1.grid(row=6,column=2)
R2.grid(row=7,column=2)
R3.grid(row=8,column=2)
button1.grid(row=6,column=4,rowspan=3)
button2.grid(row=6,column=6,rowspan=3)




windows.mainloop()
