from Files.resources import *

def hover(standard,hovering,position,mouse):
    if position[0] < mouse[0] < position[0] + standard.get_width() and position[1] < mouse[1] < position[1] + standard.get_height():
        screen.blit(hovering,position)
    else:
        screen.blit(standard,position)

def hover_select(mouse_pos,bubble,selection,insertion,merge,quick,shell,heap,counting,radix,bucket):
        if bubble:
            screen.blit(bubble_2,bubble_pos)
        else:
            hover(bubble_1,bubble_2,bubble_pos,mouse_pos)
        if insertion:
            screen.blit(insertion_2,insertion_pos)
        else:
            hover(insertion_1,insertion_2,insertion_pos,mouse_pos)
        if selection:
            screen.blit(selection_2,selection_pos)
        else:
            hover(selection_1,selection_2,selection_pos,mouse_pos)
        if merge:
            screen.blit(merge_2,merge_pos)
        else:
            hover(merge_1,merge_2,merge_pos,mouse_pos)
        if quick:
            screen.blit(quick_2,quick_pos)
        else:
            hover(quick_1,quick_2,quick_pos,mouse_pos)
        if shell:
            screen.blit(shell_2,shell_pos)
        else:
            hover(shell_1,shell_2,shell_pos,mouse_pos)
        if heap:
            screen.blit(heap_2,heap_pos)
        else:
            hover(heap_1,heap_2,heap_pos,mouse_pos)
        if counting:
            screen.blit(counting_2,counting_pos)
        else:
            hover(counting_1,counting_2,counting_pos,mouse_pos)
        if radix:
            screen.blit(radix_2,radix_pos)
        else:
            hover(radix_1,radix_2,radix_pos,mouse_pos)
        if bucket:
            screen.blit(bucket_2,bucket_pos)
        else:
            hover(bucket_1,bucket_2,bucket_pos,mouse_pos)