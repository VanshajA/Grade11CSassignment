

Width=3000
Length=3000
from time import*
from tkinter import *
from random import*
myInterface = Tk()
screen = Canvas( myInterface, width=Width, height=Length, background = "gray" )
screen.pack()


#Creating The HeadQuarters
tv=screen.create_rectangle(50,200,1650,350,fill="#ccffff")
line=screen.create_line(50,900,550,350,fill="black",width=5)
lein1=screen.create_line(1050,350,1650,900,fill="black",width=5)
stand=screen.create_rectangle(500,450,1150,550,fill="black")
stand1=screen.create_rectangle(300,650,1350,750,fill="black")
stand2=screen.create_rectangle(150,800,1500,950,fill="black")
side=screen.create_polygon(50,350,50,900,550,350,fill="black")
side2=screen.create_polygon(1050,350,1650,900,1650,350,fill="black")


#variable for people
x=350
xx=400
ll=550
lo=550




#Sign colours

Colors=["Red","Yellow"]



#Squares in HeadQuarters
for p in range(19):
    head=screen.create_rectangle(x,650,xx,700,fill="white",width=2)
    x=x+50
    xx=xx+50



for l in range(2):
    linx=screen.create_line(ll,200,lo,350,fill="black",width=4)
    ll=ll+500
    lo=lo+500




#Create SpaceX Logo
text=screen.create_text(250,275,text="SPACE",fill="white",font="Ariral 50")
text=screen.create_text(825,275,text="X",fill="white",font="Ariral 50")
text=screen.create_text(1300,275,text="STATION",fill="white",font="Ariral 50")
face=screen.create_oval(550,800,600,850,fill="white")
line=screen.create_line(575,850,575,875,fill="white")
face=screen.create_oval(800,800,850,850,fill="white")




#Text For people to say
screen.create_text(650,850,text="Sir we are ready for launch",fill="white")
screen.create_text(900,850,text="OKAY GOOOOOO",fill="white")
t=800





#Create Launching Sign
for f in range(20):


    for i in range(100):
        lol=screen.create_text(t,400,text="!LAUNCHING!",fill=Colors[i%len(Colors)],font="Ariral 50")
        t=t+5
        screen.update()
        sleep(0.02)
        screen.delete(lol)


    if t>1650:
      
        screen.delete("all")

        screen.configure(bg="#99ffff")

        b1=900
        b2=900
        b3=100
        b4=100
        break

#Make Support for rocket
for b in range(5):
    build=screen.create_line(b1,100,b2,850,fill="yellow",width=5)
    b1=b1+50
    b2=b2+50


for c in range(16):
    buildy=screen.create_line(900,b3,1100,b4,fill="yellow",width=5)
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




#Create Rocket(Standing Still)
rocket1=screen.create_rectangle(850,y,900,y1,fill="white",outline="white")
rocket1part=screen.create_oval(850,y2,900,y3,fill="white",outline="white")    
texts=screen.create_text(875,tx,text="S",fill="black",font="Arial 20")
textp=screen.create_text(875,ty,text="P",fill="black",font="Arial 20")
texta=screen.create_text(875,tw,text="A",fill="black",font="Arial 20")
textc=screen.create_text(875,ts,text="C",fill="black",font="Arial 20")
texte=screen.create_text(875,tq,text="E",fill="black",font="Arial 20")
textx=screen.create_text(875,tr,text="X",fill="black",font="Arial 20")
screen.update()
sleep(0.02)




# Make smoke variable
x=[]
y=[]
xSpeeds=[]
ySpeeds=[]
sizes=[]
colours=[]
boxDrawings=[]
Nsmoke=400



#Fill Array with random Values
for i in range(Nsmoke):
    x.append(randint(800,950))
    y.append(randint(600,700))
    xSpeeds.append(randint(-10,10))
    ySpeeds.append(randint(5,8))
    sizes.append(randint(20,30))
    colours.append(choice(["gray"]))
    boxDrawings.append(0)




