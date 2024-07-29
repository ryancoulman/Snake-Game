from turtle import Turtle
import random
SEG_LENGTH = 20


class Food(Turtle):

    # Initialise the food object to appear at a random position on screen
    def __init__(self, screen_height=600, screen_width=600):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.new_pos()

    # Food object resets each time the snake collides with it
    def new_pos(self):
        edge_x, edge_y = self.screen_width / 2 - SEG_LENGTH, self.screen_height / 2 - SEG_LENGTH
        self.goto(x=random.randint(-edge_x, edge_x), y=random.randint(-edge_y, edge_y))