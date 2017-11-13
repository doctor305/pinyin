from Tkinter import *
from math import sqrt

class Qizi():
    def __init__(self,i,j,color='none'):
        self.x = 50+i*25
        self.y = 50+j*25
        self.color = color
        self.tag = (i,j)
    def __str__(self):
        return self.color+'('+str(self.x)+','+str(self.y)+')'+'tag:('+str(self.tag)+')'
    def get_coo(self):
        return self.x,self.y
    def state(self):
        if self.color == 'none':
            return False
        else:
            return True
    def go(self,tag):
        if tag == 1:
            self.color = 'black'
        else:
            self.color = 'white'
        canvas.create_oval(self.x-10,self.y-10,self.x+10,self.y+10,\
                           fill = self.color,tag='qizi')

        
def is_gameover(num1,num2,color):
    if check(num1,num2,color):
        canvas.create_text(275,200,text='Game  Over',font='Helvetica -80 bold',\
                           fill='blue',tag='text')
        canvas.create_text(275,300,text=color+'  WIN',font='Helvetica -80 bold',\
                           fill='red',tag='text')
        canvas.unbind('<Button-1>')
def check(num1,num2,color):        
    max_x = 0
    max_y = 0
    max_xy = 0
    max_yx = 0
    step = 1
##  horizontal direction
    while num1-step>=0:
        if qizi_list[num1-step][num2].color == color:
            max_x += 1
            step += 1
        else:
            step = 1
            break
    else:
        step = 1
    while num1+step<=18:
        if qizi_list[num1+step][num2].color == color:
            max_x += 1
            step += 1
        else:
            step = 1
            break
    else:
        step = 1
    if max_x >= 4:
        return True
##   vertical direction
    while num2-step>=0:
        if qizi_list[num1][num2-step].color == color:
            max_y += 1
            step += 1
        else:
            step = 1
            break
    else:
        step = 1
    while num2+step<=18:
        if qizi_list[num1][num2+step].color == color:
            max_y += 1
            step += 1
        else:
            step = 1
            break
    else:
        step = 1
    if max_y >= 4:
        return True
#########################################################  
    while num2+step<=18 and num1+step<=18:
        if qizi_list[num1+step][num2+step].color == color:
            max_xy += 1
            step += 1
        else:
            step = 1
            break
    else:
        step = 1
    while num2-step>=0 and num1-step>=0:
        if qizi_list[num1-step][num2-step].color == color:
            max_xy += 1
            step += 1
        else:
            step = 1
            break
    else:
        step = 1
    if max_xy >= 4:
        return True
########################################################
    while num2+step<=18 and num1-step>=0:
        if qizi_list[num1-step][num2+step].color == color:
            max_yx += 1
            step += 1
        else:
            step = 1
            break
    else:
        step = 1
    while num2-step>=0 and num1+step<=18:
        if qizi_list[num1+step][num2-step].color == color:
            max_yx += 1
            step += 1
        else:
            step = 1
            break
    else:
        step = 1
    if max_yx >= 4:
        return True
  
        
def click(event):
    global PLAYER
##    print event.x,event.y
    x = event.x
    y = event.y
    for k in range(19):
        for l in range(19):
            if not qizi_list[l][k].state():
                qizi_x, qizi_y = qizi_list[l][k].get_coo()
                if sqrt((qizi_x-x)**2+(qizi_y-y)**2)<10:
                    qizi_list[l][k].go(PLAYER)
                    PLAYER = -PLAYER
                    is_gameover(l,k,qizi_list[l][k].color)
                    break
root = Tk()
canvas = Canvas(root,width=550,height=650,bg='yellow')
PLAYER = 1
for m in range(19):
    canvas.create_line(50,50+m*25,18*25+50,50+m*25,fill='black',width=2)
for n in range(19):
    canvas.create_line(50+n*25,50,50+n*25,18*25+50,fill='black',width=2)
qizi_list = []
for j in range(19):
    temp_list = []
    for i in range(19):
        temp_list.append(Qizi(i,j))
    qizi_list.append(temp_list)

canvas.bind('<Button-1>',click)


canvas.pack()

root.mainloop()
