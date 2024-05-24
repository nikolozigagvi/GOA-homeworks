from turtle import*


#we want to paint a house

#step 1:   draw a square
speed(10)
width(10)
color("blue")
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)
#end of squere

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120) 
end_fill()

penup()
goto(200, 200)
pendown()


begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
color("grey")

left(30)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

#drawing window lines
 
penup()
goto(0, 170)
pendown()
right(180)
forward(60)

penup()
goto(30, 195)
pendown()
right(90)
forward(60)

#drawing a window 2
color('light blue')
penup()
goto(140, 140)
pendown()
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

#drawing a waindow lines 2

penup()
goto(140, 170)
pendown()
left(90)
forward(60)
penup()
goto(170, 195)
pendown()
right(90)
forward(60)











exitonclick()
