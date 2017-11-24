from Tkinter import *
def printEventInfo(event):
    print 'event.time = ' , event.time
    print 'event.type = ' , event.type
    print 'event.WidgetId = ', event.widget
    print 'event.KeySymbol = ',event.keysym

def chang():
##    b['text']='test'
##    b['command']=print2
    b.configure(text='test',command=print2)

def print1():
    print "test 1"

def print2():
    print "test 2"

root = Tk()
b = Button(root,text = 'Infomation',command = print1)
b2 = Button(root,text = 'Change',command = chang)
#b.bind("<Enter>",printEventInfo)
b.pack()
b2.pack()
#b.focus_set()
root.mainloop()  
