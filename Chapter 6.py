from graphics import *
win = GraphWin("Light", 500, 500)

def draw_light_body(x, y, length, width):
    black=Rectangle(Point(x,y), Point(width, length))
    black.setFill("black")
    black.setOutline("black")
    black.draw(win)

def draw_lamp(color, x, y, radius):
    lamp = Circle(Point(x,y), radius)
    lamp.setOutline("black")
    lamp.setFill(color)
    lamp.draw(win)

def draw_traffic_light(x, y):
    draw_light_body(x,y,60,120)
    draw_lamp("red", 160, 95, 15)
    draw_lamp("yellow", 160, 130, 15)
    draw_lamp("green", 160, 165, 15)

draw_traffic_light(200,200)
