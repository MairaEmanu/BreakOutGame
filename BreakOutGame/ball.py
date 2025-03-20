from turtle import Turtle

HOME_POS = (0, -230)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#F9F7F7")
        self.penup()
        self.setposition(HOME_POS)

        self.move_y = 10
        self.move_x = 10

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.setposition(x=new_x, y=new_y)

    def bounce_x(self):
        self.move_x *= -1


    def bounce_y(self):
        self.move_y *= -1


    def miss(self):
        self.setposition(HOME_POS)
        self.move_y *= -1


    def increase_speed(self):
        self.move_y *= 1.25
        self.move_x *= 1.25
