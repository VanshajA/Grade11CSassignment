WIDTH=2000
HEIGHT=2000
from tkinter import *
from time import*
myInterface = Tk()
screen = Canvas( myInterface, width=WIDTH, height=HEIGHT, background = "white" )
screen.pack()



#Ground
ground=screen.create_rectangle(50,800,WIDTH,HEIGHT,fill="#663300")

building=screen.create_rectangle(1200,50,1500,800,fill="skyblue")


#Plane
Plane1=screen.create_rectangle(125,250,525,350,fill="gray",outline="gray")
Plane2=screen.create_arc(50,350,200,250,start=0,extent=270,fill="gray",outline="gray")
Plane3=screen.create_arc(450,350,600,250,start=180,extent=270,fill="gray",outline="gray")

PlaneWings1=screen.create_polygon(400,250,325,275,150,100,fill="gray")
PlaneWings2=screen.create_polygon(325,325,400,350,150,525,fill="gray")


spacing = 50

for x in range(0, WIDTH, spacing): 
    screen.create_line( x, 25, x, WIDTH, fill="blue")
    screen.create_text( x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, HEIGHT, spacing):
    screen.create_line( 25, y, HEIGHT, y, fill="blue")
    screen.create_text( 5, y, text=str(y), font="Times 9", anchor = W)


#x = 300   
#y = 150
#r = 10

#for f in range(200):   
   # ball = screen.create_oval( x-r, y-r, x+r, y+r, fill= "blue" )   
   # screen.update()		
    #sleep(0.03)			 
    #screen.delete( ball )
    #x = x + 5		



