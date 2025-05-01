#these are beautiful patterns drawn using a turtle in python
import turtle

for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)
turtle.exitonclick()

#this is to draw a simple square.
for i in range(0,4):
    turtle.forward(50)
    turtle.right(90)
turtle.exitonclick()   

#this is to draw an equilateral triangle
for i in range(0,3):
    turtle.forward(100)
    turtle.right(120)
turtle.exitonclick()    

#this is to draw a circle
for i in range(0,360):
    turtle.forward(1)
    turtle.right(1)
turtle.exitonclick() 


import turtle
#this is to draw a five pointed star
for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()          