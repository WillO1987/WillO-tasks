import pygame
import pygame
import math
import random
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

#classes
class snow(pygame.sprite.Sprite):
    #construcor function
        def __init__(self, s_width, s_length):
            super().__init__()
            self.width = s_width
            self.length = s_length
            # self.Y_position = y
            # self.X_postion = x
            self.speed = random.randrange(1,3)
            self.image = pygame.Surface([s_width, s_length])
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(0,700)
            self.rect.y = random.randrange(0, 500)
            self.horizontalspeed = random.randrange(-2,2)
           
        #ednconstructor function

        def update(self):
            if self.rect.y > 500 :
                self.rect.y = -50
                self.speed = random.randrange(1,3)
                self.rect.x = self.rect.x + self.horizontalspeed

            else:
                self.rect.y = self.rect.y + self.speed
            #endif
            if self.rect.y > 0:
                self.rect.x = self.rect.x + self.horizontalspeed
            if self.rect.x < 0 and self.rect.y > 500:
                self.rect.x = random.randrange(0,700)
            elif self.rect.x > 700 and self.rect.y > 500:
                self.rect.x = random.randrange(0,700)
        
#endclass

#global variables
snow_list = pygame.sprite.Group()
number_of_flakes = 6000
for i in range(0,number_of_flakes):
    sizeee = random.randrange(2,5)
    flake = snow(sizeee,sizeee)
    snow_list.add(flake)
#next i 

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
    
    snow_list.update()
    #draw stuff here:
   
    snow_list.draw(screen)
   # pygame.draw.rect(screen, WHITE, [0, 300, 700, 200], 0)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()