#Animate for 50 smoke
for f in range(50):



    for i in range(50):
        boxDrawings[i]=screen.create_oval( x[i], y[i], x[i] +sizes[i], y[i] +sizes[i], fill= colours[i])
        x[i]=x[i]+xSpeeds[i]
        y[i]=y[i]+ySpeeds[i]
    screen.update()
    sleep(0.03)



    for i in range(50):
        screen.delete(boxDrawings[i])




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



#Delete previous rocket 
screen.delete(rocket1,rocket1part,texts,textp,texta,textc,texte,textx)




#make ground
Ground=screen.create_rectangle(0,850,1700,1000,fill="black")



#Make Rocket Fly
for q in range(210):
    rocket1=screen.create_rectangle(850,y,900,y1,fill="white",outline="white")
    rocket1part=screen.create_oval(850,y2,900,y3,fill="white",outline="white")
    
    texts=screen.create_text(875,tx,text="S",fill="black",font="Arial 20")
    textp=screen.create_text(875,ty,text="P",fill="black",font="Arial 20")
    texta=screen.create_text(875,tw,text="A",fill="black",font="Arial 20")
    textc=screen.create_text(875,ts,text="C",fill="black",font="Arial 20")
    texte=screen.create_text(875,tq,text="E",fill="black",font="Arial 20")
    textx=screen.create_text(875,tr,text="X",fill="black",font="Arial 20")

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
        screen.configure(bg="black") #Make screen black
        b1=900
        b2=900
        b3=100
        b4=100



#Make the support black too
        for b in range(5):
            build=screen.create_line(b1,100,b2,850,fill="black",width=5)
            b1=b1+50
            b2=b2+50


        for c in range(16):
            buildy=screen.create_line(900,b3,1100,b4,fill="black",width=5)
            b3=b3+50
            b4=b4+50


            
                        
#import Image of Moon
        img=PhotoImage(file='C:\\Users\\vansh\\Downloads\\monlololp.png')
        screen.create_image(200,200,anchor=NW,image=img)


 
#Draw Stars
        nStars = 300
        x = []
        y = []
        starDrawings = []

        for i in range(nStars):
            x.append(randint(0,1650))
            y.append(randint(0,900))
            starDrawings.append(0)

        for f in range(50):

            for i in range(nStars):
                starDrawings[i]=screen.create_oval(x[i]-2, y[i]-2, x[i]+2, y[i]+2, fill="white")
                x[i] = x[i] - 5

                if x[i] < 0:
                    x[i]=1650
            screen.update()
            sleep(0.03)

            for i in range(nStars):
                screen.delete(starDrawings[i])
        screen.delete("all")
        screen.configure(bg="gray")


#Create HeadQuarters(Again)
        tv=screen.create_rectangle(50,200,1650,350,fill="#ccffff")
        line=screen.create_line(50,900,550,350,fill="black",width=5)
        lein1=screen.create_line(1050,350,1650,900,fill="black",width=5)
        stand=screen.create_rectangle(500,450,1150,550,fill="black")
        stand1=screen.create_rectangle(300,650,1350,750,fill="black")
        stand2=screen.create_rectangle(150,800,1500,950,fill="black")
        side=screen.create_polygon(50,350,50,900,550,350,fill="black")
        side2=screen.create_polygon(1050,350,1650,900,1650,350,fill="black")
        text=screen.create_text(250,275,text="SPACE",fill="white",font="Ariral 50")
        text=screen.create_text(825,275,text="X",fill="white",font="Ariral 50")
        text=screen.create_text(1300,275,text="STATION",fill="white",font="Ariral 50")
        face=screen.create_oval(550,800,600,850,fill="white")
        line=screen.create_line(575,850,575,875,fill="white")
        face=screen.create_oval(800,800,850,850,fill="white")
        screen.create_text(650,900,text="Sir we lost the rocket and my arms and legs",fill="white")
        screen.create_text(900,900,text="YOU DID WHATTTT, well I only have a face",fill="white")


#End of Animation        

        

           

            



       
    


    



    
