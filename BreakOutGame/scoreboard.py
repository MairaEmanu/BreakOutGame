from turtle import Turtle



ALIGNMENT = "center"
FONT_NORMAL = ("Courier", 25, "normal")
FONT_GAME_OVER = ("Courier", 40, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.score = 0

        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0
        except ValueError:
            self.high_score = 0

        self.setposition(x=0, y= 320)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.write(f"Lives: {'❤️'*self.lives} Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT_NORMAL)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            self.reset()
        else:
            self.update()

    def game_over(self):
        self.update()
        self.penup()
        self.hideturtle()
        self.setposition(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_GAME_OVER)