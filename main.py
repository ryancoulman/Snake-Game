from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup the background GUI screen
width, height = 600, 600
seg_length = 20
screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check if the snakes head is touching a food object
    if snake.head.distance(food) < 15:
        food.new_pos()
        scoreboard.increase_score()
        snake.extend()

    # Check if the snake collides with the wall
    if abs(snake.head.xcor()) > width/2-seg_length/2 or abs(snake.head.ycor()) > height/2-seg_length/2:
        scoreboard.reset(screen)
        snake.reset()

    # Check if the snakes head collides with its tail
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset(screen)
            snake.reset()


screen.exitonclick()