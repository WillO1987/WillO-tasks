import pygame
import math
import random
import time
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = (255 , 255, 0)
PURPLE = (150, 0, 150)
PINK = (255,192,203)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wills PONG")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x_val = 350
y_val = 250
x_offset = 5
y_offset = 5
pi= 3.141592652
counter = 0
screenfill = RED
randomint = random.randint(1,4)
y_val_2 = 200
x_val_2 = 5
lives = 5
text_font = pygame.font.SysFont(None, 30)
font = pygame.font.SysFont(None, 30)
end = ""

 
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
   
    
    screen.fill(screenfill)
    
    
    #draw stuff here:
    lives_count = font.render("Life Count: " + str(lives), True, BLACK)
    endmessage = font.render(end, True, BLACK)
    screen.blit(endmessage, [271,103])
    screen.blit(lives_count, [271,130])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_val_2 -= 5
    if keys[pygame.K_DOWN]:
        y_val_2 += 5


    y_val = y_val+ y_offset
    x_val = x_val + x_offset
    if y_val < 0:
        y_offset = y_offset*-1 

    elif y_val > 495:
        y_offset = y_offset*-1 
        
    
    elif x_val > 695:
        x_offset = x_offset*-1 
    
    elif x_val < 20 and y_val >= y_val_2 and y_val <= y_val_2 + 100:
        x_offset = x_offset*-1 
        
    if x_val < 0 and y_val >= y_val_2+100:
       # screenfill = RED
        x_val = 350
        y_val = 250
        #screenfill = BLUE
        lives -= 1
    
    elif x_val < 0 and y_val <= y_val_2:
       # screenfill = RED
        x_val = 350
        y_val = 250
        #screenfill = BLUE
        lives -= 1    
    
    if lives == 0:
        end = "GAME OVER"
        endmessage = font.render(end, True, WHITE)
        screen.blit(endmessage, [271,103])
        pygame.display.flip() # clears the screen 
        time.sleep(1.5)
        done = True
    

    #end if

    pygame.draw.circle(screen, WHITE, [x_val, y_val] , 10)

    pygame.draw.rect(screen, WHITE, (5, y_val_2, 15, 100))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()