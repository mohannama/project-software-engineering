# Import necessary libraries
import random
import pygame
import time

# Initialize the game
pygame.init()

# Define grid and character properties
grid_size = 5
cell_size = 100
grid = [[0] * grid_size for _ in range(grid_size)]
player1_x, player1_y = 0, 0
player2_x, player2_y = grid_size - 1, grid_size - 1

# Set up the game window
window_size = (grid_size*cell_size, grid_size*cell_size)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Wandering in the Woods")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move characters randomly
    player1_x, player1_y = random.choice([(player1_x + 1, player1_y), (player1_x, player1_y + 1)])
    player2_x, player2_y = random.choice([(player2_x - 1, player2_y), (player2_x, player2_y - 1)])

    # Check if characters meet
    if (player1_x, player1_y) == (player2_x, player2_y):
        # Display happy graphics and announce statistics
        # Reset the game
        player1_x, player1_y = 0, 0
        player2_x, player2_y = grid_size - 1, grid_size - 1

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw characters (you can customize this part with graphics)
    pygame.draw.rect(screen, (255, 0, 0), (player1_x * cell_size, player1_y * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, (0, 0, 255), (player2_x * cell_size, player2_y * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.flip()

    time.sleep(2)


# Quit the game
pygame.quit()
