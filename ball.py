from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.x_speed = 10  # Adjust the speed in the x-direction
        self.y_speed = 10  # Adjust the speed in the y-direction

    def move(self):
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)

        # Check if the ball hits the top or bottom of the screen
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_speed *= -1  # This will reverse the direction of the ball

    def increase_speed(self):
        self.x_speed *= 1.5  # You can adjust the multiplier as needed
        self.y_speed *= 1.5

    def reset_speed(self):
        self.x_speed = 10
        self.y_speed = 10

    def bounce_x(self):
        self.x_speed *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()