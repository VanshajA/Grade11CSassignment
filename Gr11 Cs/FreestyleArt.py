


WIDTH=3000
HEIGHT=3000

from random import*
WIDTH=3000
HEIGHT=3000

from tkinter import *
myInterface = Tk()
screen = Canvas( myInterface, width=WIDTH, height=HEIGHT, background = "black" )
screen.pack()






#drawMoon
screen.create_polygon(860,110,875,142,900,175,950,200,1000,198,1050,160,1070,140,1083,120,1083,150,1075,178,1063,200,1035,233,1000,246,950,246,900,225,865,175, fill = "white",smooth = True)


#guy

screen.create_oval(950,100,1000,150,fill="gray")
screen.create_line(975,150,975,200,fill="gray",width=3)
screen.create_line(975,200,950,250,width=3,fill="gray")
screen.create_line(975,200,1000,250,width=3,fill="gray")
screen.create_line(975,175,950,175,width=3,fill="gray")
screen.create_line(975,175,1000,175,width=3,fill="gray")



#Draw Stars
for f in range(2500):
    x=randint(0,WIDTH)
    y=randint(0,HEIGHT)
    stars=screen.create_oval(x,y,x+4,y+4,fill="white",outline="white")

#createplane
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

Plane1=screen.create_rectangle(x1,y1,x2,y2,fill="gray",outline="gray")
Plane2=screen.create_arc(x11,y11,x12,y12,start=0,extent=270,fill="gray",outline="gray")
Plane3=screen.create_arc(x21,y21,x22,y22,start=180,extent=270,fill="gray",outline="gray")
PlaneWings1=screen.create_polygon(x31,y32,x32,y33,x33,100,fill="gray")
PlaneWings2=screen.create_polygon(x41,y41,x42,y42,x43,y43,fill="gray")


#text
screen.create_text(350,300,text="We are coming home!",font="Arial 20",fil="white")

#Ground
ground=screen.create_rectangle(50,900,1650,1000,fill="black")



#buildings

building1=screen.create_rectangle(50,650,250,1000,fill="white")
building2=screen.create_rectangle(350,500,550,1000,fill="white")
building3=screen.create_rectangle(600,400,850,1000,fill="white")
building4=screen.create_rectangle(950,550,1150,1000,fill="white")
building5=screen.create_rectangle(1300,50,1600,1000,fill="white")



x1=50
x2=50
y1=650
y2=1000



#Buidinglinesdown

for line in range(30):
    line=screen.create_line(x1,y1,x2,y2,fill="black",width=3)

    x1=x1+50
    x2=x2+50
    
#BuildingLines
x11=50
x22=250
y11=700
y22=700


for lineacross in range(30):
    lines=screen.create_line(x11,y11,x22,y22,fill="black",width=3)

    y11=y11+50
    y22=y22+50



#Building 2

xx1=350
yy1=500
xx2=350
yy2=900

xxx1=350
xxx2=550
yyy1=550
yyy2=550

for line2down in range(15):
    lin=screen.create_line(xx1,yy1,xx2,yy2,fill="black",width=3)

    xx1=xx1+50
    xx2=xx2+50


for line2across in range(15):
    ok=screen.create_line(xxx1,yyy1,xxx2,yyy2,fill="black",width=3)

    yyy1=yyy1+50
    yyy2=yyy2+50



#Building3

fx=600
fy=400
sx=600
sy=900

for lol in range(15):
    l=screen.create_line(fx,fy,sx,sy,fill="black",width=3)
    fx=fx+50
    sx=sx+50


firstx=600
firsty=450
secondx=850
secondy=450

for hi in range(15):
    ll=screen.create_line(firstx,firsty,secondx,secondy,fill="black",width=3)

    firsty=firsty+50
    secondy=secondy+50


    
#Building4

a=950
b=550
c=950
d=900

aa=950
bb=600
cc=1150
dd=600


for yes in range(15):
    linz=screen.create_line(a,b,c,d,fill="black",width=3)

    a=a+50
    c=c+50

for no in range(15):
    screen.create_line(aa,bb,cc,dd,fill="black",width=3)
    bb=bb+50
    dd=dd+50
    


#Building 5

num1=1300
num2=50
num3=1300
num4=1000

for xx in range(15):
    screen.create_line(num1,num2,num3,num4,fill="black",width=3)
    num1=num1+50
    num3=num3+50


na=1300
nb=100
nc=1600
nd=100

for h in range(30):
    screen.create_line(na,nb,nc,nd,fill="black",width=3)
    nb=nb+50
    nd=nd+50









