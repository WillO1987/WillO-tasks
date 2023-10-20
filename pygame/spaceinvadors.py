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
pygame.display.set_caption("Wills test:")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#classes go here
class Bullet(pygame.sprite.Sprite):
    def __init__(self, b_width , b_length):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = b_width
        self.rect.centery = b_length
    def update(self) :
        self.rect.y = self.rect.y - 3

#endclass
class spaceship(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, initial_x):
        super().__init__()
        self.x_val2 = x_val2
        self.width = s_width
        self.height = s_length
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = 465

    

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

        

class Invador(pygame.sprite.Sprite):
    def __init__(self, I_width, I_height ):
        super().__init__()
        self.width = I_width
        self.height = I_height
        self.speed = random.randrange(1,3)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,700)
        self.rect.y = 0
        #self.horizontalspeed = random.randrange(-2,-1)
        self.horizontalspeed = -1

    def update(self):
        if self.rect.y >= -50 :
            self.rect.y = self.rect.y - self.horizontalspeed
        if self.rect.y > screen_y:
            self.rect.y = -50
            pygame.quit()
            # end = "GAME OVER"
            # endmessage = font.render(end, True, WHITE)
            # screen.blit(endmessage, [271,103])
            # #lives = 5
            #lives = lives - 1
       


#global variables
x_val2 = 350
enemy_count = 5
x_val = 0
y_val = 200
x_offset = 1
pi= 3.141592652
counter = 0
end = ""


#create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
invador_sprites = pygame.sprite.Group()
spaceship_sprite = pygame.sprite.Group()

# create player spaceship
player = spaceship(40 , 30 , x_val2)
spaceship_sprite.add(player)

#set the enemy count
Invador_Num = enemy_count


 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.add(bullet)
            all_sprites.add(bullet)
    
    if len(invador_sprites) < Invador_Num:
        Invador_width = 30
        Invador_Length = 15 
        enemy = Invador(Invador_width, Invador_Length)
        invador_sprites.add(enemy)
        all_sprites.add(enemy)
        #add 1 to the score becuase eneemy killed 
        score = score + 1
        #Invador_Num = Invador_Num + 1
    # --- Game logic should go here

    #check for collisions
    hits = pygame.sprite.groupcollide(invador_sprites, bullets, True, True)
    
    #update game objects
    all_sprites.update()
    spaceship_sprite.update()

    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    
    screen.fill(BLUE)
    
    #draw stuff here:
    all_sprites.draw(screen)
    spaceship_sprite.draw(screen)
    
    #messages at the top 
    realscore = score - 5
    score_count = font.render("Score Count: " + str(realscore), True, WHITE)
    # endmessage = font.render(end, True, WHITE)
    # screen.blit(endmessage, [271,103])
    screen.blit(score_count, [280,40])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()