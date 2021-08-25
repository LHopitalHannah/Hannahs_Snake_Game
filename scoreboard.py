from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}     High Score: {self.high_score} ", move=False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
