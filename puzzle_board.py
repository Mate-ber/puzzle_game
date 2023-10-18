import turtle
STRING_DISTANCE = 50

class Puzzle:
    def __init__(self):
        #self.board = [['1', '2', '3', '4'],
        #              ['5', '6', '7', '8'],
        #              ['9', '10', '11', '12'],
        #              ['13', '14', ' ', '15']]
        self.board = [['4', '15', '3', '9'],
                      ['5', '14', '11', '1'],
                      ['2', '8', '10', ' '],
                      ['12', '6', '7', '13']]
        self.board_height = 4
        self.board_width = 4
        self.move_made = 0
        self.tur = turtle.Turtle()
        self.tur.penup()
        self.tur.hideturtle()
        self.write_board()

    def write_board(self):
        self.tur.goto(-80, 80)
        for i in range(0, self.board_height):
            for j in range(0, self.board_width):
                self.tur.write(self.board[i][j], align="left", font=("Courier", 20, "normal"))
                self.tur.goto(self.tur.xcor() + STRING_DISTANCE, self.tur.ycor())
            self.tur.goto(self.tur.xcor() - 200, self.tur.ycor() - STRING_DISTANCE)

    def change(self, vx, vy, tx, ty):
        self.clear()
        if self.board_width > tx >= 0 and self.board_height > ty >= 0:
            self.move_made += 1
            self.board[vx][vy] = self.board[tx][ty]
            self.board[tx][ty] = ' '
        self.write_board()

    def up(self):
        cor = self.find_void()
        self.change(cor[0], cor[1], cor[0] + 1, cor[1])

    def down(self):
        cor = self.find_void()
        self.change(cor[0], cor[1], cor[0] - 1, cor[1])

    def right(self):
        cor = self.find_void()
        self.change(cor[0], cor[1], cor[0], cor[1] - 1)

    def left(self):
        cor = self.find_void()
        self.change(cor[0], cor[1], cor[0], cor[1] + 1)

    def find_void(self):
        vx = 0
        vy = 0
        for i in range(0, self.board_height):
            for j in range(0, self.board_width):
                if self.board[i][j] == ' ':
                    vx = i
                    vy = j
        return vx, vy

    def clear(self):
        self.tur.clear()

    def check_correct(self):
        need = 1
        for i in range(0, self.board_height):
            for j in range(0, self.board_width):
                if self.board[i][j] == ' ' and i == 3 and j == 3:
                    return True
                elif self.board[i][j] != ' ' and int(self.board[i][j]) == need:
                    need += 1
                else:
                    return False
        return True

    def return_score(self):
        return self.move_made


class Grid:
    def __init__(self):
        self.grid_d = turtle.Turtle()
        self.grid_d.color("black")
        self.grid_d.hideturtle()
        self.draw_grid()


    def draw_grid(self):
        xcor = -95
        ycor = 120
        for i in range(5):
            self.change_cor(xcor, ycor)
            self.for_10()
            ycor -= STRING_DISTANCE
        self.grid_d.right(90)
        xcor = -95
        ycor = 120
        for i in range(5):
            self.change_cor(xcor, ycor)
            self.for_10()
            xcor += STRING_DISTANCE

    def for_10(self):
        for i in range(10):
            self.grid_d.forward(20)

    def change_cor(self, x, y):
        self.grid_d.penup()
        self.grid_d.goto(x, y)
        self.grid_d.pendown()

    def clear(self):
        self.grid_d.clear()
