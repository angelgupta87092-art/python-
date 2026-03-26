import turtle

# Create a turtle
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(2)

# Draw Square
pen.color("blue")
pen.penup()
pen.goto(-200, 100)  # Position for square
pen.pendown()
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Draw Rectangle
pen.color("green")
pen.penup()
pen.goto(0, 100)  # Position for rectangle
pen.pendown()
for _ in range(2):
    pen.forward(150)
    pen.right(90)
    pen.forward(80)
    pen.right(90)

# Draw Circle
pen.color("red")
pen.penup()
pen.goto(150, -20)  # Position for circle
pen.pendown()
pen.circle(50)

# Hide the turtle and keep the window open
pen.hideturtle()
screen.mainloop()
