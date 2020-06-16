from tkinter import *
from random import randrange as rnd, choice
import time


def create_objekt():
    global ball,x1,y1,ball2,x_wei,y_wei
    canv.delete(ALL)

    x = rnd(100,500)
    y = rnd(100,300)
    r = rnd(30,50)
    x2 = rnd(100,500)
    y2 = rnd(100,300)
    r2 = rnd(30,50)

    ball=canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors),outline='black', width=1)
    ball2=canv.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill = choice(colors),outline='black', width=1)
    
    x1= choice(wais)
    y1= choice(wais)
    x_wei= choice(wais)
    y_wei= choice(wais)

    canv.after(4000,create_objekt)
    move()

    

def singl_move ():
    global x1,y1,x_wei,y_wei
    coordss=canv.coords(ball)
    coordss2=canv.coords(ball2)

    if  len(coordss)!=0 and coordss[0]>0 and coordss[1]>0 and coordss[2]<600 and coordss[3]<600 :    
        canv.move(ball, x1,y1)
        if len(coordss2)!=0 and coordss2[0]>0 and coordss2[1]>0 and coordss2[2]<600 and coordss2[3]<600 :
            canv.move(ball2,x_wei,y_wei)
            
    elif len(coordss2)!=0 and coordss2[0]>0 and coordss2[1]>0 and coordss2[2]<600 and coordss2[3]<600 :
        canv.move(ball2,x_wei,y_wei)
    elif len(coordss)!=0 and coordss[0]<=0 :
        x1*=-1
        canv.move(ball, x1,y1)
    elif len(coordss)!=0  and coordss[2]>=600 :
        x1*=-1
        canv.move(ball, x1,y1)    
    elif len(coordss)!=0 and coordss[1]<=0:
        y1*=-1
        canv.move(ball, x1,y1)
    elif len(coordss)!=0  and coordss[3]>=600:
        y1*=-1
        canv.move(ball, x1,y1)    
    elif len(coordss2)!=0 and coordss2[0]<=0 :
        x_wei*=-1
        canv.move(ball2,x_wei,y_wei)
    elif len(coordss2)!=0  and coordss2[2]>=600:
        x_wei*=-1
        canv.move(ball2,x_wei,y_wei)
    elif len(coordss2)!=0 and coordss2[1]<=0 :
        y_wei*=-1
        canv.move(ball2,x_wei,y_wei) 
    elif len(coordss2)!=0  and coordss2[3]>=600:
        y_wei*=-1
        canv.move(ball2,x_wei,y_wei)      
    canv.after(40,singl_move)


def move():
    global x1,y1,x_wei,y_wei
    coordss=canv.coords(ball)
    coordss2=canv.coords(ball2) 
    try:   
        if  coordss[0]>0 and coordss[1]>0 and coordss[2]<600 and coordss[3]<600 and coordss2[0]>0 and coordss2[1]>0 and coordss2[2]<600 and coordss2[3]<600 :    
            canv.move(ball, x1,y1)
            canv.move(ball2,x_wei,y_wei)
        elif coordss[0]<=0 or coordss[2]>=600 :
            x1*=-1
            canv.move(ball, x1,y1)

        elif coordss[1]<=0 or coordss[3]>=600:
            y1*=-1
            canv.move(ball, x1,y1)

        elif coordss2[0]<=0 or coordss2[2]>=600:
            x_wei*=-1
            canv.move(ball2,x_wei,y_wei)
        elif coordss2[1]<=0 or coordss2[3]>=600:
            y_wei*=-1
            canv.move(ball2,x_wei,y_wei) 
        canv.after(40,move)
    except IndexError :
        singl_move()
    return


def click(event):
    
    coordss=canv.coords(ball)
    coordss2=canv.coords(ball2)

    if len(coordss)!=0 and event.x > coordss[0] and event.x < coordss[2] and event.y > coordss[1] and event.y < coordss[3] :
        l1['text']=int(l1['text'])+1
        canv.delete(ball)
    elif event.x > coordss2[0] and event.x < coordss2[2] and event.y > coordss2[1] and event.y < coordss2[3]  :
        l1['text']=int(l1['text'])+1
        canv.delete(ball2)
    else:
            return


root = Tk()
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2 
w = w - 300 # смещение от середины
h = h - 300
root.geometry('600x600+{}+{}'.format(w, h))
canv = Canvas(root,bg='white')

a = Toplevel()
a.title('очки')
w = a.winfo_screenwidth() # ширина экрана
h = a.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2 
w = w + 315 # смещение от середины
h = h - 300
a.geometry('200x250+{}+{}'.format(w, h))
a.resizable(False, False)
l= Label (a,text='ваши очки ')
l1=Label(a,text='0')


wais=[2,-2,1.5]
colors = ['red','orange','yellow','green','blue','lime','navy','indigo']
speed=(40,50)



canv.pack(fill=BOTH,expand=1)
l.grid(row=0, column=0)
l1.grid(row=0, column=1)

create_objekt()
# root.after(40,move)
move()



canv.bind('<Button-1>', click)

root.mainloop()