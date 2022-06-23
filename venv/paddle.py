import pygame

BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):       # Constructor for class
        super().__init__()      # Inherit properties from parent class

        # Set color width and height of paddle
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        # Make image transparent
        self.image.set_colorkey(BLACK)

        # Draw paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch rectangle object that has dimensions of the paddle
        self.rect = self.image.get_rect()
    
    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Checking that paddle is not moving off the screen
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # Checking that paddle is not moving off the screen
        if self.rect.y > 400:
            self.rect.y = 400








