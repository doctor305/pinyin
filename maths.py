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
    button1.configure(text='下一题',command=nextquestion)

def nextquestion():
    global list_result
    get_question(10)
    
def display():
    canvas.delete('text')
    button1.configure(text='开始',command=start)
    #    canvas.create_text(590,500,text='此次出错的音节有： ',font='ComicSansMS -50 bold',fill='blue',tags='text')

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
#            print xy.number,list_result[0]
            
    

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
windows.title("一年级数学练习  Version 1.0.3 ")

#frame1 = Frame(windows,relief=GROOVE,borderwidth=10)
#frame2 = Frame(windows,borderwidth=5)

canvas = Canvas(windows,bg='green',width=1180,height=600)
model_list = StringVar()
model_list.set(1)
#model = OptionMenu(frame2,model_list,'10以内加减法','20以内不进位','20以内进位 ')
button1 = Button(windows,height=10,width=20,font='ComicSansMS -20 bold',text='开始',command=start)
button2 = Button(windows,height=10,width=20,font='ComicSansMS -20 bold',text='结束-显示成绩',command=display)
R1 = Radiobutton(windows,indicatoron = False ,text="Option 1", variable=model_list, value=1)  
R2 = Radiobutton(windows,indicatoron = False ,text="Option 2", variable=model_list, value=2)  
R3 = Radiobutton(windows,indicatoron = False ,text="Option 3", variable=model_list, value=3)  
 

#frame1.pack()
#frame2.pack()

canvas.grid(row=0, column=0)

#model.pack(side=LEFT)
R1.grid(row=1, column=1)
R2.grid(row=2, column=1)
R3.grid(row=3, column=1)
button1.grid(row=1, column=2)
button2.grid(row=1, column=3)


init(10)

windows.mainloop()
