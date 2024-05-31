import turtle
from turtle import Turtle, Screen
import random

def draw_finish_line(turtle, x, start_y, end_y, segment_height, colors):
    turtle.penup()
    turtle.goto(x, start_y)
    turtle.pendown()
    turtle.width(10)  # Set the thickness of the line
    current_y = start_y
    color_index = 0

    while current_y < end_y:
        turtle.color(colors[color_index])
        turtle.begin_fill()
        turtle.goto(x, current_y + segment_height)
        turtle.goto(x + 10, current_y + segment_height)  # Extend the line thickness horizontally
        turtle.goto(x + 10, current_y)
        turtle.goto(x, current_y)
        turtle.end_fill()
        current_y += segment_height
        color_index = (color_index + 1) % len(colors)


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles_list.append(new_turtle)


finish_line = Turtle()
draw_finish_line(finish_line, x=220, start_y=-200, end_y=200, segment_height=20, colors=["black", "white"])
finish_line.hideturtle()

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
