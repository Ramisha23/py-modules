from turtle import *

class Face:
    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.noseSize = 'small'

    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)

    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        fillcolor("yellow")
        begin_fill()
        circle(self.size)
        end_fill()
        self.goHome()

    def drawEye(self, angle, color="white"):
        penup()
        left(angle)
        forward(self.size / 2)
        pendown()
        dot(self.size / 10, color)
        self.goHome()

    def drawEyebrow(self, angle):
        penup()
        left(angle)
        forward(self.size / 2 + 10)
        pendown()
        width(3)
        forward(20)
        width(1)
        self.goHome()

    def drawMouth(self):
        penup()
        right(135)
        forward(self.size / 1.7)
        left(90)
        pendown()
        width(3)
        circle(self.size / 1.7, 90)
        width(1)
        self.goHome()

    def drawNose(self):
        dot(self.size / 6, "orange")
        self.goHome()

    def draw(self):
        speed(0)
        pensize(3)
        self.drawOutline()
        self.drawEye(135, "blue")
        self.drawEye(45, "blue")
        self.drawEyebrow(135)
        self.drawEyebrow(45)
        self.drawMouth()
        self.drawNose()
        pensize(1)

f1 = Face(0, 0)
f1.draw()

showturtle()
done()