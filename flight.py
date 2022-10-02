import turtle
from turtle import Turtle


X_LEFT = -280
X_RIGHT = 280
Y_BOTTOM = -180
Y_START = -160
MOVE_DISTANCE = 10
NUM_FLIGHTERS = 3
turtle.addshape('flighter.gif', shape=None)


class Flight(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.x_change = 10
        self.flights = []
        # self.build_flights()
        
    # Build flighter crew.
    def build_flights(self):
        for n in range(NUM_FLIGHTERS):
            new_x = X_LEFT + (NUM_FLIGHTERS - n - 1) * 20
            new_flight = Turtle('flighter.gif')
            new_flight.penup()
            new_flight.goto(new_x, Y_BOTTOM)
            self.flights.append(new_flight)
    
    # Move the flighter with keypress.
    def move_left(self):
        if self.flights[0].xcor() > X_LEFT:
            self.flights[0].setheading(180)
            self.flights[0].forward(MOVE_DISTANCE)
    
    def move_right(self):
        if self.flights[0].xcor() < X_RIGHT:
            self.flights[0].setheading(0)
            self.flights[0].forward(MOVE_DISTANCE)

    def remove(self):
        self.flights[0].hideturtle()
        self.flights.pop(0)
        if len(self.flights) > 0:
            self.flights[0].goto(0, Y_START)
        return len(self.flights) == 0
        
    def reset(self):
        for flight in self.flights:
            flight.hideturtle()
        self.flights.clear()
        self.build_flights()
        self.flights[0].goto(0, Y_START)
        