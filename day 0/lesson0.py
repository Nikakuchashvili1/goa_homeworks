from turtle import *


#we want to paint a hose


#step 1: draw a square

width(7)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square


#drawing a door
begin_fill()
forward(70) 
color("green")
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()
color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows
begin_fill()
penup()
goto(10, 130)
pendown()
left(210)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

begin_fill()
penup()
goto(140, 130)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()



exitonclick()