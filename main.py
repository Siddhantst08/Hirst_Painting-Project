# import colorgram
import turtle
from turtle import Turtle, Screen
from random import *

turtle.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)

# colors_required = 10
# colors = colorgram.extract('img.jpg', colors_required)
#
#
# def rgb_fun():
#     rgb_list = []
#     for _ in range(colors_required):                      #Color Extraction From 'img.jpg' Code !!!
#         rgb = colors[_].rgb
#         red = rgb.r
#         green = rgb.g
#         blue = rgb.b
#         rgb_tuple = (red, green, blue)
#         rgb_list.append(rgb_tuple)
#     return rgb_list
#
#
# print(rgb_fun())

color_list = [(246, 243, 239), (247, 241, 244), (202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244),
              (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22)]

timmy.penup()
timmy.setpos(-250, -250)
y_cord = -250
for _ in range(10):
    for _ in range(10):
        random_color = choice(color_list)
        timmy.forward(50)
        timmy.dot(20, random_color)
    y_cord += 50
    timmy.setpos(-250, y_cord)


# DRAW A SQUARE CODE
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# Draw Dashed lines
# timmy.forward(10)
#
# for _ in range(15):
#     timmy.penup()
#     timmy.forward(10)
#
#     timmy.pendown()
#     timmy.forward(10)


# DRAW PATTERN CODE
# for _ in range(3, 11):
#     timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     for i in range(_):
#         timmy.forward(100)
#         timmy.right(360/_)


# DRAW A WAlK CODE
# timmy.pensize(10)
# timmy.speed(0)
#
#
# directions = [90, 270, 0, 180]
#
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     random_c = (r, g, b)
#     return random_c
#
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.right(choice(directions))


# DRAW SPIROGRAPH CODE
# timmy.speed(0)
#
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     random_c = (r, g, b)
#     return random_c
#
#
# angle = 0
# gap_size = 5
# for _ in range(int(360 / gap_size)):
#     timmy.color(random_color())
#     timmy.circle(100)
#     angle += gap_size
#     timmy.setheading(angle)


screen = Screen()
screen.exitonclick()

