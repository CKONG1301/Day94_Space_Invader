from turtle import Turtle
import turtle

Y_TOP = 180
Y_START = -150
Y_DISTANCE = 10
Y_BOTTOM = -160
turtle.addshape('bomb.gif', shape=None)


# Inherit Turtle's method
class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.bullets = []
    
    def create_bullet(self, x_pos):
        new_bullet = Turtle('square')
        new_bullet.shapesize(0.4, 0.1)
        new_bullet.color("red")
        new_bullet.penup()
        new_bullet.goto(x_pos, Y_START)
        self.bullets.append(new_bullet)

    def move(self):
        for bullet in self.bullets:
            new_x = bullet.xcor()
            new_y = bullet.ycor() + Y_DISTANCE
            bullet.goto(new_x, new_y)
            # Hide bullet that missed alien.
            if new_y > Y_TOP:
                bullet.hideturtle()
                self.bullets = [item for item in self.bullets if item != bullet]
                
    def reset(self):
        # Hide all bullets.
        for bullet in self.bullets:
            bullet.hideturtle()
        # Clear bullet list.
        self.bullets.clear()


# Inherit Turtle's method
class Bomb(Turtle):
    def __init__(self):
        super().__init__()
        self.bombs = []
    
    def create_bomb(self, position):
        new_bomb = Turtle('bomb.gif')
        new_bomb.penup()
        new_bomb.goto(position)
        self.bombs.append(new_bomb)
    
    def move(self):
        for bomb in self.bombs:
            new_x = bomb.xcor()
            new_y = bomb.ycor() - Y_DISTANCE
            bomb.goto(new_x, new_y)
            # Hide bomb that missed flighter.
            if new_y < Y_BOTTOM:
                bomb.hideturtle()
                self.bombs = [item for item in self.bombs if item != bomb]
                
    def reset(self):
        # Hide all bombs.
        for bomb in self.bombs:
            bomb.hideturtle()
        # Clear bomb list.
        self.bombs.clear()
        