from turtle import Turtle
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]
        self.head.shape("circle")
        self.head.color("black")

    def create_snake(self):
        for i in range(0, 3):
            self.add_seg((i, 0))

    def add_seg(self, i):
        t = Turtle("square")
        t.penup()
        t.goto(i)
        self.seg.append(t)

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            self.seg[i].speed("slow")
            self.seg[i].goto(self.seg[i - 1].xcor(), self.seg[i - 1].ycor())
            if i % 2 == 0:
                self.seg[i].color("white")
            else:
                self.seg[i].color("black")
        self.head.forward(20)

    def extend(self):
        self.add_seg(self.seg[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
