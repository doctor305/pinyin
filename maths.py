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
list_question = ['','','','']
list_result = [-1]
list_error = []
time_start = 0
time_end = 0
number_question = 0
number_error = 0
tag_done = 0
n = 0

class ClickNumber():
    def __init__(self,x1,y1,x2,y2,number):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.number = number

    
def get_question():
    global list_question
    global list_result
    global model_list
    global tag_start
    global tag_done
    canvas.delete('text')
    list_question[0] = random.choice(['+','-'])
    if list_question[0] == '+':
        if model_list.get()=='1':
            list_question[1] = random.randint(0,10)
            list_question[2] = random.randint(0,10-list_question[1])
            list_question[3] = list_question[1]+list_question[2]
        elif model_list.get()=='2':
            list_question[1] = random.randint(10,20)
            list_question[2] = random.randint(0,20-list_question[1])
            list_question[3] = list_question[1]+list_question[2]
        elif model_list.get()=='3':
            list_question[1] = random.randint(0,20)
            list_question[2] = random.randint(0,20-list_question[1])
            list_question[3] = list_question[1]+list_question[2]
    elif list_question[0] == '-':
        if model_list.get()=='1':
            list_question[1] = random.randint(1,10)
            list_question[2] = random.randint(0,list_question[1])
            list_question[3] = list_question[1]-list_question[2]
        elif model_list.get()=='2':
            list_question[1] = random.randint(11,19)
            list_question[2] = random.randint(1,list_question[1]-10)
            list_question[3] = list_question[1]-list_question[2]
        elif model_list.get()=='3':
            list_question[1] = random.randint(1,20)
            list_question[2] = random.randint(0,list_question[1])
            list_question[3] = list_question[1]-list_question[2]
    b = random.choice([1,2,3])
    result = list_question[b]
    list_result[0] = result
    list_question[b] = '?'
    string = str(list_question[1])+str(list_question[0])+str(list_question[2])+'='+str(list_question[3])
    canvas.bind('<Button-1>',click)
    canvas.create_text(100,50,text='第%s题' % number_question,font='黑体 -40 bold',fill='red',tags='text')    
    canvas.create_text(590,250,text=string,font='ComicSansMS -270 bold',fill='blue',tags='text')
    tag_done = 0

def start():
    global time_start
    global number_question
    global number_error
    global list_error
    number_question = 1
    number_error = 0
    time_start = int(time.time())
    get_question()
    init()
    button1.configure(text='下一题',command=nextquestion)
    R1.configure(state = 'disabled')
    R2.configure(state = 'disabled')
    R3.configure(state = 'disabled')
    button2.configure(state = 'normal')
    for s in range(len(list_error)):
        list_error.pop()
    

def nextquestion():
    global number_question
    global tag_done
    global number_error
    global list_error
    number_question += 1
    if tag_done == 0:
        number_error += 1
        list_error.append(str(list_question[1])+str(list_question[0])+str(list_question[2])+'='+str(list_question[3]))
    get_question()
    
def display():
    global time_start
    global time_end
    global number_question
    global number_error
    global list_error
    global tag_done
    
    if tag_done == 0:
        number_error += 1
        list_error.append(str(list_question[1])+str(list_question[0])+str(list_question[2])+'='+str(list_question[3]))
    canvas.delete('text')
    canvas.delete('init')
    time_end = int(time.time())
    canvas.create_text(1180/2,400,text='此次用时：%s 时 %s 分 %s 秒' % ((time_end-time_start)/3600,((time_end-time_start)%3600)/60,((time_end-time_start)%3600)%60),font='ComicSansMS -40 bold',fill='red',tags='text')
    canvas.create_text(1180/2,500,text='共 %s  错误 %s' % (number_question,number_error) ,font='ComicSansMS -40 bold',fill='red',tags='text')
    button1.configure(text='开始',command=start)
    R1.configure(state = 'normal')
    R2.configure(state = 'normal')
    R3.configure(state = 'normal')
    button2.configure(state = 'disabled')

def click(event):
    global number_error
    global tag_done
    global list_error
    x = event.x
    y = event.y
    for xy in list_number:
        if x < xy.x2 and x > xy.x1 and y < xy.y2 and y > xy.y1:
            tag_done = 1
            canvas.unbind('<Button-1>')
            canvas.create_rectangle(xy.x1,xy.y1,xy.x2,xy.y2,fill='red',tags='text')
            if xy.number == list_result[0]:
                canvas.create_text(700,400,text='正确,你好棒哦！',font='ComicSansMS -40 bold',fill='red',tags='text')
            else:
                canvas.create_text(700,400,text='错误，正确答案应为 '+str(list_result[0]),font='ComicSansMS -40 bold',fill='red',tags='text')
                number_error += 1
                list_error.append(str(list_question[1])+str(list_question[0])+str(list_question[2])+'='+str(list_question[3]))
                #print number_error
            break
            ##print xy.number,list_result[0]

def init():
    maxnum = 20
    num_width = 50
    canvas.create_line(65,580-45-num_width,1180-65,580-45-num_width,fill='black',width=2,tags='init')
    canvas.create_line(65,580-45,1180-65,580-45,fill='black',width=2,tags='init')
    for a in range(maxnum+1):
        canvas.create_line(65+a*num_width,580-45-num_width,65+a*num_width,580-45,fill='black',width=2,tags='init')
        canvas.create_text(65+(a+0.5)*num_width,580-45-num_width*0.5,text = a,font='ComicSansMS -40 bold',fill='black',tags='init')
        list_number.append(ClickNumber(65+a*num_width,580-45-num_width,65+(a+1)*num_width,580-45,a))
    canvas.create_line(65+(maxnum+1)*num_width,580-45-num_width,65+(maxnum+1)*num_width,580-45,fill='black',width=2,tags='init')
    

windows = Tk()
windows.maxsize(1200,700)
windows.minsize(1200,700)
windows.title("一年级数学练习  Version 1.0.5 ")

frame = Frame(windows,relief=GROOVE,borderwidth=10)
canvas = Canvas(frame,bg='green',width=1180,height=580)
model_list = StringVar()
model_list.set(1)
button1 = Button(windows,height=3,width=15,font='ComicSansMS -20 bold',text='开始',command=start)
button2 = Button(windows,state = 'disabled',height=3,width=15,font='ComicSansMS -20 bold',text='结束-显示成绩',command=display)
R1 = Radiobutton(windows,width=12,indicatoron = False ,text="10以内加减", variable=model_list, value=1)  
R2 = Radiobutton(windows,width=12,indicatoron = False ,text="20以内不进位", variable=model_list, value=2)  
R3 = Radiobutton(windows,width=12,indicatoron = False ,text="20以内含进位", variable=model_list, value=3)  
 
frame.grid(row=0,column=0,columnspan=9,rowspan=6)
canvas.grid(row=0,column=0,columnspan=9,rowspan=6)
R1.grid(row=6,column=2)
R2.grid(row=7,column=2)
R3.grid(row=8,column=2)
button1.grid(row=6,column=4,rowspan=3)
button2.grid(row=6,column=6,rowspan=3)

windows.mainloop()
