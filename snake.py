from turtle import Turtle
coordinates = [(0,0), (-20,0), (-40,0)]
snake_list = []

class Snake():
    def __init__(self):
        for position in coordinates:
            self.create_snake(position)

    def create_snake(self, position):
        snake = Turtle()
        snake.penup()
        snake.goto(position)
        snake.shape("square")
        snake.fillcolor("white")
        snake_list.append(snake)
        
    def extend_snake(self):
        self.create_snake(snake_list[-1].position())
    
    
    def move(self):
        for seg in range(len(snake_list)-1, 0, -1):
            x_new = snake_list[seg-1].xcor()
            y_new = snake_list[seg-1].ycor()
            snake_list[seg].goto(x_new, y_new)
        snake_list[0].forward(20)
    def up(self):
        for seg in range(len(snake_list)-1, 0, -1):
            x_new = snake_list[seg-1].xcor()
            y_new = snake_list[seg-1].ycor()
            snake_list[seg].goto(x_new, y_new)
        snake_list[0].setheading(90)
        snake_list[0].forward(20)
    
    def down(self):
        for seg in range(len(snake_list)-1, 0, -1):
            x_new = snake_list[seg-1].xcor()
            y_new = snake_list[seg-1].ycor()
            snake_list[seg].goto(x_new, y_new)
        snake_list[0].setheading(270)
        snake_list[0].forward(20)
    def left(self):
        for seg in range(len(snake_list)-1, 0, -1):
            x_new = snake_list[seg-1].xcor()
            y_new = snake_list[seg-1].ycor()
            snake_list[seg].goto(x_new, y_new)
        snake_list[0].setheading(180)
        snake_list[0].forward(20)
    def right(self):
        for seg in range(len(snake_list)-1, 0, -1):
            x_new = snake_list[seg-1].xcor()
            y_new = snake_list[seg-1].ycor()
            snake_list[seg].goto(x_new, y_new)
        snake_list[0].setheading(0)
        snake_list[0].forward(20)