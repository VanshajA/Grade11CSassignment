from tkinter import *
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

pacman = screen.create_arc(0,50,370,400,fill="yellow",start=45,extent=100)
