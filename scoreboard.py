from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white") #change the score board color if you need ed to white or black
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GANE OVER !!", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score+=5 #change the score size one increment
        self.clear()
        self.update_scoreboard()

    def red_food_increase_score(self):
        self.score+=10 #change the score size one increment
        self.clear()
        self.update_scoreboard()






