import pygame
import math
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = (255 , 255, 0)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wills test:")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
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
    def night():
        screen.fill(BLACK)
        
    
    def day():
        screen.fill(BLUE)
    #endfunction
    screen.fill(BLUE)
    
    
    #draw stuff here:
    x_val += 3
    y_val = 24/6125 * x_val ** 2 + -2.798 *x_val + 500


    #x_val = x_val + x_offset
    # if x_val > size[0]:
    #     x_val = 0
    #     counter = 1
    if counter > 0:
        night()
        counter = 0
    else:
        day()
        
    
    #endif
    pygame.draw.rect(screen, GREEN, [0, 300, 700, 200], 0)
    pygame.draw.rect(screen, RED, [250, 250, 200, 150], 0)
    pygame.draw.circle(screen, YELLOW, [x_val, y_val] , 20)
    pygame.draw.polygon(screen,BLACK, [[250, 250] , [355,150] , [450,250]])
    pygame.draw.rect(screen,WHITE, [340, 335, 25, 50], 0)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()