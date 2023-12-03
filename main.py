import turtle
import math


# Screen constants
FULL_SCREEN_HEIGHT = turtle.window_height()
FULL_SCREEN_WIDTH = turtle.window_width()
HALF_SCREEN_HEIGHT_FLOORED = turtle.window_height() // 2
HALF_SCREEN_WIDTH_FLOORED = turtle.window_width() // 2

# House distance constants
FRONT_WALL_WIDTH = HALF_SCREEN_WIDTH_FLOORED
FRONT_WALL_HEIGHT = math.floor(FULL_SCREEN_HEIGHT * 0.31)
SIDE_WALL_WIDTH = math.floor(FRONT_WALL_WIDTH / 4)
SIDE_WALL_HEIGHT = FRONT_WALL_HEIGHT

FRONT_DOOR_WIDTH = math.floor(FRONT_WALL_WIDTH / 4)
FRONT_DOOR_HEIGHT = math.floor(FRONT_WALL_HEIGHT / 2)
FRONT_WINDOW_SIZE = (FRONT_WALL_HEIGHT / 4)

# Colour constants
FRONT_WALL_COLOUR = 'dark sea green'
FRONT_ROOF_COLOUR = 'dark sea green'
SIDE_ROOF_COLOUR = 'bisque'
FRONT_DOOR_COLOUR = 'sandy brown'
FRONT_DOOR_BORDER = 'snow2'

# Setup the turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest


#########################################################
# DRAW BACKGROUND
#########################################################
skyStartX = -HALF_SCREEN_WIDTH_FLOORED
skyStartY = HALF_SCREEN_HEIGHT_FLOORED

# Sky
t.penup()
t.goto(skyStartX, skyStartY)
t.fillcolor('honeydew')
t.setheading(0)
t.begin_fill()
t.forward(FULL_SCREEN_WIDTH)
t.right(90)
t.forward(HALF_SCREEN_HEIGHT_FLOORED)
t.right(90)
t.forward(FULL_SCREEN_WIDTH)
t.right(90)
t.forward(HALF_SCREEN_HEIGHT_FLOORED)
t.end_fill()

# Ground
groundStartX = -HALF_SCREEN_WIDTH_FLOORED
groundStartY = 0

t.penup()
t.goto(groundStartX, groundStartY)
t.fillcolor('snow2')
t.setheading(0)
t.begin_fill()
t.forward(FULL_SCREEN_WIDTH)
t.right(90)
t.forward(HALF_SCREEN_HEIGHT_FLOORED)
t.right(90)
t.forward(FULL_SCREEN_WIDTH)
t.right(90)
t.forward(HALF_SCREEN_HEIGHT_FLOORED)
t.end_fill()

#########################################################
# DRAW WALLS
##########################################################
 
# Calculate the starting point for the wall drawing.
# We take take the decimal floor to ensure whole numbers.
frontWallStartX = math.floor(turtle.window_width() / 4)
frontWallStartY = math.floor(turtle.window_height() / 2)

# Convert to 0 centre coordinates
frontWallStartX = frontWallStartX - HALF_SCREEN_WIDTH_FLOORED
frontWallStartY = frontWallStartY - HALF_SCREEN_HEIGHT_FLOORED

# Move turtle to wall starting point.
t.up()
t.goto(frontWallStartX, frontWallStartY)
t.setheading(0)

# Draw front wall
t.fillcolor(FRONT_WALL_COLOUR)
t.begin_fill()

t.down()
t.forward(FRONT_WALL_WIDTH)

t.right(90)
t.forward(FRONT_WALL_HEIGHT)

t.right(90)
t.forward(FRONT_WALL_WIDTH)

t.right(90)
t.forward(FRONT_WALL_HEIGHT)

t.end_fill()

# Draw side wall
t.up()
t.right(90)

t.forward(FRONT_WALL_WIDTH)

t.down()

t.begin_fill()
t.left(45)
t.forward(SIDE_WALL_WIDTH)

roofSideEndX = t.xcor()
roofSideEndY = t.ycor()

t.right(135)
t.forward(SIDE_WALL_HEIGHT)

t.right(45)
t.forward(SIDE_WALL_WIDTH)

t.right(135)
t.forward(SIDE_WALL_HEIGHT)

t.end_fill()

#########################################################
# DRAW ROOF
##########################################################

# Calculate the starting point for the ceiling drawing.
# We take take the decimal floor to ensure whole numbers.
frontRoofStartX = math.floor(turtle.window_width() / 4)
frontRoofEndX = math.floor(frontRoofStartX + FRONT_WALL_WIDTH)

frontRoofMiddleX = math.floor(frontRoofStartX + (FRONT_WALL_WIDTH / 2))
frontRoofStartY = math.floor(turtle.window_height() / 2)

