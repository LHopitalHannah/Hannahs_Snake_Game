from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink")
screen.title("Hannah's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Now detect the collision with the food
    if snake.head.distance(food) < 17:
        food.refresh()
        # trigger function that adds another segment to snake if they ate food
        snake.extend()
        score_board.increase_score()
        score_board.update_scoreboard()



    #Detect snake head with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset_position()



    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset_position()


screen.exitonclick()
