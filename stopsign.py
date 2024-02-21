#Lynda Levy
#CS175L
#Stop sign



#setup
import math #for math.sqrt
import turtle #for drawing
from turtle import * #for commands
turtle.setup(400, 400) #set up window



#define octagon function
def octagon(col, oct_size):
    penup()
    #giving values to color and coordinates
    color(col) #sets color to given color
    goto((x*oct_size), (y*oct_size)) #sets coordinates to center
    fillcolor(col) #sets fill color to given color
    pendown()
    begin_fill() #tells turtle to start filling
    
    #draw 8 lines
    for i in range(0, 8):
        forward(oct_size * 100) #draws line
        right(45) #turns
    end_fill() #tells turtle to stop filling
    penup()



#math to get x and y coordinates:
s = 100
p = s / math.sqrt(2) #pythagorean therom, get x and y length
y = p + 50 #get y distance from center of octagon to top edge
x = -50 #half a side going left



#make octagons shape
octagon("red", 1) #red octagon
octagon("white", 0.925) #white border inside
octagon ("red", 0.825) #red octagon inside



#set up pen for words
penup()
goto(0, -30) #center for words
color("white") #color for words



#print STOP
write("STOP", align='center', font=("Arial", 36, "bold")) #writes word
goto(100, 100) #moves pen out of the way

