from turtle import Screen

from redfood import Redfood #x
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor("green")
screen.title("Snake Game version 1.0")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
redfood=Redfood() #x


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

last_redfood_time = time.time()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with Food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.distance(redfood)<15: #x
        redfood.refresh()
        snake.extend()
        scoreboard.red_food_increase_score()
        last_redfood_time = time.time()


    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()



screen.exitonclick()