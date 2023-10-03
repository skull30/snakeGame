from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lev = True
        self.level = 1
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.hideturtle()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

    def select_level(self):
        self.goto(0, 0)
        self.write("LEVELS: 1 :EASY 2: MEDIUM 3: HARD ", align="center", font=("Arial", 20, "normal"))

    def level_1(self):
        self.level = 1
        self.lev = False

    def level_2(self):
        self.level = 2
        self.lev = False

    def level_3(self):
        self.level = 3
        self.lev = False








