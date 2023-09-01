from turtle import Turtle

PACE = 5
START_POSITION = (0, - 270)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)
        self.showturtle()

    def go_forward(self):
        self.forward(PACE)

    def go_backward(self):
        self.backward(PACE)

    def reach_the_end(self):
        if self.ycor() >= 260:
            return True
        return False

    def reset_player(self):
        self.hideturtle()
        self.goto(START_POSITION)
        self.showturtle()
