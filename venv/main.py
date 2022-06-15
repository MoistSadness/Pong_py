# Importing libraries
from operator import truediv
import pygame
pygame.init()

# Define global variables
BLACK = (0,0,0)
WHITE = (255,255,255)
size = (700,500)

# Create a window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")


# Game Loop
isRunning = True
clock = pygame.time.Clock()
while isRunning:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    # Game logic

    # Draw to screen
    screen.fill(BLACK)      # Clear screen
    pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)      # Draw net
    pygame.display.flip()       # Update screen
    clock.tick(60)      # Limit game to 60FPS


# Exit application when complete
pygame.quit()

















