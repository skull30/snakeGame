import time
from snake import Snake
from turtle import Turtle, Screen
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.title("snake game")
screen.bgcolor("green")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.075)
    snake.move()
    if snake.head.distance(food) < 15:
        food.food_refresh()
        score.increase_score()
        snake.extend()

    if int(snake.head.xcor()) > 280 or int(snake.head.xcor()) < -280 or int(snake.head.ycor()) > 280 or int(snake.head.ycor()) < -280:
        game_is_on = False
        score.game_over()

    for j in snake.seg:
        if j == snake.head:
            pass
        elif snake.head.distance(j) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
