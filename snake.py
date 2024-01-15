# =============================================================================
# Snake game using python turtle module
# Author: Michael Sumaya
# 
# Snake class
# =============================================================================
from turtle import Turtle

DIR_RIGHT = 0
DIR_UP = 90
DIR_LEFT = 180
DIR_DOWN = 270
DOT_WIDTH = 20
START_POS = [
    (0, 0),
    (-DOT_WIDTH, 0),
    (-(DOT_WIDTH*2), 0),
    (-(DOT_WIDTH*3), 0),
]


class Snake():

    def __init__(
            self,
            screen_x: float = 300.0,
            screen_y: float = 300.0,
            speed: float = 0.1,
            is_walled: bool = False,
            is_running: bool = True,
            *args
    ) -> None:
        self.MAX_X = screen_x
        self.MIN_X = -self.MAX_X
        self.MAX_Y = screen_y
        self.MIN_Y = -self.MAX_Y
        self.speed = speed
        self.is_walled = is_walled
        self.is_running = is_running
        self.snake = []
        self.init_snake()
        self.head = self.snake[0]["segment"]

    def init_snake(self):
        '''Snake Segment format
        {
            "segment": Turtle(),
            "coord": (x,y),
            "ishead": True only for first one
        }
        '''
        for pos in START_POS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.snake.append(
                {
                    "segment": new_segment,
                    "coord": pos,
                    "ishead": (True if pos[0] == 0 else False)
                }
            )

    def snake_forward(self) -> bool:
        '''Move the head forward by DOT_WIDTH.
        Body segments follows movement history from front segment.
        '''
        segment_list = self.snake
        is_wall_hit = False
        is_dead = False
        num_segments = len(segment_list) - 1
        for seg_num in range(num_segments, -1, -1):
            # seg_turtle = Turtle()
            seg_turtle = segment_list[seg_num]["segment"]
            if segment_list[seg_num]["ishead"]:
                seg_turtle.forward(DOT_WIDTH)
                x, y = seg_turtle.pos()
                segment_list[seg_num]["coord"] = (x, y)
                # Wall check
                if x >= self.MAX_X:
                    x = self.MIN_X + DOT_WIDTH
                    is_wall_hit = True
                if x <= self.MIN_X:
                    x = self.MAX_X - DOT_WIDTH
                    is_wall_hit = True
                if y >= self.MAX_Y:
                    y = self.MIN_Y + DOT_WIDTH
                    is_wall_hit = True
                if y <= self.MIN_Y:
                    y = self.MAX_Y - DOT_WIDTH
                    is_wall_hit = True
                # Collision check with walls
                if is_wall_hit:
                    if not self.is_walled:
                        segment_list[seg_num]["coord"] = (x, y)
                        seg_turtle.goto(x=x, y=y)
                    else:
                        is_dead = True
                # Collision check with body
                for seg in self.snake[2:]:
                    if self.head.distance(seg["segment"]) < 10:
                        is_dead = True
            else:
                if is_dead:
                    break
                new_coord = segment_list[seg_num - 1]["coord"]
                segment_list[seg_num]["coord"] = new_coord
                seg_turtle.goto(new_coord)
        if not is_dead:
            return True
        else:
            return False

    def snake_right(self):
        if self.head.heading() != DIR_LEFT:
            self.head.setheading(DIR_RIGHT)

    def snake_up(self):
        if self.head.heading() != DIR_DOWN:
            self.head.setheading(DIR_UP)

    def snake_left(self):
        if self.head.heading() != DIR_RIGHT:
            self.head.setheading(DIR_LEFT)

    def snake_down(self):
        if self.head.heading() != DIR_UP:
            self.head.setheading(DIR_DOWN)

    def _snake_get_last(self) -> dict:
        num_segments = len(self.snake) - 1
        last_segment = self.snake[num_segments]
        return last_segment

    def snake_grow(self):
        '''Copy the last segment and append'''
        last_segment = self._snake_get_last()
        last_coord = last_segment["coord"]
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_coord)
        self.snake.append(
            {
                "segment": new_segment,
                "coord": last_coord,
                "ishead": False
            }
        )

    def print_snake(self):
        for seg in self.snake:
            print(f"coord: {seg['coord']} // ishead: {seg['ishead']}")
