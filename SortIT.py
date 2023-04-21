# Imports
import pygame
from math import floor
from Files.algorithms import *
from Files.resources import *
from Files.buttons import *

# Initilazation
pygame.init()

# Screen
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

# Basic Settings
clock = pygame.time.Clock()
running = True
active = False
bubble = selection = insertion = merge = quick = shell = heap = counting = radix = bucket = False
method = None
result = ''
start_res = 0
end_res = 65
left = 0
right = 0

# Game Loop
while running:

    # Events
    for event in pygame.event.get():

        # Mouse Pressed
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Input Box
            if input_box_rect.collidepoint(mouse_pos):
                active = True
            else:
                active = False

            # Method Value
            if bubble_rect.collidepoint(mouse_pos):
                method = 'bubble'
                bubble = True
                selection = insertion = merge = quick = shell = heap = counting = radix = bucket = False
            elif insertion_rect.collidepoint(mouse_pos):
                method = 'insertion'
                insertion = True
                bubble = selection = merge = quick = shell = heap = counting = radix = bucket = False
            elif selection_rect.collidepoint(mouse_pos):
                method = 'selection'
                selection = True
                bubble = insertion = merge = quick = shell = heap = counting = radix = bucket = False
            elif merge_rect.collidepoint(mouse_pos):
                method = 'merge'
                merge = True
                bubble = selection = insertion = quick = shell = heap = counting = radix = bucket = False
            elif quick_rect.collidepoint(mouse_pos):
                method = 'quick'
                quick = True
                bubble = selection = insertion = merge = shell = heap = counting = radix = bucket = False
            elif shell_rect.collidepoint(mouse_pos):
                method = 'shell'
                shell = True
                bubble = selection = insertion = merge = quick = heap = counting = radix = bucket = False
            elif heap_rect.collidepoint(mouse_pos):
                method = 'heap'
                heap = True
                bubble = selection = insertion = merge = quick = shell = counting = radix = bucket = False
            elif counting_rect.collidepoint(mouse_pos):
                method = 'counting'
                counting = True
                bubble = selection = insertion = merge = quick = shell = heap = radix = bucket = False
            elif radix_rect.collidepoint(mouse_pos):
                method = 'radix'
                radix = True
                bubble = selection = insertion = merge = quick = shell = heap = counting = bucket = False
            elif bucket_rect.collidepoint(mouse_pos):
                method = 'bucket'
                bucket = True
                bubble = selection = insertion = merge = quick = shell = heap = counting = radix = False

            # SortIT
            if sortit_rect.collidepoint(mouse_pos) and method != None:
                array = text.split(',')
                try:
                    flo = False
                    for i in range(len(array)):
                        if array[i].find(".") != -1:
                            flo = True
                    if flo:
                        for i in range(len(array)):
                            array[i] = float(array[i])
                    else:
                        raise
                except:
                    array = text.split(',')
                    try:
                        integer = False
                        for i in range(len(array)):
                            if array[i].find(".") == -1:
                                integer = True
                        if integer:
                            for i in range(len(array)):
                                array[i] = int(array[i])
                    except:
                        array = text.split(',')
                        for i in range(len(array)):
                            array[i] = array[i].strip()
                to_sort = Algo(array)
                if method == 'bubble':
                    sorted = to_sort.bubbleSort()
                    result = f'Iterations: {Algo.iteration}\nComparisions: {Algo.comparision}\nSwaps: {Algo.swap}\nSorted Array: {sorted}'
                elif method == 'insertion':
                    sorted = to_sort.insertionSort()
                    result = f'Iterations: {Algo.iteration}\nComparisions: {Algo.comparision}\nSwaps: {Algo.swap}\nSorted Array: {sorted}'
                elif method == 'selection':
                    sorted = to_sort.selectionSort()
                    result = f'Iterations: {Algo.iteration}\nComparisions: {Algo.comparision}\nSwaps: {Algo.swap}\nSorted Array: {sorted}'
                elif method == 'merge':
                    result = to_sort.mergeSort()
                elif method == 'quick':
                    result = to_sort.quickSort()
                elif method == 'shell':
                    result = to_sort.shellSort()
                elif method == 'heap':
                    result = to_sort.heapSort()
                elif method == 'counting':
                    result = to_sort.countingSort()
                elif method == 'radix':
                    result = to_sort.radixSort()
                elif method == 'bucket':
                    result = to_sort.bucketSort()
                right = result.splitlines()
                right = len(right[len(right)-1])
                right = floor(right/65)

            # Left/Right Button
            if right_rect.collidepoint(mouse_pos) and result != '' and right != 0:
                right -= 1
                left += 1
                start_res += 65
                end_res += 65
            if left_rect.collidepoint(mouse_pos) and left != 0:
                right += 1
                left -= 1
                end_res -= 65
                start_res -= 65

            # Close Program
            if close_rect.collidepoint(mouse_pos):
                running = False

        # Key Pressed
        if event.type == pygame.KEYDOWN:

            # Close Program
            if event.key == pygame.K_ESCAPE:
                running = False

            # User Input
            if active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Mouse Position
    mouse_pos = pygame.mouse.get_pos()

    # Background
    screen.fill((40,54,70))

    # Close Button
    hover(close_1,close_2,close_pos,mouse_pos)

    # Border
    screen.blit(top_left,top_left_pos)
    screen.blit(bottom_right,bottom_right_pos)

    # Input Box
    if active:
        screen.blit(input_box_2,input_box_pos)
    else:
        hover(input_box_1,input_box_2,input_box_pos,mouse_pos)

    # # Text
    # Title
    screen.blit(title,(title_rect))

    # User Text
    text_length = dt.get_size()
    display_length = input_box_1.get_width() - 0.047244094488189*input_box_1.get_width()*2 - 20
    start = int((text_length[0] - display_length)//11)
    if text == '':
        screen.blit(enter_array,enter_array_rect)
    else:
        if text_length[0] > display_length:
            user_input = font2.render(text[start:],True,(40,54,70))
            dt = font2.render(text,True,(40,54,70))
        else:
            user_input = font2.render(text,True,(40,54,70))
            dt = font2.render(text,True,(40,54,70))
        screen.blit(user_input,user_input_rect)

    # SortIT Button
    hover(sortit_1,sortit_2,sortit_pos,mouse_pos)

    # Sorting Options
    hover_select(mouse_pos,bubble,selection,insertion,merge,quick,shell,heap,counting,radix,bucket)

    # Result Box
    screen.blit(result_box,result_box_pos)
    
    # Left/Right Button
    hover(left_1,left_2,left_pos,mouse_pos)
    hover(right_1,right_2,right_pos,mouse_pos)

    # Result
    if result != '':
        res = result.splitlines()
        res_arr_length = res[len(res)-1]
        a = 0
        for i in res:
            screen.blit(font2.render(i[start_res:end_res],True,(40,54,70)),(result_pos[0],result_pos[1]+a))
            a += result_text.get_height()
    else:
        screen.blit(result_text,result_rect)

    # FPS
    clock.tick(60)

    pygame.display.flip()

pygame.quit()