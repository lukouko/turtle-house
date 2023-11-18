import turtle
import math

print('Window height is', turtle.window_height());
print('Window width is', turtle.window_width());

# Screen constants
FULL_SCREEN_HEIGHT = turtle.window_height()
FULL_SCREEN_WIDTH = turtle.window_width()
HALF_SCREEN_HEIGHT_FLOORED = turtle.window_height() // 2
HALF_SCREEN_WIDTH_FLOORED = turtle.window_width() // 2

# Setup the turtle
t = turtle.Turtle()
t.speed(3) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

def drawWalls(t):
  # Calculate the starting point for the wall drawing.
  # We take take the decimal floor to ensure whole numbers.
  startX = math.floor(turtle.window_width() / 4)
  startY = math.floor(turtle.window_height() / 2)

  # Convert to 0 centre coordinates
  startX = startX - HALF_SCREEN_WIDTH_FLOORED
  startY = startY - HALF_SCREEN_HEIGHT_FLOORED

  # Wall widths
  frontWallWidth = HALF_SCREEN_WIDTH_FLOORED
  frontWallHeight = math.floor(FULL_SCREEN_HEIGHT * 0.31)
  sideWallWidth = math.floor(frontWallWidth / 4)
  sideWallHeight = frontWallHeight

  # Move turtle to wall starting point.
  t.up()
  t.goto(startX, startY)

  # Draw front wall
  t.down()
  t.forward(frontWallWidth)

  t.right(90)
  t.forward(frontWallHeight)

  t.right(90)
  t.forward(frontWallWidth)

  t.right(90)
  t.forward(frontWallHeight)

  # Draw side wall
  t.up()
  t.right(90)
  t.forward(frontWallWidth)

  t.down()
  t.left(45)
  t.forward(sideWallWidth)

  t.right(135)
  t.forward(sideWallHeight)

  t.right(45)
  t.forward(sideWallWidth)

# Draw house
drawWalls(t)

turtle.exitonclick()
