# pyqt5
class button:
    def __init__(self):
        pass

def image(path,width_ratio,height_ratio):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img,(width_ratio*screen_width,height_ratio*screen_height))
    return img

def hover(standard,hover,position,mouse):
    if position[0] < mouse[0] < position[0] + standard.get_width() and position[1] < mouse[1] < position[1] + standard.get_height():
        screen.blit(hover,position)
    else:
        screen.blit(standard,position)

# Libraries
import pygame

# Initilazation
pygame.init()

# Screen
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

# Fonts
font1 = pygame.font.Font("Fonts/Aladin-Regular.ttf",round(0.0732064421669107*screen_width))

# Text
title = font1.render("SortIT",True,'White')

# Images
top_left = image('Images/Top_Left.png',0.3060102489019034,0.396171875)
bottom_right = image('Images/Bottom_Right.png',0.1930453879941435,0.27734375)
close_1 = image('Icons/Close_1.png',0.0329428989751098,0.05859375)
close_2 = image('Icons/Close_2.png',0.0329428989751098,0.05859375)
bubble_1 = image('Images/Bubble_1.png',0.109809663250366,0.0651041666666667)
bubble_2 = image('Images/Bubble_2.png',0.109809663250366,0.0651041666666667)
insertion_1 = image('Images/Insertion_1.png',0.109809663250366,0.0651041666666667)
insertion_2 = image('Images/Insertion_2.png',0.109809663250366,0.0651041666666667)
selection_1 = image('Images/Selection_1.png',0.109809663250366,0.0651041666666667)
selection_2 = image('Images/Selection_2.png',0.109809663250366,0.0651041666666667)
merge_1 = image('Images/Merge_1.png',0.109809663250366,0.0651041666666667)
merge_2 = image('Images/Merge_2.png',0.109809663250366,0.0651041666666667)
quick_1 = image('Images/Quick_1.png',0.109809663250366,0.0651041666666667)
quick_2 = image('Images/Quick_2.png',0.109809663250366,0.0651041666666667)
shell_1 = image('Images/Shell_1.png',0.109809663250366,0.0651041666666667)
shell_2 = image('Images/Shell_2.png',0.109809663250366,0.0651041666666667)
heap_1 = image('Images/Heap_1.png',0.109809663250366,0.0651041666666667)
heap_2 = image('Images/Heap_2.png',0.109809663250366,0.0651041666666667)
counting_1 = image('Images/Counting_1.png',0.109809663250366,0.0651041666666667)
counting_2 = image('Images/Counting_2.png',0.109809663250366,0.0651041666666667)
radix_1 = image('Images/Radix_1.png',0.109809663250366,0.0651041666666667)
radix_2 = image('Images/Radix_2.png',0.109809663250366,0.0651041666666667)
bucket_1 = image('Images/Bucket_1.png',0.109809663250366,0.0651041666666667)
bucket_2 = image('Images/Bucket_2.png',0.109809663250366,0.0651041666666667)

# Positions
top_left_pos = (0,0)
bottom_right_pos = (0.8071010248901903*screen_width,0.72265625*screen_height)
close_pos = (0.9560761346998536*screen_width,0.01953125*screen_height)
bubble_1_pos = (0.2152269399707174*screen_width,0.41796875*screen_height)
insertion_1_pos = (0.3301610541727672*screen_width,0.41796875*screen_height)
selection_1_pos = (0.445095168374817*screen_width,0.41796875*screen_height)
merge_1_pos = (0.5600292825768668*screen_width,0.41796875*screen_height)
quick_1_pos = (0.6749633967789165*screen_width,0.41796875*screen_height)
shell_1_pos = (0.2152269399707174*screen_width,0.49609375*screen_height)
heap_1_pos = (0.3301610541727672*screen_width,0.49609375*screen_height)
counting_1_pos = (0.445095168374817*screen_width,0.49609375*screen_height)
radix_1_pos = (0.5600292825768668*screen_width,0.49609375*screen_height)
bucket_1_pos = (0.6749633967789165*screen_width,0.49609375*screen_height)

# Rectangles
title_rect = title.get_rect()
close_rect = close_1.get_rect()
close_rect.x, close_rect.y = round(close_pos[0]), round(close_pos[1])
bubble_rect = pygame.Rect(bubble_1_pos[0],bubble_1_pos[1],bubble_1.get_width(),bubble_1.get_height())

# Positions
title_rect.centerx = screen_width/2
title_rect.y = 0.1041666666666667*screen_height

# Basic Settings
clock = pygame.time.Clock()
close_hover = False
running = True
mouse_pos = pygame.mouse.get_pos()
bubble = False

# Game Loop
while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bubble_rect.collidepoint(mouse_pos):
                print("Collide")
                bubble = True

            if close_rect.collidepoint(mouse_pos):
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    mouse_pos = pygame.mouse.get_pos()
    screen.fill((40,54,70))

    # Title
    screen.blit(title,(title_rect))

    # Border
    screen.blit(top_left,top_left_pos)
    screen.blit(bottom_right,bottom_right_pos)

    # Button
    hover(close_1,close_2,close_pos,mouse_pos)
    if not bubble:
        hover(bubble_1,bubble_2,bubble_1_pos,mouse_pos)
    else:
        screen.blit(bubble_2,bubble_1_pos)
    hover(insertion_1,insertion_2,insertion_1_pos,mouse_pos)
    hover(selection_1,selection_2,selection_1_pos,mouse_pos)
    hover(merge_1,merge_2,merge_1_pos,mouse_pos)
    hover(quick_1,quick_2,quick_1_pos,mouse_pos)
    hover(shell_1,shell_2,shell_1_pos,mouse_pos)
    hover(heap_1,heap_2,heap_1_pos,mouse_pos)
    hover(counting_1,counting_2,counting_1_pos,mouse_pos)
    hover(radix_1,radix_2,radix_1_pos,mouse_pos)
    hover(bucket_1,bucket_2,bucket_1_pos,mouse_pos)

    # FPS
    clock.tick(60)

    pygame.display.flip()

pygame.quit()