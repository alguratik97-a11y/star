# Program to draw a star using Turtle graphics

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Draw a Star")

# Create the turtle pen
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)
pen.color("blue")

# Loop to draw a 5-pointed star
for i in range(5):
    pen.forward(150)  # Move forward by 150 pixels
    pen.right(144)    # Turn right by 144 degrees

# Keep the window open
turtle.done()
