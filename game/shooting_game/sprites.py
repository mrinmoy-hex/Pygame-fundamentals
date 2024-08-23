import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# general setup
pygame.init()
clock = pygame.time.Clock()

# image path
bg_path = "game/assets/sprite_new_game/bg.png"

# game screen
screen_width = 1500
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

# load and scale the background
background = pygame.image.load(bg_path)
background = pygame.transform.scale(background, (screen_width, screen_height))



# Crosshair
crosshair = Crosshair(50, 50, 100, 100, (255, 255, 255))
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.flip()
    screen.blit(background, (0,0))  # putting stuff on screen
    crosshair_group.draw(screen)
    clock.tick(60)