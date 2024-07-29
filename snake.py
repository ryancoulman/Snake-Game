from turtle import Turtle
SEG_LENGTH = 20
START_LENGTH = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # Initialise the snake object to consist of an array of segments
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # Used ot initialise the snake with 3 segments to begin
    def create_snake(self):
        position = [(SEG_LENGTH * (i - int(START_LENGTH / 2)), 0) for i in range(START_LENGTH)]
        for pos in reversed(position):
            self.add_seg(pos)

    # Increases the snake length vy one segment, called when it collides with food
    def add_seg(self, pos):
        seg = Turtle(shape="square")
        seg.penup()
        seg.goto(pos)
        seg.color('white')
        self.snake.append(seg)

    def extend(self):
        self.add_seg(self.snake[-1].position())

    # Resets the snakes length and position
    def reset(self):
        for seg in self.snake:
            seg.hideturtle()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    # Snake moves continuously according to the keyboard arrows
    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(SEG_LENGTH)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)