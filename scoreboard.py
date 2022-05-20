from tkinter import TOP
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier" , 12 , "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.pendown()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write("Game Over..", align=ALIGNMENT, font=FONT)
        
        