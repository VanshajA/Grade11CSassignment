from tkinter import *
from random import*
myInterface = Tk()
screen = Canvas( myInterface, width=900, height=900, background = "black" )
screen.pack()













mycolor="blue"




dx = 50
dy = 150

for k in range(1,8):

    intdx=0
    intdy=0

    for i in range (1,9):
        

        for j in range (0,i):
            
            for f in range(600):
                x=randint(dx,dy)
                y=randint(dx,dy)
                s=randint(1,4)
                screen.create_oval(x+intdx,y,x+s+intdx,y,fill=mycolor)
                screen.create_oval(x,y+intdx,x+s,y+intdx,fill=mycolor)

        
   
        if mycolor=="blue":
            mycolor="yellow"
        else:
            mycolor="blue"
            
        intdx=intdx+100
        intdy=intdy+100
    dx=dx+100
    dy=dy+100
    




             
 

    
    

    
 
    
    
 


           

 

    

        
        
    
        


   
        








#first line
x1=50
x2=50
y1=50
y2=850
#SecondLine
x11=50
x22=850
y11=50
y22=50







for x in range(0,9):
    Xline=screen.create_line(x1,y1,x2,y2,fill="red")

    x1=x1+100
    x2=x2+100
    for y in range(0,9):
        Yline=screen.create_line(x11,y11,x22,y22,fill="red")

        y11=y11+100
        y22=y22+100
    



