Width=3000
Length=3000
from time import*
from tkinter import *
from random import*
myInterface = Tk()
screen = Canvas( myInterface, width=Width, height=Length, background = "white" )
screen.pack()


spacing = 50

for x in range(0, Width, spacing): 
    screen.create_line( x, 25, x, Width, fill="blue")
    screen.create_text( x, 5, text=str(x), font="Times 9",fill="red", anchor = N)

for y in range(0, Length, spacing):
    screen.create_line( 25, y, Length, y, fill="blue")
    screen.create_text( 5, y, text=str(y), font="Times 9",fill="red", anchor = W)





#making the support for rocket
b1=900
b2=900
b3=100
b4=100

for b in range(5):
    build=screen.create_line(b1,100,b2,850,fill="yellow",width=3)
    b1=b1+50
    b2=b2+50

for c in range(16):
    buildy=screen.create_line(900,b3,1100,b4,fill="yellow",width=3)
    b3=b3+50
    b4=b4+50    




#rocket Values
y=100
y1=850
y2=75
y3=150

#Text Values
tx=275
ty=325
tw=375
ts=425
tq=475
tr=525


#make ground
Ground=screen.create_rectangle(0,850,1700,1000,fill="black")



for q in range(210):
    rocket1=screen.create_rectangle(850,y,900,y1,fill="red")
    rocket1part=screen.create_oval(850,y2,900,y3,fill="red")
    
    texts=screen.create_text(875,tx,text="S",fill="white",font="Arial 20")
    textp=screen.create_text(875,ty,text="P",fill="white",font="Arial 20")
    texta=screen.create_text(875,tw,text="A",fill="white",font="Arial 20")
    textc=screen.create_text(875,ts,text="C",fill="white",font="Arial 20")
    texte=screen.create_text(875,tq,text="E",fill="white",font="Arial 20")
    textx=screen.create_text(875,tr,text="X",fill="white",font="Arial 20")

    screen.update()
    sleep(0.02)
    screen.delete(rocket1,rocket1part,texts,textp,texta,textc,texte,textx)
    y=y-4
    y1=y1-4
    y2=y2-4
    y3=y3-4

    tx=tx-4
    ty=ty-4
    tw=tw-4
    ts=ts-4
    tq=tq-4

    tr=tr-4

    if y1<50:
        screen.configure(bg="black")
        b1=900
        b2=900
        b3=100
        b4=100
        for b in range(5):
            build=screen.create_line(b1,100,b2,850,fill="black",width=3)
            b1=b1+50
            b2=b2+50

        for c in range(16):
            buildy=screen.create_line(900,b3,1100,b4,fill="black",width=3)
            b3=b3+50
            b4=b4+50

        nStars = 300
        x = []
        y = []
        starDrawings = []

        for i in range(nStars):
            x.append(randint(0,1650))
            y.append(randint(0,900))
            starDrawings.append(0)
        for f in range(1000):
            for i in range(nStars):
                starDrawings[i]=screen.create_oval(x[i]-2, y[i]-2, x[i]+2, y[i]+2, fill="white")
                x[i] = x[i] - 5
                if x[i] < 0:
                    x[i]=1650
            screen.update()
            sleep(0.03)
            for i in range(nStars):
                screen.delete(starDrawings[i])

                


        
      

      

 

 
    


    


    

