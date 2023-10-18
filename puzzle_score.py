import turtle


class Score:
    def __init__(self):
        self.moves = 0
        self.title = turtle.Turtle()
        self.title.color("black")
        self.title.speed(0)
        self.title.hideturtle()
        self.title.goto(0, 250)
        self.score(0)

    def game_finished(self):
        game_over = turtle.Turtle()
        game_over.color("black")
        game_over.hideturtle()
        game_over.goto(0, 0)
        game_over.write(f"Game Over! You Won!", align="center", font=("Courier", 30, "normal"))

    def score(self, score):
        self.title.clear()
        self.title.write(f"Moves Made: {score}", align="center",
                         font=("Courier", 24, "normal"))

