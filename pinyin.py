# -*- coding: utf-8 -*-
## Author: Jin Feng
## Date: 2017-10-29
## 

from Tkinter import *
import os
import random


list_pinyin_all = ['ɑ','o','e','i','u','ü','b','p','m','f','d','t','n','l','ɡ','k','h','j','q','x','zh','ch','sh','r','z','c','s','y','w','ɑi','ei','ui','ɑo','ou','iu','ie','üe','er','ɑn','en','in','un','ün','ɑnɡ','enɡ','inɡ','onɡ']
list_pinyin_shengmu = ['b','p','m','f','d','t','n','l','ɡ','k','h','j','q','x','zh','ch','sh','r','z','c','s','y','w']
list_pinyin_yunmu = ['ɑ','o','e','i','u','ü','ɑi','ei','ui','ɑo','ou','iu','ie','üe','er','ɑn','en','in','un','ün','ɑnɡ','enɡ','inɡ','onɡ']
list_error = []
list_pinyin_txt = []
number = 0
letter_temp = ''

def read_txt():
    with open('pinyin.txt','r') as f:
        for line in f.read():
            if line[0] != '#' and len(line) != 0:
                print line
                list_pinyin_txt.append(line)
        
        
def display_letter(ls):
    letter = random.choice(ls)
    canvas.delete('text')
    canvas.create_text(590,300,text=letter,font='ComicSansMS -500 bold',fill='blue',tags='text')
    return letter

def yes():
    global number
    global letter_temp
    if letter_temp != '':
        number += 1
    letter_temp = display_letter(list_pinyin_all)
    

def no():
    global number
    global letter_temp
    if letter_temp != '':
        list_error.append(letter_temp)
        number += 1
    letter_temp = display_letter(list_pinyin_all)
    
    

def display():
    global number
    global list_error
    global letter_temp
    canvas.delete('text')
    n = len(list_error)
    msg = '答题 %s 道，错误 %s 道' % (number,n)
    canvas.create_text(590,300,text=msg,font='ComicSansMS -100 bold',\
                       fill='blue',tags='text')
    if n <= 10 and n > 1:
        msg2 = ' ，'.join(list_error)
        canvas.create_text(590,500,text='此次出错的音节有： ',font='ComicSansMS -50 bold',\
                           fill='blue',tags='text')
        canvas.create_text(590,570,text=msg2,font='ComicSansMS -50 bold',\
                           fill='red',tags='text')
    elif n == 0:
        canvas.create_text(590,500,text='很棒！这次全对了！ ',font='ComicSansMS -50 bold',\
                           fill='blue',tags='text')
    elif n == 1:
        canvas.create_text(590,500,text='此次出错的音节有： ',font='ComicSansMS -50 bold',\
                           fill='blue',tags='text')
        canvas.create_text(590,570,text=list_error[0],font='ComicSansMS -50 bold',\
                           fill='red',tags='text')
    else:
        canvas.create_text(590,500,text='错误太多了，还需努力！ ',font='ComicSansMS -50 bold',\
                           fill='blue',tags='text')
    list_error = []
    number = 0
    letter_temp = ''

#read_txt()
#print list_pinyin_txt
windows = Tk()
windows.maxsize(1200,700)
windows.minsize(1200,700)
windows.title("一年级拼音练习  Version 1.0.1 ")
windows.iconbitmap("pinyin.ico")

frame1 = Frame(windows,relief=GROOVE,borderwidth=10)
frame2 = Frame(windows,borderwidth=5)

canvas = Canvas(frame1,bg='green',width=1180,height=600)
button1 = Button(frame2,height=10,width=10,text='正确',command=yes)
button2 = Button(frame2,height=10,width=10,text='错误',command=no)
button3 = Button(frame2,height=10,width=20,text='结束-显示成绩',command=display)


frame1.pack()
frame2.pack()

canvas.pack()

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)


windows.mainloop()
