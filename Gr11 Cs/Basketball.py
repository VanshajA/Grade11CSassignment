WIDTH=3000
HEIGHT=3000
from time import*
from tkinter import *
from math import*
myInterface = Tk()
screen = Canvas( myInterface, width=WIDTH, height=HEIGHT, background = "#ffcc99" )
screen.pack()


spacing = 50

for x in range(0, WIDTH, spacing): 
    screen.create_line( x, 25, x, WIDTH, fill="blue")
    screen.create_text( x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, HEIGHT, spacing):
    screen.create_line( 25, y, HEIGHT, y, fill="blue")
    screen.create_text( 5, y, text=str(y), font="Times 9", anchor = W)








#BasketballCourt left side
MidCricel=screen.create_oval(650,600,900,350,fill="#ffa64d",outline="blue",width=2)
rectline=screen.create_line(50,600,400,600,fill="blue",width=3)
line2=screen.create_line(400,300,400,600,fill="blue",width=3)
line3=screen.create_line(50,300,400,300,fill="blue",width=3)
insideoval=screen.create_oval(700,550,850,400,fill="#ffa64d",outline="blue",width=2)
Midline= screen.create_line(780, 1000, 780, 0, fill= "blue", width=2)
freethrow=screen.create_oval(300,350,550,550,fill="#ffcc99",outline="blue",width=2)
backrect=screen.create_rectangle(50,350,400,550,fill="#ff8000")



#Basketballcourt right side
line4=screen.create_line(1650,600,1300,600,fill="blue",width=3)
line5=screen.create_line(1300,600,1300,300,fill="blue",width=3)
line6=screen.create_line(1300,300,1650,300,fill="blue",width=3)
rightfreethrow=screen.create_oval(1150,350,1350,550,fill="#ffcc99",outline="blue",width=2)
backrectright=screen.create_rectangle(1300,350,1650,550,fill="#ff8000")



#basketballnet
netstick=screen.create_line(50,400,200,400,fill="black",width=4)
netstick2=screen.create_line(50,500,200,500,fill="black",width=4)
net=screen.create_oval(100,400,200,500,fill="white")
netline=screen.create_line(110,420,190,420,fill="black",width=2)
netline2=screen.create_line(110,440,190,440,fill="black",width=2)
netline3=screen.create_line(110,460,190,460,fill="black",width=2)
netline4=screen.create_line(110,480,190,480,fill="black",width=2)
netline5=screen.create_line(110,410,110,500,fill="black",width=2)
netline6=screen.create_line(150,410,150,500,fill="black",width=2)
netline7=screen.create_line(180,420,180,500,fill="black",width=2)


#Basketball stands
L=50
q=75
r=60
y=60
o=60
t=50
a=60
b=70

stand=screen.create_rectangle(50,50,1650,200,fill="gray",outline="black",width=5)
standline=screen.create_line(50,125,1650,125,fill="white",width=5)
vip=screen.create_text(750,175,text="VIP SECTION",fill="gold",font="Arial 20")
stan2=screen.create_rectangle(50,800,1650,950,fill="gray",outline="black",width=5)
text=screen.create_text(750,875,text="UNDER CONSTRUCTION",fill="red",font="Arial 20")

for p in range(79):
    People=screen.create_oval(L,50,q,80,fill="white")
    line=screen.create_line(r,60,y,100,fill="white")
    leg=screen.create_line(o,100,t,125,fill="white")
    leg2=screen.create_line(a,100,b,125,fill="white")

    L=L+20
    q=q+20
    r=r+20
    y=y+20
    o=o+20
    t=t+20
    a=a+20
    b=b+20




    
    



y1=400
y2=450
y3=450
y4=500
y5=500
y6=525
y7=475
y8=475
y9=475
y10=475
e1=438
e2=413
e3=438
e4=413
s1=470
s2=500




#charcter
for man in range(10):
    face=screen.create_oval(550,y1,600,y2,fill="brown")
    body=screen.create_line(575,y3,575,y4,fill="black",width=2)
    leg=screen.create_line(575,y5,575,y6,fill="black",width=2)
    arm=screen.create_line(575,y7,550,y8,fill="black",width=2)
    arm2=screen.create_line(575,y9,600,y10,fill="black",width=2)
    shirt=screen.create_rectangle(555,s1,595,s2,fill="blue",width=3)
    eye1=screen.create_oval(560,e1,570,e2,fill="white")
    eye=screen.create_oval(580,e3,590,e4,fill="white")
    



    y1=y1-5
    y2=y2-5
    y3=y3-5
    y4=y4-5
    y5=y5-5
    y6=y6-5
    y7=y7-5
    y8=y8-5
    y9=y9-5
    y10=y10-5
    e1=e1-5
    e2=e2-5
    e3=e3-5
    e4=e4-5
    s1=s1-5
    s2=s2-5

    screen.update()
    sleep(0.10)
    screen.delete(face,body,leg,arm,arm2,eye1,eye,shirt)
face=screen.create_oval(550,y1+15,600,y2+15,fill="brown")
body=screen.create_line(575,y3+15,575,y4+15,fill="black",width=2)
leg=screen.create_line(575,y5+15,575,y6+15,fill="black",width=2)
arm=screen.create_line(575,y7+15,550,y8+15,fill="black",width=2)
arm2=screen.create_line(575,y9+15,600,y10+15,fill="black",width=2)
shirt=screen.create_rectangle(555,s1,595,s2,fill="blue",width=3)
eye1=screen.create_oval(560,e1,570,e2,fill="white")
eye=screen.create_oval(580,e3,590,e4,fill="white")
    




x=550
y=425
r=10


#Basketball
for f in range(300):
    x = -5*f + 550                          
    y = 0.2*f**2 - 15*f + 425
    ball = screen.create_oval( x-r, y-r, x+r, y+r, fill= "blue" )
    screen.update()
    sleep(0.03)
    screen.delete( ball )



     


    
    
    











