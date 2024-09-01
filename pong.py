from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, initial_x):
        super().__init__()
        self.create_paddle(initial_x)


    def create_paddle(self, initial_x):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(initial_x, 0)  # Center the paddle vertically

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


