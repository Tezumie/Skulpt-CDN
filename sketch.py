import turtle

# Set up the screen
turtle.setup(750, 830)
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# List of colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Number of circles
n = 36

# Draw the pattern
for i in range(n):
    t.color(colors[i % len(colors)])
    t.circle(100)
    t.right(360 / n)

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
