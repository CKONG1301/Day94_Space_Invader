import turtle, random
from turtle import Turtle


X_LEFT = -280
X_RIGHT = 280
X_DISTANCE = 20
Y_TOP = 160
Y_BOTTOM = -150
Y_DISTANCE = 20
Y_CHANGE = 10
turtle.addshape('alienA.gif', shape=None)
turtle.addshape('alienB.gif', shape=None)
turtle.addshape('alienship.gif', shape=None)

# Alien class
class Alien(Turtle):
    def __init__(self):
        self.aliens = []
        self.x_change = 10
        self.type = 0
        self.y_level_down = False
        
    # Add alien type A.
    def add_alienA(self, position):
        new_alien = Turtle('alienA.gif')
        new_alien.penup()
        new_alien.goto(position)
        new_alien.type = 10
        self.aliens.append(new_alien)

    # Add alien type B.
    def add_alienB(self, position):
        new_alien = Turtle('alienB.gif')
        new_alien.penup()
        new_alien.goto(position)
        new_alien.type = 20
        self.aliens.append(new_alien)

    # Build aliens crew.
    def build_aliens(self):
        new_x = X_LEFT
        new_y = Y_TOP
        for m in range(2):
            for n in range(8):
                self.add_alienB((new_x, new_y))
                new_x += X_DISTANCE
            new_x = X_LEFT
            new_y -= Y_DISTANCE
        for m in range(2):
            for n in range(8):
                self.add_alienA((new_x, new_y))
                new_x += X_DISTANCE
            new_x = X_LEFT
            new_y -= Y_DISTANCE
            
    def x_move(self):
        bomb_position = []
        bounce = False
        new_y = 0
        for alien in self.aliens:
            new_x = alien.xcor() + self.x_change
            new_y = alien.ycor()
            if new_x < X_LEFT or new_x > X_RIGHT:
                bounce = True
            alien.goto(new_x, new_y)
            # Drop bomb randomly.
            if random.randint(1, 100) == 1:
                bomb_position.append((new_x, new_y))
        # Do bounce and y level shift after all aliens position changed.
        if bounce:
            if self.y_level_down:
                self.y_level_down = False
                for alien in self.aliens:
                    new_x = alien.xcor()
                    new_y = alien.ycor() - Y_CHANGE
                    alien.goto(new_x, new_y)
            bounce = False
            self.bounce_x()
        # When alien too low, game over.
        return new_y < Y_BOTTOM, bomb_position
    
    def y_move(self):
        self.y_level_down = True
        
    def bounce_x(self):
        self.x_change *= -1

    def reset(self):
        self.x_change = 10
        self.y_level_down = False
        for alien in self.aliens:
            alien.hideturtle()
        self.aliens.clear()
        self.build_aliens()


# Alienship class
class AlienShip(Turtle):
    def __init__(self):
        super().__init__()
        self.type = 30
        self.create_ship()
        self.reset()
        
    def create_ship(self):
        self.shape("alienship.gif")
        self.hideturtle()
        self.setheading(0)
        self.penup()
        self.speed(3)
  
    def move(self):
        if self.xcor() < 300:
            self.forward(5)
        else:
            self.hideturtle()
            
    def reset(self):
        self.goto((X_LEFT, Y_TOP + 20))
        self.hideturtle()
    
        