# thanksjotform
This code uses the turtle graphics library in Python to create a text. The text consists of a red bordered rectangle filled with red color, and a yellow text that says "Thanks Jotform".

Explanation of the code:

1.Import the turtle library using import turtle.
2.Create a turtle object using t = turtle.Turtle().
3.Set the animation speed of the turtle object using t.speed(10).
4.Set the color of the pen and the size of the pen using t.color("red") and t.pensize(3).
5.Start filling the shape with color using t.begin_fill().
6.Draw the rectangle by repeatedly moving forward and turning right by 90 degrees using a for loop and the t.forward() and t.right() methods.
7.End filling the shape with color using t.end_fill().
8.Lift the pen off the screen using t.penup().
9.Set the text color to yellow using t.color("yellow").
10.Move the turtle object to the desired position using t.goto(0, 15).
11.Write the text using t.write(), specifying the text, alignment, font, and font size.
12.Hide the turtle using t.hideturtle().
13.Set the background color of the turtle screen to red using turtle.Screen().bgcolor("red").
14.Display the turtle graphics window using turtle.done(). 
