import pygame
import math
import random
import time

from pygame.sprite import _Group

# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = (255 , 255, 0)
screenx =700
screeny = 500
size = (screenx, screeny)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wills test:")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#classes go here

class Invader(pygame.sprite.Sprite):
    def __init__(self,I_color, I_width, I_height ):
        super().__init__()
        self.width = I_width
        self.height = I_height
        self.image = pygame.surface([I_width, I_height])


x_val = 0
y_val = 200
x_offset = 1
pi= 3.141592652
counter = 0

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
   
    screen.fill(BLUE)
    
    
    #draw stuff here:
   

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()