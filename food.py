# =============================================================================
# Snake game using python turtle module
# Author: Michael Sumaya
# 
# SnakeFood class
# =============================================================================
import random
from turtle import Turtle


class SnakeFood(Turtle):

    def __init__(
            self,
            screen_x: int,
            screen_y: int,
            shape: str = "circle",
            undobuffersize: int = 1000,
            visible: bool = True) -> None:
        super().__init__(
            shape,
            undobuffersize,
            visible)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.space_x = (screen_x - 20) // 20
        self.space_y = (screen_y - 20) // 20
        random.seed()
        self.regen()

    def regen(self):
        self.color(
            (
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
            ),
        )
        rand_x = random.randint(-self.space_x, self.space_x) * 20
        rand_y = random.randint(-self.space_y, self.space_y) * 20
        self.goto(rand_x, rand_y)
