'''
    Following a tutorial online to learn to use pygame
    https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
'''

# Importing libraries
import pygame
from paddle import Paddle
from ball import Ball

# Start pygame
pygame.init()

# Define global variables
BLACK = (0,0,0)
WHITE = (255,255,255)
size = (700,500)

# Create a window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")

# Creating sprites
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# Create a list to store all the sprites in one place
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


# Game Loop
isRunning = True
clock = pygame.time.Clock()
while isRunning:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:         # Press x key to exit game
                isRunning = False

    # Adding event handlers to move the paddle (w/s for player 1, up/down for player 2) 
    pixelsForMovement = 5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(pixelsForMovement)
    if keys[pygame.K_s]:
        paddleA.moveDown(pixelsForMovement)
    if keys[pygame.K_UP]:
        paddleB.moveUp(pixelsForMovement)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(pixelsForMovement)

    # Game logic
    all_sprites_list.update()

    # Check if ball in hitting any of the walls
    if ball.rect.x >= 690 or ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490 or ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    # Draw to screen
    screen.fill(BLACK)      # Clear screen
    pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)      # Draw net
    all_sprites_list.draw(screen)     # Draw sprites all at once
    pygame.display.flip()       # Update screen
    clock.tick(60)      # Limit game to 60FPS


# Exit application when complete
pygame.quit()

















