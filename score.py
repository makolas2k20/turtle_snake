# =============================================================================
# Snake game using python turtle module
# Author: Michael Sumaya
# 
# ScoreBoard class
# =============================================================================
from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Arial"
FONT_TYPE = "normal"
COLOR_GAME_OVER = "red"


class ScoreBoard(Turtle):
    def __init__(
            self,
            pos_x: float = 0.0,
            pos_y: float = 0.0,
            size: int = 10,
            color: any = "white",
            shape: str = "classic",
            undobuffersize: int = 1,
            visible: bool = False) -> None:
        super().__init__(
            shape,
            undobuffersize,
            visible)
        self.penup()
        self.speed("fastest")
        self.color(color)
        self.goto(x=pos_x, y=pos_y)
        self.score = 0
        self.size = size
        self._updatescore()

    def _updatescore(self):
        self.clear()
        self.write(
            f"SCORE:    {self.score}",
            move=False,
            align=ALIGNMENT,
            font=(FONT_NAME, self.size, FONT_TYPE)
        )

    def increase_point(self):
        self.score += 1
        self._updatescore()

    def game_over(self):
        self.goto(x=0.0, y=0.0)
        self.color(COLOR_GAME_OVER)
        self.write(
            f"GAME OVER!",
            move=False,
            align=ALIGNMENT,
            font=(FONT_NAME, self.size, FONT_TYPE)
        )