# imports
from random import randrange
from turtle import *
from freegames import vector

# vectors for the proyectile and its speed
ball = vector(-200, -200)
speed = vector(0, 0)

# array where the targets are stored
targets = []

# checks whether there is a click
def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
	
	# determines the x speed of the proyectile
        speed.x = (x + 400) / 25 
        
	# determines the y speed of the proyectile
        speed.y = (y + 400) / 25 

# checks whether xy is within the boundaries
def inside(xy):
    return -200 < xy.x < 200 

# draws the proyectile and the targets
def draw():
    clear()

    # draws every target with blue
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # draws the proyectile if its within the boundaries
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# movement of the proyectile and the targets
def move():
    # creates a target on the right side of the screen at a random altitude
    if randrange(40) == 0:
        y = randrange(-150,150 ) 
        target = vector(200, y) 
        targets.append(target)

    # determines horizontal velocity of targets
    for target in targets:
        target.x -= 1.0 

    # while the ball is within the boundaries, its vertical velocity decreases
    if inside(ball):
        speed.y -= 0.70
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    # if there are targets on the left, return them to the list
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    
    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

# setting up the space
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)

# checks for clicks
onscreenclick(tap)

# game running
move()
done()
