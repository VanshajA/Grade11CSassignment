
WIDTH=2000
HEIGHT=2000
from tkinter import *
from time import*
myInterface = Tk()
screen = Canvas( myInterface, width=WIDTH, height=HEIGHT, background = "skyblue" )
screen.pack()













#Ground
ground=screen.create_rectangle(0,800,WIDTH,HEIGHT,fill="#663300")

x1p=1200
y1p=50
x2p=1200
y2p=800

x1q=1200
y1q=100
x2q=1500
y2q=100






building=screen.create_rectangle(1200,50,1500,800,fill="gray")


for line in range(7):

    screen.create_line(x1p,y1p,x2p,y2p,fill="black",width=3)

    x1p=x1p+50
    x2p=x2p+50

for y in range(14):
    screen.create_line(x1q,y1q,x2q,y2q,fill="black",width=3)

    y1q=y1q+50
    y2q=y2q+50


avg=screen.create_text(1350,300,text="Avengers Building",font="Arial 25")






x1=125
x2=525
x11=50
x12=200
x21=450
x22=600
x31=400
x32=325
x33=150
x41=325
x42=400
x43=150

y1=250
y2=350
y11=350
y12=250
y21=350
y22=250
y32=250
y33=275
y41=325
y42=350
y43=525

x45=450
y45=300

w1=100
wy1=280
wy2=310
wy3=280
wy4=310
wy5=280
wy6=310
w2=150
w3=160
w4=210
w5=220
w6=270






#Plane
for f in range(200):
    Plane1=screen.create_rectangle(x1,y1,x2,y2,fill="gray",outline="gray")
    Plane2=screen.create_arc(x11,y11,x12,y12,start=0,extent=270,fill="gray",outline="gray")
    Plane3=screen.create_arc(x21,y21,x22,y22,start=180,extent=270,fill="gray",outline="gray")
    PlaneWings1=screen.create_polygon(x31,y32,x32,y33,x33,100,fill="gray")
    PlaneWings2=screen.create_polygon(x41,y41,x42,y42,x43,y43,fill="gray")
    text=screen.create_text(x45,y45,text="Vansh Airlines",font="Arial 20")
    window=screen.create_rectangle(w1,wy1,w2,wy2,fill="skyblue")
    window1=screen.create_rectangle(w3,wy3,w4,wy4,fill="skyblue")
    window2=screen.create_rectangle(w5,wy5,w6,wy6,fill="skyblue")


    screen.update()
    sleep(0.02)
    screen.delete(Plane1,Plane2,Plane3,PlaneWings1,PlaneWings2,text,window,window1,window2)

    w1=w1+5
    w2=w2+5
    w3=w3+5
    w4=w4+5
    w5=w5+5
    w6=w6+5



    
    x1=x1+5
    x2=x2+5
    x11=x11+5
    x12=x12+5
    x21=x21+5
    x22=x22+5
    x31=x31+5
    x32=x32+5
    x33=x33+5
    x41=x41+5
    x42=x42+5
    x43=x43+5
    x45=x45+5

    if x2>=1200:
        y1=y1+7
        y2=y2+7
        y11=y11+7
        y12=y12+7
        y21=y21+7
        y22=y22+7
        y32=y32+7
        y33=y33+7
        y41=y41+7
        y42=y42+7
        y43=y43+7
        y45=y45+7
        wy1=wy1+7
        wy2=wy2+7
        wy3=wy3+7
        wy4=wy4+7
        wy5=wy5+7
        wy6=wy6+7
        
        
        




    







