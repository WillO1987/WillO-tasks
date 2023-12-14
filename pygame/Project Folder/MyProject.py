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
pygame.display.set_caption("Cookout:")#
moveSide = 0
moveUp = 0

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#classes go here

#endclass
class Pacman(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, initial_x, initial_y, s_health):
        super().__init__()
        self.x_val2 = x_val2
        self.health = s_health
        self.width = s_width
        self.height = s_length
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
    def update(self):
        global moveSide
        global moveUp
        self.rect.x += moveSide
        self.rect.y += moveUp
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
            moveSide = -1
            moveUp = 0
            #self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            moveSide = 1
            moveUp = 0
            #self.rect.x += 5
        if keys[pygame.K_UP]:
            moveSide = 0
            moveUp = -1
           # self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            moveSide = 0
            moveUp = 1
            #self.rect.y += 5
    
    def eatItems(self, item):
        global score
        if isinstance(item, Ghost):
            score += 1
        elif isinstance(item, Coin):
            score += 10  # Adjust the score as needed
            item.kill()   # Remove the coin when Pacman collects it

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

class Coin(pygame.sprite.Sprite):
    def __init__(self, C_colour, width, height, C_xval, C_yval):
        super().__init__()
        self.width = width
        self.height = height
        self.colour = C_colour
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = C_xval
        self.rect.y = C_yval
        
   

        

class Ghost(pygame.sprite.Sprite):
    def __init__(self, I_width, I_height ):
        super().__init__()
        self.width = I_width
        self.height = I_height
        self.speed = random.randrange(1,3)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,700)
        self.rect.y = random.randrange(0,350)
        #self.horizontalspeed = random.randrange(-2,-1)
        self.horizontalspeed = -1

    def update(self):
        self = self


#global variables
x_val2 = 350
enemy_count = 5
x_val = 60
y_val = 60
x_offset = 1
pi= 3.141592652
counter = 0
end = ""


#create sprite groups
all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
ghost_sprites = pygame.sprite.Group()
pacman_sprite = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

# create player spaceship
player = Pacman(10, 10 , x_val , y_val , 3)
pacman_sprite.add(player)
all_sprites.add(player)
#set the enemy count
Ghost_num = enemy_count

ghost = Ghost(5,5)
#<---------- MAP MAKE HERE ----------------->

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


for y in range(0,20):
    for x in range(0,20):
        if map[x][y] == 1:
            my_wall = Block(WHITE ,20 , 20 , x*20 , y*20)
            wall_list.add(my_wall)
            all_sprites.add(my_wall)

for y in range(0, 20):
    for x in range(0, 20):
        if map[x][y] == 0:  #  0 represents an empty space for coins
            coin = Coin(YELLOW, 20, 20, x * 20, y * 20)
            coin_sprites.add(coin)
            all_sprites.add(coin)



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
    pacman_sprite.draw(screen)
    
    coin_sprites.draw(screen)

    #messages at the top 
    realscore = score 
    score_count = font.render("Score Count: " + str(realscore), True, BLACK)
    # endmessage = font.render(end, True, WHITE)
    # screen.blit(endmessage, [271,103])
    screen.blit(score_count, [200,4])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()