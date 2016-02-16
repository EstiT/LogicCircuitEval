#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

from SimpleGraphics import *  

def main (): 
    a,b,c,d,e=input("Enter either (T)rue or (F)alse five times without spaces: ") 
    Val1,Val2,Val3,Val4,Val5= evaluateMyCircuit(a,b,c,d,e)
    #change the background of the window to white
    background("white") 
     #adjust formatting for text
    setFont("Times","12")
    #draw the logical circut
    drawShapes(a,b,c,d,e,Val1,Val2,Val3,Val4,Val5)


def evaluateMyCircuit(a,b,c,d,e): 
    if a=="T": #if first input value is True
        a=True #assign it to be boolean true
    else: #otherwise
        a=False #assign it to be false
#repeat for each T/F value inputed
    if b=="T": 
        b=True
    else:
        b=False
    if c=="T":
        c=True
    else:
        c=False
    if d=="T":
        d=True
    else:
        d=False
    if e=="T":
        e=True
    else:
        e=False 
#find new values using "not", "and" and "or"           
    Val1=not a 
    Val2= b and c 
    Val3= d or e
    Val4= Val2 or Val3
    Val5= Val1 or Val4
    return Val1,Val2,Val3,Val4,Val5 #return all of the values


def drawShapes(a,b,c,d,e,Val1,Val2,Val3,Val4,Val5):
    #draw 5 circles with the inputed values (T/F) inside of them 
    ellipse(7,129,30,30);text(12,135,a,"nw") 
    ellipse(7,169,30,30);text(12,175,b,"nw")
    ellipse(7,209,30,30);text(12,215,c,"nw")
    ellipse(7,249,30,30);text(12,255,d,"nw")
    ellipse(7,289,30,30);text(12,295,e,"nw")

    setFont("Times","11") #change text formatting
    # draw the AND symbol
    line(65,175,65,235)#Vertical line
    curve(65,175,115,177,135,205,115,232,65,235)#curve 

    #lines near first AND symbol connecting circut 
    line(35,185,65,185)#Horizintal 
    line(35,225,65,225)#H 
    line(130,205,150,205) #H 
    line(175,205,235,205) #H
    line(235,205,235,235)#Vertical

    ellipse(150,195,25,25) #circle with the new value in it after first AND operator
    text(150,200,Val2,"nw") #value displayed inside the circle


    #draw first OR symbol
    line(35,265,78,265)#horizontal line
    line(35,305,80,305)#H line
    curve(65,250,105,290,65,320)#inner cuver
    curve(65,250,198,285,65,320)#outer curve
    line(130,285,150,285)#H line

    ellipse(150,275,25,25)#circle with the new value in it after first OR operator
    text(150,280,Val3,"nw")#True or false inside the circle anchored at north west

    line(175,285,235,285)#lines connecting the circuit
    line(235,285,235,275)

    #draw first NOT symbol
    line(37,139,280,139)#horizontal line
    line(280,109,280,169)#vertical line triangle base
    line(280,109,345,139)#diagonal
    line(345,139,280,169)#diagonal
    line(360,139,370,139)#right horizontal line
    line(369,140,369,205)#vertical line

    ellipse(345,130,25,25)#circle with the new value in it after NOT operator
    text(346,134,Val1,"nw")#Value displayed inside a circle 

    #draw 2nd OR symbol
    line(235,235,278,235)#H line
    line(235,275,280,275)#H line
    curve(265,220,305,260,265,290)#inner cuver
    curve(265,220,398,255,265,290)#outer curve
    line(330,255,350,255)#H line

    ellipse(350,240,25,25)#circle with the new value in it after 2nd OR operator
    text(350,245,Val4,"nw")#value displayed in a circle 

    #draw 3rd OR symbol
    line(369,205,418,205)#H line
    line(374,245,420,245)#H line
    curve(405,190,445,230,405,260)#inner cuver
    curve(405,190,538,225,405,260)#outer curve
    line(470,225,490,225)#H line
    ellipse(490,210,25,25)#circle with the new value in it after 3rd OR operator
    text(490,215,Val5,"nw")#True/false inside the circle anchored at north west

    #black circles at "joints" of circuit wires
    setFill("black") #change the fill to be black
    ellipse(50,136,8,8) #draw all of the circles
    ellipse(50,181,8,8)
    ellipse(50,221,8,8)
    ellipse(50,261,8,8)
    ellipse(50,301,8,8)
    ellipse(231,283,8,8)
    ellipse(231,271,8,8)
    ellipse(231,230,8,8)
    ellipse(231,202,8,8)
    ellipse(365,202,8,8)
    
    
main()