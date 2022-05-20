from turtle import Screen, Turtle, time
import snake
from scoreboard import Score
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.title("Snake Game")
screen.tracer(0)
scoreboard = Score()

snake_game = snake.Snake()
food = Food()

screen.listen()
screen.onkey(snake_game.up, "Up")
screen.onkey(snake_game.down, "Down")
screen.onkey(snake_game.left, "Left")
screen.onkey(snake_game.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake_game.move()

    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        snake_game.extend_snake()
        scoreboard.increase_score()

    #for collision with wall
    if snake.snake_list[0].xcor() > 230 or snake.snake_list[0].xcor() < -230 or snake.snake_list[0].ycor() > 230 or snake.snake_list[0].ycor() < -230:
        is_game_on = False
        scoreboard.gameOver()

    #for collision with snake's body
    for segment in snake.snake_list[1:]: #slicing
        if snake.snake_list[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.gameOver()












screen.exitonclick()