# Convert to 0 centre coordinates
frontRoofMiddleX = frontRoofMiddleX - HALF_SCREEN_WIDTH_FLOORED
frontRoofEndX = frontRoofEndX - HALF_SCREEN_WIDTH_FLOORED
frontRoofStartX = frontRoofStartX - HALF_SCREEN_WIDTH_FLOORED
frontRoofStartY = frontRoofStartY - HALF_SCREEN_HEIGHT_FLOORED

# Roof distances
roofHeight = math.floor(FULL_SCREEN_HEIGHT * 0.4)

# Move turtle to wall starting point.
t.up()
t.goto(frontRoofMiddleX, frontRoofStartY)
t.setheading(90)

t.forward(roofHeight)
topOfRoofX = t.xcor()
topOfRoofY = t.ycor()

# Draw the front of the roof.
t.begin_fill()
t.fillcolor(FRONT_ROOF_COLOUR)

t.down()
t.goto(frontRoofStartX, frontRoofStartY)
t.goto(frontRoofEndX, frontRoofStartY)
t.goto(topOfRoofX, topOfRoofY)

t.end_fill()

# Draw side roof
t.fillcolor(SIDE_ROOF_COLOUR)
t.begin_fill()

t.setheading(45)
t.forward(SIDE_WALL_WIDTH)

t.goto(roofSideEndX, roofSideEndY)
t.goto(frontRoofEndX, frontRoofStartY)
t.goto(topOfRoofX, topOfRoofY)
t.end_fill()

# Draw cladding on front and side wall
t.penup()
t.goto(frontWallStartX, frontWallStartY)
t.setheading(0)
t.pendown()

amountOfCladding = 12
gapBetweenCladding = FRONT_WALL_HEIGHT / amountOfCladding

currentCladdingY = frontWallStartY
for count in range(amountOfCladding):
  t.forward(FRONT_WALL_WIDTH)
  t.left(45)
  t.forward(SIDE_WALL_WIDTH)
 
  currentCladdingY = currentCladdingY - gapBetweenCladding
 
  t.penup()
  t.goto(frontWallStartX, currentCladdingY)
  t.setheading(0)
  t.pendown()

# Draw front door
frontDoorStartX = math.floor(frontWallStartX + (FRONT_WALL_WIDTH / 2) - (FRONT_DOOR_WIDTH / 2))
frontDoorStartY = frontWallStartY - FRONT_WALL_HEIGHT
t.goto(frontDoorStartX, frontDoorStartY)
t.setheading(90)
t.fillcolor(FRONT_DOOR_COLOUR)
t.begin_fill()
t.forward(FRONT_DOOR_HEIGHT)
t.right(90)
t.forward(FRONT_DOOR_WIDTH)
t.right(90)
t.forward(FRONT_DOOR_HEIGHT)
t.right(90)
t.forward(FRONT_DOOR_WIDTH)
t.end_fill()

#Draw windows
def draw_window(t, x, y, colour, size):
  t.penup()
  t.goto(x, y)
  t.setheading(0)
  t.pendown()
  t.fillcolor(colour)
  t.pencolor(colour)
  t.begin_fill()
  for count in range(4):
    t.forward(size)
    t.right(90)
  t.end_fill()
  t.penup()

def draw_window_details(t, x, y, windowSize, colour, penSize):
  # Draw border around window.
  t.penup()
  t.goto(x, y)
  t.setheading(0)
  t.pencolor(colour)
  t.pensize(penSize)
  t.pendown()

  for count in range(4):
    t.forward(windowSize)
    t.right(90)

  # Draw cross inside window
  t.penup()
  t.goto(math.floor(x + windowSize / 2), y)
  t.setheading(270)
  t.pendown()
  t.forward(windowSize)
  t.penup()
  t.goto(x, math.floor(y - windowSize / 2))
  t.setheading(0)
  t.pendown()
  t.forward(windowSize)

leftWindowStartX = math.floor(frontWallStartX + FRONT_WALL_WIDTH * 0.05)
leftWindowStartY = frontDoorStartY + FRONT_DOOR_HEIGHT

draw_window(t, leftWindowStartX, leftWindowStartY, 'steel blue', FRONT_WINDOW_SIZE)
draw_window_details(t, leftWindowStartX, leftWindowStartY, FRONT_WINDOW_SIZE, 'bisque', 4)

rightWindowStartX = math.floor(frontWallStartX + FRONT_WALL_WIDTH * 0.95 - FRONT_WINDOW_SIZE)
rightWindowStartY = frontDoorStartY + FRONT_DOOR_HEIGHT

draw_window(t, rightWindowStartX, rightWindowStartY, 'steel blue', FRONT_WINDOW_SIZE)
draw_window_details(t, rightWindowStartX, rightWindowStartY, FRONT_WINDOW_SIZE, 'bisque', 4)

turtle.exitonclick()