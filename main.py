# pyqt5


# Libraries
import pygame

# Initilazation
pygame.init()

# Screen
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

# Images
top_left = pygame.image.load(r'Images/Top_Left.png').convert_alpha()
close_1 = pygame.image.load(r'Icons/Close_1.png').convert_alpha()
close_2 = pygame.image.load(r'Icons/Close_2.png').convert_alpha()

# Transformations
top_left = pygame.transform.scale(top_left,(0.3060102489019034*screen_width,0.396171875*screen_height))
close_1 = pygame.transform.scale(close_1,(0.0329428989751098*screen_width,0.05859375*screen_height))
close_2 = pygame.transform.scale(close_2,(0.0329428989751098*screen_width,0.05859375*screen_height))

# Positions
top_left_pos = (0,0)
close_pos = (0.9560761346998536*screen_width,0.01953125*screen_height)

# Rectangles
close_rect = close_1.get_rect()
close_rect.x, close_rect.y = round(close_pos[0]), round(close_pos[1])

# Basic Settings
clock = pygame.time.Clock()
close_hover = False
running = True
mouse_pos = pygame.mouse.get_pos()

# Game Loop
while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if close_rect.collidepoint(mouse_pos):
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    mouse_pos = pygame.mouse.get_pos()
    screen.fill((40,54,70))
    screen.blit(top_left,top_left_pos)
    if close_pos[0] < mouse_pos[0] < close_pos[0] + close_rect.width and close_pos[1] < mouse_pos[1] < close_pos[1] + close_rect.height:
        screen.blit(close_2,close_pos)
    else:
        screen.blit(close_1,close_pos)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()