from turtle import Turtle

OUT_OF_FRAME = (-700, -900)
COLORS = {1 : "#FFDFD6", 2 : "#E3A5C7", 3: "#B692C2", 4: "#694F8E"}

class Brick(Turtle):
    def __init__(self, color, x,y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=5)
        self.color(color)
        self.penup()
        self.setposition((x,y))

        #borders of bricks
        self.left = self.xcor() - 55
        self.right =  self.xcor() + 55
        self.upper = self.ycor() + 20
        self.bottom = self.ycor() - 20


    def remove(self):
        self.goto(OUT_OF_FRAME)


class Bricks:
    def __init__(self):
        y_start = 270
        key = 1

        self.bricks = []
        self.create_all_rows(y=y_start,colors=COLORS, key=key)


    def create_row(self,y, color):
        for i in range(-340, 430, 110):
            brick = Brick(color=color, x=i, y=y)
            self.bricks.append(brick)

    def create_all_rows(self,y, colors , key):
        for i in range(4):
            self.create_row(y=y, color=colors[key])
            y -= 40
            key += 1





