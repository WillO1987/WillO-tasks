import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    

    carry_block_list = []

    def __init__(self, x, y):
        
        
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(RED)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, diff_x, diff_y):
        # Loop through each block that we are carrying and adjust
        # it by the amount we moved.
        for block in self.carry_block_list:
            block.rect.x += diff_x
            block.rect.y += diff_y


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Wills Block movement test for item pickup')

# Create the player paddle object
player = Player(50, 50)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
block_list = pygame.sprite.Group()


for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

            

               blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

            

               player.carry_block_list = blocks_hit_list

            if event.key == pygame.K_BACKSPACE:

            

               player.carry_block_list = []

            if event.key == pygame.K_LEFT:
                player.rect.x -= player.rect.width
                player.update(-player.rect.width, 0)

            elif event.key == pygame.K_RIGHT:
                player.rect.x += player.rect.width
                player.update(player.rect.width, 0)

            elif event.key == pygame.K_UP:
                player.rect.y -= player.rect.height
                player.update(0, -player.rect.height)

            elif event.key == pygame.K_DOWN:
                player.rect.y += player.rect.height
                player.update(0, player.rect.height)



    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(40)

pygame.quit()