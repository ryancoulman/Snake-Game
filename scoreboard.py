from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.penup()
        self.goto(x=0, y=270)
        self.color('white')
        self.update_score()
        self.hideturtle()

    # Called to update the score each time it is modified
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    # Opens the data.txt file to get the current high score
    def get_high_score(self):
        with open("data.txt", "r") as file:
            data = file.read()
            return int(data) if data else 0

    # Writes to the data.txt file with the new high score if surpassed
    def write_high_score(self):
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")

    # Resets the old score
    def reset(self, screen):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()

        self.goto(x=0, y=0)
        self.write('GAME OVER.', align='center', font=("Courier", 24, "normal"))
        screen.update()
        time.sleep(2)
        self.clear()
        self.goto(x=0, y=270)
        screen.update()

        self.score = 0
        self.update_score()
