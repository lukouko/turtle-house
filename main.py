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

# Colour constants
FRONT_WALL_COLOUR = 'dark sea green'
FRONT_ROOF_COLOUR = 'dark sea green'
SIDE_ROOF_COLOUR = 'bisque4'

# Setup the turtle
t = turtle.Turtle()
t.speed(3) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

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


turtle.exitonclick()
