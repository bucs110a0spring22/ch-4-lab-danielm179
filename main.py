import turtle
import math
from turtle import *
import matplotlib.pyplot as plt
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def test():
  y = math.sin(math.radians(90))
  print(y)
test()


def drawSineCurve():
  for num in range(-360,360):   
    for i in range(num):
      turt_one = turtle.Turtle()
      turt_one = turtle.down()
      x = math.sin(math.radians(i))
      turt_one = turtle.goto(num,num)
      turt_one = turtle.speed(110)
drawSineCurve()

def setupWindow(mywindow=None):
  sc = turtle.Screen()
  sc.mode('world')
  turtle.setworldcoordinates(-400,-400,400,400)
setupWindow()

def setupAxis(myturtle=None):
  x = [-400, 0, 400]
  y = [-400, 0, 400]
  turtle.set(0,0)
setupAxis()

def drawCosineCurve():
  for num in range(-360,360):   
    for i in range(num):
      turt_two = turtle.Turtle()
      turt_two = turtle.down()
      x = math.cos(math.radians(i))
      turt_two = turtle.goto(num,num)
      turt_two = turtle.speed(110)
drawCosineCurve()

def drawTangentCurve():
  for num in range(-360,360):   
    for i in range(num):
      turt_three = turtle.Turtle()
      turt_three = turtle.down()
      x = math.tan(math.radians(i))
      turt_three = turtle.goto(num,num)
      turt_three = turtle.speed(110)
drawTangentCurve()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    wn.exitonclick()


    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()

main()
