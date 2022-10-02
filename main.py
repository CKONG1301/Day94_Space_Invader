import random
import time
import threading
from turtle import Screen
from flight import Flight
from alien import Alien, AlienShip
from block import Block
from animation import Bullet, Bomb
from scoreboard import Scoreboard


is_continue = True
game_over = True
tick_msec = False
tick_sec = False
first_run = True


# Timer to move invader in y-axis
def timer_y_move():
    global is_continue, tick_sec
    while is_continue:
        time.sleep(10)
        tick_sec = True


# Timer to move invader in x-axis
def timer_x_move():
    global is_continue, tick_msec
    while is_continue:
        time.sleep(0.1)
        tick_msec = True


def move_objects():
    global game_over
    game_over, bomb_position = invader.x_move()
    if game_over:
        score.game_over(game_over)
        unbind_key()
    if shot:
        shot.move()
    for position in bomb_position:
        attack.create_bomb(position)
    attack.move()
    if ship.isvisible():
        ship.move()


def fire():
    global shot
    shot.create_bullet(flight.flights[0].xcor())
    
    
def bind_key():
    global game_over
    game_over = False
    # Setup key press detection.
    screen.onkey(flight.move_left, "Left")
    screen.onkey(flight.move_right, "Right")
    screen.onkey(fire, 'space')
    screen.listen()
    

def unbind_key():
    global game_over
    game_over = True
    screen.onkey(None, "Left")
    screen.onkey(None, "Right")
    screen.onkey(play_game, 'space')
    screen.listen()
    
    
def check_collision():
    global shot, invader
    game_end = False
    # Detect collision between bullet and alien.
    for bullet in shot.bullets:
        for alien in invader.aliens:
            if alien.distance(bullet) < 10:
                score.increase_score(alien.type)
                alien.hideturtle()
                bullet.hideturtle()
                shot.bullets = [item for item in shot.bullets if item != bullet]
                invader.aliens = [item for item in invader.aliens if item != alien]
    # Detect collision between bullet and obstacle.
    for bullet in shot.bullets:
        for block in obstacle.blocks:
            if block.distance(bullet) < 10:
                block.hideturtle()
                bullet.hideturtle()
                shot.bullets = [item for item in shot.bullets if item != bullet]
                obstacle.blocks = [item for item in obstacle.blocks if item != block]
    # Detect collision between bomb and obstacle.
    for bomb in attack.bombs:
        for block in obstacle.blocks:
            if block.distance(bomb) < 10:
                block.hideturtle()
                bomb.hideturtle()
                attack.bombs = [item for item in attack.bombs if item != bomb]
                obstacle.blocks = [item for item in obstacle.blocks if item != block]
    # Detect collision between alien ship and bullets.
    for bullet in shot.bullets:
        if ship.distance(bullet) < 10:
            score.increase_score(ship.type)
            ship.hideturtle()
            bullet.hideturtle()
            shot.bullets = [item for item in shot.bullets if item != bullet]
    # Detect collision between bomb and flight.
    for bomb in attack.bombs:
        if bomb.distance(flight.flights[0]) < 10:
            bomb.hideturtle()
            attack.bombs = [item for item in attack.bombs if item != bomb]
            game_end = flight.remove()
            break
    # Return mission end or not.
    if len(invader.aliens) == 0:
        game_end = True
    return game_end
    
            
def play_game():
    global game_over, timer_x, timer_y, invader
    obstacle.reset()
    flight.reset()
    score.reset()
    invader.reset()
    ship.reset()
    shot.reset()
    attack.reset()
    bind_key()
    # Create timer thread to move alien downward.
    if not timer_y.is_alive():
        timer_y = threading.Thread(target=timer_y_move, name='timerY')
        timer_y.start()
    # Create thread to move invader in x-axis, or bullet in y-axis.
    if not timer_x.is_alive():
        timer_x = threading.Thread(target=timer_x_move, name='timerX')
        timer_x.start()
    
    
screen = Screen()
screen.setup(width=600, height=400)
screen.tracer(0)
screen.title('Space Invader')
screen.bgcolor('black')
# Create game objects.
score = Scoreboard()
obstacle = Block()
invader = Alien()
ship = AlienShip()
flight = Flight()
shot = Bullet()
attack = Bomb()
# Create timers for x-axis move and y-axis move.
timer_x = threading.Thread(target=timer_x_move, name='timerX')
timer_y = threading.Thread(target=timer_y_move, name='timerY')
# Listen only to 'space' key.
screen.onkey(play_game, 'space')
screen.listen()
# Start main loop.
score.start_game()
while is_continue:
    if not game_over:
        if tick_msec:
            # Reset timer.
            tick_msec = False
            move_objects()
        if tick_sec:
            # Reset timer.
            tick_sec = False
            invader.y_move()
            if random.randint(1, 2) == 1 and not ship.isvisible():
                ship.reset()
                ship.showturtle()
        if check_collision():
            if len(flight.flights) == 0:
                game_over = True
            score.game_over(game_over)
            # Prepare to detect 'space'
            unbind_key()
    screen.update()


screen.exitonclick()
