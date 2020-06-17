from tkinter import *
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=800, background = "black" )
screen.pack()




#pie 1

pacman2 = screen.create_arc(250,50,600,400,fill="blue",start = -30,extent=-70)

pacman = screen.create_arc(315,83,650,423,fill="red",start = -190,extent=71)

pacman = screen.create_arc(204,200,600,600,fill="green",start = 25,extent=90)


















