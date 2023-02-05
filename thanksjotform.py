import turtle

t = turtle.Turtle()
t.speed(10)
t.color("red")
t.pensize(3)
t.penup()
t.color("yellow")
t.goto(0, 15)
t.write("Thanks Jotform", align="center", font=("Arial", 67, "bold", ))
t.hideturtle()

turtle.Screen().bgcolor("red")
turtle.done()
