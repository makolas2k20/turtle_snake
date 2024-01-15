# =============================================================================
# Snake game using python turtle module
# Author: Michael Sumaya
# =============================================================================

import time
from turtle import Screen
from snake import Snake
from food import SnakeFood
from score import ScoreBoard

KEY_RIGHT = "Right"
KEY_UP = "Up"
KEY_LEFT = "Left"
KEY_DOWN = "Down"
KEY_EXIT = "x"
KEY_NEW = "y"

MAX_WIDTH = 600
MAX_HEIGHT = 600

screen = Screen()
screen.setup(
    width=MAX_WIDTH,
    height=MAX_HEIGHT,
)
screen.bgcolor("black")
screen.title("SNAKES!")
screen.tracer(0)
screen.colormode(255)

# Main Game
snake = Snake(
    screen_x=(MAX_WIDTH // 2),
    screen_y=(MAX_HEIGHT // 2) - 20,
    speed=0.05,
    is_walled=False,
    is_running=True
)

screen.listen()
screen.onkeypress(fun=snake.snake_right, key=KEY_RIGHT)
screen.onkeypress(fun=snake.snake_up, key=KEY_UP)
screen.onkeypress(fun=snake.snake_left, key=KEY_LEFT)
screen.onkeypress(fun=snake.snake_down, key=KEY_DOWN)
screen.onkeypress(fun=screen.bye, key=KEY_EXIT)

food = SnakeFood(
    screen_x=(MAX_WIDTH // 2),
    screen_y=(MAX_HEIGHT // 2) - 20,
)

scoreboard = ScoreBoard(
    pos_y=(MAX_HEIGHT // 2) - 20,
    size=10,
    color="yellow"
)

while snake.is_running:
    try:
        snake.is_running = snake.snake_forward()
        if snake.head.distance(food) < 10:
            food.regen()
            snake.snake_grow()
            scoreboard.increase_point()
        screen.update()
        time.sleep(snake.speed)
    except Exception as error_:
        print(f"Error encountered: {error_}")
        snake.is_running = False

scoreboard.game_over()

# Exit
screen.mainloop()
