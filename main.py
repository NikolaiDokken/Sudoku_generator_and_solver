import pygame
from sudoku import Sudoku

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
size = [600, 700]
screen = pygame.display.set_mode([size[0] + 2, size[1]])

square_side = size[0] / 9

pygame.display.set_caption("Sudoku")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Generates a sudoku
sudoku = Sudoku()

# Font to be used for text
my_font = pygame.font.SysFont("Comic Sans MS", 48)

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sudoku.solve()

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, [0, i * square_side], [size[0], i * square_side], 5)
            pygame.draw.line(screen, BLACK, [i * square_side, 0], [i * square_side, size[0]], 5)
        else:
            pygame.draw.line(screen, BLACK, [0, i * square_side], [size[0], i * square_side], 1)
            pygame.draw.line(screen, BLACK, [i * square_side, 0], [i * square_side, size[0]], 1)

    sudoku.draw_sudoku(screen, square_side, my_font)
    label = my_font.render("Press space to solve", 1, (0, 0, 0))
    screen.blit(label, (10, square_side * 9))

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
