import random


class Sudoku:
    # generates random sudoku
    def __init__(self, sudoku=None):
        if not sudoku:
            self.arr = [[0 for i in range(9)] for j in range(9)]
            self.generate_sudoku()
        else:
            self.arr = sudoku

    def print_sudoku(self):
        for x in range(9):
            print(self.arr[x])

    def valid_slot(self, row, col, num):
        # check row
        if num in self.arr[row]:
            return False

        # check column
        for y in range(9):
            if self.arr[y][col] == num:
                return False

        # check box
        for x in range(3):
            for y in range(3):
                # check if section is valid
                if self.arr[x + row - row % 3][y + col - col % 3] == num:
                    return False
        return True

    def find_empty_pos(self, pos):
        for row in range(9):
            for col in range(9):
                if self.arr[row][col] == 0:
                    pos[0] = row
                    pos[1] = col
                    return True
        return False

    def generate_sudoku(self):
        # Number of hints to fill in
        # 17 is the lowest amount of hints that gives unique answer
        for i in range(17):
            # choose random numbers
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
            while not self.valid_slot(row, col, num) or self.arr[row][col] != 0:  # if taken or not valid re-roll
                row = random.randrange(9)
                col = random.randrange(9)
                num = random.randrange(1, 10)
            self.arr[row][col] = num

    def solve(self):
        pos = [0, 0]
        if not self.find_empty_pos(pos):
            return True

        row = pos[0]
        col = pos[1]

        for num in range(1, 10):
            if self.valid_slot(row, col, num):
                self.arr[row][col] = num
                if self.solve():
                    return True

                self.arr[row][col] = 0
        return False

    # This method is only used to display sudoku in GUI
    def draw_sudoku(self, screen, square_size, font):
        for row in range(9):
            for col in range(9):
                if self.arr[row][col] != 0:
                    label = font.render(str(self.arr[row][col]), 1, (0, 0, 0))
                    screen.blit(label, (col * square_size + square_size * 0.3, row * square_size))


if __name__ == "__main__":
    test_sudoku = Sudoku([
        [0, 0, 4, 0, 0, 0, 3, 0, 0],
        [2, 0, 0, 7, 0, 9, 0, 0, 8],
        [0, 6, 0, 5, 0, 4, 0, 7, 0],
        [0, 0, 5, 0, 7, 0, 2, 0, 0],
        [4, 0, 0, 3, 0, 5, 0, 0, 9],
        [0, 0, 7, 0, 9, 0, 5, 0, 0],
        [0, 4, 0, 9, 0, 2, 0, 5, 0],
        [8, 0, 0, 6, 0, 7, 0, 0, 2],
        [0, 0, 9, 0, 0, 0, 1, 0, 0]
    ])
    print("Input sudoku")
    test_sudoku.print_sudoku()
    print()

    test_sudoku.solve()
    print("Solved sudoku:")
    test_sudoku.print_sudoku()
