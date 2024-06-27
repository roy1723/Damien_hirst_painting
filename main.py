# import colorgram
# from colorgram import Color
# colors = colorgram.extract("image.jpg", 6)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color= (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen
from random import Random
turtle.colormode(255)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86),
              (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots = 101
tim.speed("fastest")

for dot_counts in range (1, number_dots):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if dot_counts % 10 == 0:
        tim.penup()
        tim.lt(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = Screen()
turtle.exitonclick()



