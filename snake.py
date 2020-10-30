# imports
from turtle import *
import random
from freegames import square, vector
import time
# vectors that dictate the positions of the food, the snake, and where the snake goes
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
flag = False
# dictionary that contains 5 different colors
color = {1 : 'black', 2 : 'blue', 3 : 'green', 4 : 'orange', 5 : 'yellow'}	

# variables that keep the key for the dictionary
fKey = random.randint(1, 5)
sKey = random.randint(1, 5)

# makes sure that both keys are not the same
while sKey == fKey:
    sKey = random.randint(1, 5)

# color variables
foodC = color[fKey]
snakeC = color[sKey]

# moves the snake by changing the associated vector
def change(x, y):
    aim.x = x
    aim.y = y

# checks the position of the head item to see whether it is within the boundaries
# returns a boolean
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

#checks if the snake is inside the food square
def insidef(head):
    return food.x-8 < head.x < food.x+8 and food.y-8 < head.y < food.y+8

#determines if the food is inside the boundaries
def foodib(food):
    return -200 < food.x < 190 and -200 < food.y < 190

#moves food randomly given its position
def mf():
    x = random.randrange(-5,5,1)
    y = random.randrange(-5,5,1)
    food.x = food.x + x
    food.y = food.y + y
# the function that actually moves the snake
def move():
	# moves the snake itself
    head = snake[-1].copy()
    head.move(aim)

    #moves food in case it touches the boundaries
    if not foodib(food):
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10

	# checks the position of the head within the boundaries or inside 
	# the snake's body to see if it's dead
	# ends the game if it's dead
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

	# checks the position of the head to see if it has eaten food, which then
	# changes the food's position and elongates the snake
	# if not, it eliminates the tail item to keep the snake the same size
    if insidef(head):
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

	# visualizes each item in the snake array with the color snakeC
    for body in snake:
        square(body.x, body.y, 9, snakeC)
	
	# visualizes the food with the color foodC
    mf()
    square(food.x, food.y, 9, foodC)
    update()
    ontimer(move, 100)

# start up the game, set up the space
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# does the associated lambda function when an arrow key is pressed
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# the actual part that runs
move()
done()
