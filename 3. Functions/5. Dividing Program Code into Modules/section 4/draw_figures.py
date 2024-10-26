###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

figures.pen.speed(5) 

startingPos = -375

figures.pen.penup()
figures.pen.goto(startingPos, 0)
figures.pen.pendown()

## Draw figures
for i in range(1, 7):
  if i < 3:
    figures.draw_square(100)
  if i >= 3 and i < 5:
    figures.draw_rectangle(100, 50)
  if i >= 5 and i < 7:
    figures.draw_triangle(100)
  figures.pen.penup()
  figures.pen.goto(startingPos + (125 * i), 0)
  figures.pen.pendown()

# Hide the turtle and finish
figures.pen.hideturtle()
window.mainloop()