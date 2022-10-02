from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 12, 'bold')
Y_BOTTOM = -160


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()
        
    def read_score(self):
        with open('score.txt') as file:
            return int(file.read())
        
    def write_score(self, high_score):
        with open('score.txt', 'w') as file:
            file.write(str(high_score))
            
    def increase_score(self, m):
        self.score += m
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0, y=180)
        self.write(f"Score: {self.score}   High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def game_over(self, game_over):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score(self.high_score)
        self.goto(0, 0)
        if game_over:
            self.color('red')
            self.write("GAME OVER", False, ALIGNMENT, FONT)
        else:
            self.color('green')
            self.write("MISSION COMPLETED!", False, ALIGNMENT, FONT)
        self.start_game()
        
    def reset(self):
        self.score = 0
        self.update_scoreboard()
        
    def start_game(self):
        self.color('white')
        self.goto(0, Y_BOTTOM )
        self.write("Hit <SPACE> bar to start new game!", False, ALIGNMENT, FONT)
