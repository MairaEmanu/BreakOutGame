from turtle import Turtle

# borders for the paddle

LEFT = 360
RIGHT = 180
HOME_POS = (0,-250)
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color("#F9F7F7")
        self.penup()
        self.speed("fastest")
        self.setposition(HOME_POS)


    def move_right(self):
        new_x = self.xcor() + 30
        self.setposition(x=new_x, y=self.ycor())


    def move_left(self):
        new_x = self.xcor() - 30
        self.setposition(x=new_x, y=self.ycor())

    def missed_ball(self):
        self.setposition(HOME_POS)