from tkinter import *
from time import*

myInterface = Tk()
screen = Canvas( myInterface, width=800, height=800, background = "white" )
screen.pack()
spacing = 50

for x in range(0, 1000, spacing): 
    screen.create_line( x, 25, x, 1000, fill="blue")
    screen.create_text( x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line( 25, y, 1000, y, fill="blue")
    screen.create_text( 5, y, text=str(y), font="Times 9", anchor = W)

Trafficlight=["Green","Yellow","Red"]

for i in range(50):
  screen.create_oval(450,400,500,450,fill=Trafficlight[i%len(Trafficlight)])
  screen.update()
  sleep(0.25)
  screen.mainloop()
