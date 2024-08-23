import pygame, sys

# settng up pygame
pygame.init()
screen = pygame.display.set_mode((800, 900))
clock = pygame.time.Clock()

current_time = 0
button_pressed_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            button_pressed_time = pygame.time.get_ticks()
            screen.fill((255, 255, 255))
            
    current_time = pygame.time.get_ticks()
    print(f"Current time: {current_time}\n Button press time: {button_pressed_time}")

    if current_time - button_pressed_time >= 2000:
        screen.fill((255, 0, 0))
    
    pygame.display.flip()
    clock.tick(60)