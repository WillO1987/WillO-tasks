from typing import Any
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
score = 0
#lives = 5
end = ""
text_font = pygame.font.SysFont(None, 30)
font = pygame.font.SysFont(None, 30)
screen_x =700
screen_y = 500
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cooking Game:")#
moveSide = 0
moveUp = 0

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#classes go here

#endclass
class Chef(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, initial_x, initial_y):
        super().__init__()
        self.x_val2 = x_val2
        self.width = s_width
        self.height = s_length
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
    def update(self):
        # Check for collisions with walls
        wall_collisions = pygame.sprite.spritecollide(self, wall_list, False)
        for wall in wall_collisions:
            if moveSide > 0:
                self.rect.right = wall.rect.left
            elif moveSide < 0:
                self.rect.left = wall.rect.right
            if moveUp > 0:
                self.rect.bottom = wall.rect.top
            elif moveUp < 0:
                self.rect.top = wall.rect.bottom
        #check collisions with coins
        coin_collisions = pygame.sprite.spritecollide(player, coin_sprites, True)
        for coin in coin_collisions:
            player.eatItems(coin)
        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            
            self.rect.x -= 2
        if keys[pygame.K_RIGHT]:
          
            self.rect.x += 2
            
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
    
    def pickUPitem(self, item):  
        # global score
        # if isinstance(item, Ghost):
        #     score += 1
        # elif isinstance(item, Coin):
        #     score += 10  # Adjust the score as needed
        #     item.kill()   # Remove the coin when Pacman collects i
        pass

class Block(pygame.sprite.Sprite):
    def __init__(self ,B_colour , width , height, B_xval, B_yval):
        super().__init__()   
        self.width = width
        self.height = height
        self.colour = B_colour   
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()  
        self.rect.x = B_xval
        self.rect.y = B_yval
        
    def update(self):
        self = self
 

        

class Item(pygame.sprite.Sprite): #Parent Class 
    def __init__(self, I_width, I_height, I_type, I_colour ):
        super().__init__()
        self.width = I_width
        self.height = I_height
        self.type = I_type

    
        self.colour = I_colour   
      

    def update(self):
        pass

class beef(pygame.sprite.Sprite): #daughter class
    def __init__(self, I_width, I_height, I_xval , I_Yval , I_colour):
        super().__init__(I_width, I_height, I_colour)
        self.type = "meat"
   
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()  
        self.rect.x = I_xval 
        self.rect.y = I_Yval

    def update(self):
        pass

    def cook(self):
        pass

class bread(pygame.sprite.Sprite):
    def __init__(self, I_width, I_height, I_xval , I_Yval , I_colour):
        super().__init__(I_width, I_height , I_colour)
        self.type = "meat"
        
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()  
        self.rect.x = I_xval 
        self.rect.y = I_Yval
    def update(self):
        pass

class Cheese(pygame.sprite.Sprite):
    def __init__(self, I_width, I_height, I_xval , I_Yval , I_colour):
        super().__init__(I_width, I_height , I_colour)
        self.type = "Cheese"
         
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()  
        self.rect.x = I_xval 
        self.rect.y = I_Yval

    def update(self):
        pass

#global variables
x_val2 = 350
enemy_count = 5
x_val = 60
y_val = 60
x_val1 = 70
y_val1 = 100
x_offset = 1
pi= 3.141592652
counter = 0
end = ""


#create sprite groups
all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
item_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

# create player spaceship
player = Chef(10, 10 , x_val , y_val )
player_sprite.add(player)
all_sprites.add(player)

#create items
cheese = Cheese(5, 5, x_val1 , y_val1 , YELLOW)
all_sprites.add(cheese)
item_sprite.add(cheese)

#<---------- MAP MAKE HERE ----------------->



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    #check for collisions
   
    
    #update game objects
    all_sprites.update()
   
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    
    screen.fill(BLUE)
    

    #draw stuff here:
    all_sprites.draw(screen)
    player_sprite.draw(screen)
    
    coin_sprites.draw(screen)

    #messages at the top 
    realscore = score 
    score_count = font.render("Score Count: " + str(realscore), True, BLACK)
    # endmessage = font.render(end, True, WHITE)
    # screen.blit(endmessage, [271,103])
    screen.blit(score_count, [275,4])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()