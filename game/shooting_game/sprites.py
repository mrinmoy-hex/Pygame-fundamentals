import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,image_path, gunshot_wav) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound(gunshot_wav)
        
    def shoot(self):
        self.gunshot.play()
        # destorys the target if both sprites overlaps
        pygame.sprite.spritecollide(crosshair, target_group, True)
        
    def update(self):
        # crosshair follows the mouse
        self.rect.center = pygame.mouse.get_pos()
        
        
class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y) -> None:
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]



# general setup
pygame.init()
clock = pygame.time.Clock()

# media path
bg_path = "game/assets/sprite_new_game/bg.png"
crosshair_path = "game/assets/sprite_new_game/corsshair.png"
gunshot_wav = "game/assets/sprite_new_game/gunshot.mp3"
target_image = "game/assets/sprite_new_game/target_colored.png"

# game screen
screen_width = 1500
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_visible(False)

# load and scale the background
background = pygame.image.load(bg_path)
background = pygame.transform.scale(background, (screen_width, screen_height))

# Crosshair
crosshair = Crosshair(crosshair_path, gunshot_wav)
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target(target_image, random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
            
    pygame.display.flip()
    screen.blit(background, (0,0))  # putting stuff on screen
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)