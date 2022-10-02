import turtle
from turtle import Turtle

X_START = -230
Y_START = -60
X_GAP = 50

class Block(Turtle):
    def __init__(self):
        self.blocks = []
        self.build_blocks()

    # Build blocks crew.
    def build_blocks(self):
        x = X_START
        y = Y_START
        for l in range(5):
            for m in range(5):
                for n in range(5):
                    new_block = Turtle('square')
                    new_block.color('white')
                    new_block.shapesize(0.5, 0.5)
                    new_block.penup()
                    new_block.goto(x, y)
                    self.blocks.append(new_block)
                    y -= 10
                x += 10
                y = Y_START
            x += X_GAP
            y = Y_START
      
    def reset(self):
        for block in self.blocks:
            block.hideturtle()
        self.blocks.clear()
        self.blocks = []
        self.build_blocks()
        