import time
from turtle import Screen
from puzzle_board import Puzzle
from puzzle_score import Score
from puzzle_board import Grid
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

puzzle = Puzzle()
score = Score()
grid = Grid()

screen.listen()
screen.onkeypress(puzzle.up, "Up")
screen.onkeypress(puzzle.down, "Down")
screen.onkeypress(puzzle.right, "Right")
screen.onkeypress(puzzle.left, "Left")
while True:
    score.score(puzzle.return_score())
    if puzzle.check_correct():
        puzzle.clear()
        grid.clear()
        score.game_finished()
        break
    time.sleep(.1)
    screen.update()

screen.exitonclick()
