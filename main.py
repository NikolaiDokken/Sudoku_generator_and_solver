import pygame
from sudoku import Sudoku

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
size = [600, 640]
screen = pygame.display.set_mode([size[0] + 2, size[1]])

square_side = size[0] / 9

pygame.display.set_caption("Sudoku")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Generates a sudoku
sudoku = Sudoku([
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
solved = False

# Keeps track of users input
input_sudoku = [[0 for i in range(9)] for j in range(9)]
row, col = 0, 0

# Font to be used for text
my_font = pygame.font.SysFont("Helvetica", 48)
error_font = pygame.font.SysFont("Helvetica", 20)
instructions_font = pygame.font.SysFont("Helvetica", 24)

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:  # Key pressed
            if event.key == pygame.K_SPACE:
                sudoku.solve()
                solved = True
            if event.key == pygame.K_DOWN:
                row = (row + 1) % 9
            if event.key == pygame.K_UP:
                row = (row - 1) % 9
            if event.key == pygame.K_RIGHT:
                col = (col + 1) % 9
            if event.key == pygame.K_LEFT:
                col = (col - 1) % 9
            if event.key in range(48, 58):
                if sudoku.arr[row][col] == 0:
                    input_sudoku[row][col] = event.key - 48
            if event.key == pygame.K_BACKSPACE:
                input_sudoku[row][col] = 0

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draws grid
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, [0, i * square_side], [size[0], i * square_side], 5)
            pygame.draw.line(screen, BLACK, [i * square_side, 0], [i * square_side, size[0]], 5)
        else:
            pygame.draw.line(screen, BLACK, [0, i * square_side], [size[0], i * square_side], 1)
            pygame.draw.line(screen, BLACK, [i * square_side, 0], [i * square_side, size[0]], 1)

    # Draws numbers
    sudoku.draw_sudoku(screen, square_side, my_font)
    label = instructions_font.render("Use arrow-keys to navigate and space to solve.", 1, BLACK)
    screen.blit(label, (10, square_side * 9))
    for i in range(9):
        for j in range(9):
            if input_sudoku[i][j] != 0:
                if solved:
                    if input_sudoku[i][j] != sudoku.arr[i][j]:
                        label = error_font.render(str(input_sudoku[i][j]), 1, RED)
                        screen.blit(label, (j * square_side + 5, i * square_side + 2))
                        continue
                    else:
                        label = my_font.render(str(input_sudoku[i][j]), 1, GREEN)
                else:
                    label = my_font.render(str(input_sudoku[i][j]), 1, GREY)
                screen.blit(label, (j * square_side + square_side * 0.3, i * square_side + square_side*0.1))
    if not solved:
        pygame.draw.rect(screen, (255, 0, 0),
                         pygame.Rect(col * square_side, row * square_side, square_side, square_side),
                         2)
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
