import pygame

def image(path,width_ratio=0.109809663250366,height_ratio=0.0651041666666667):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img,(width_ratio*screen_width,height_ratio*screen_height))
    return img

pygame.init()

screen = pygame.display.set_mode((0,0))
screen_width = screen.get_width()
screen_height = screen.get_height()


# ------ Fonts -------
font1 = pygame.font.Font("Fonts/Aladin-Regular.ttf",round(0.0732064421669107*screen_width))
font2 = pygame.font.Font("Fonts/Aladin-Regular.ttf",round(0.0234260614934114*screen_width))


# ------ Text -------
title = font1.render("SortIT",True,'White')
enter_array = font2.render('Enter Array',True,(40,54,70))
text = ''
user_input = font2.render(text,True,(40,54,70))
result_text = font2.render('Result',True,(40,54,70))
# Result Text Position 0.2379209370424597,0.6015625


#  ------ Images ------
# Borders
top_left = image('Images/Top_Left.png',0.3060102489019034,0.396171875)
bottom_right = image('Images/Bottom_Right.png',0.1930453879941435,0.27734375)

# Close Button
close_1 = image('Images/Close_1.png',0.0329428989751098,0.05859375)
close_2 = image('Images/Close_2.png',0.0329428989751098,0.05859375)

# Input Box
input_box_1 = image('Images/Array_Text_1.png',0.4648609077598829,0.0924479166666667)
input_box_2 = image('Images/Array_Text_2.png',0.4648609077598829,0.0924479166666667)

# SortIT Button
sortit_1 = image('Images/SortIT_1.png',0.0973645680819912,0.0924479166666667)
sortit_2 = image('Images/SortIT_2.png',0.0973645680819912,0.0924479166666667)

# Sorting Options
bubble_1 = image('Images/Bubble_1.png')
bubble_2 = image('Images/Bubble_2.png')
insertion_1 = image('Images/Insertion_1.png')
insertion_2 = image('Images/Insertion_2.png')
selection_1 = image('Images/Selection_1.png')
selection_2 = image('Images/Selection_2.png')
merge_1 = image('Images/Merge_1.png')
merge_2 = image('Images/Merge_2.png')
quick_1 = image('Images/Quick_1.png')
quick_2 = image('Images/Quick_2.png')
shell_1 = image('Images/Shell_1.png')
shell_2 = image('Images/Shell_2.png')
heap_1 = image('Images/Heap_1.png')
heap_2 = image('Images/Heap_2.png')
counting_1 = image('Images/Counting_1.png')
counting_2 = image('Images/Counting_2.png')
radix_1 = image('Images/Radix_1.png')
radix_2 = image('Images/Radix_2.png')
bucket_1 = image('Images/Bucket_1.png')
bucket_2 = image('Images/Bucket_2.png')

# Result Box
result_box = image('Images/Result_Box.png',0.5695461200585652,0.2565104166666667)


# ------ Positions -------
# Borders
top_left_pos = (0,0)
bottom_right_pos = (0.8071010248901903*screen_width,0.72265625*screen_height)

# Close Button
close_pos = (0.9560761346998536*screen_width,0.01953125*screen_height)

# Input Box
input_box_pos = (0.2152269399707174*screen_width,0.3125*screen_height)

# SortIT Button
sortit_pos = (0.6874084919472914*screen_width,0.3125*screen_height)

# Sorting Options
bubble_pos = (0.2152269399707174*screen_width,0.41796875*screen_height)
insertion_pos = (0.3301610541727672*screen_width,0.41796875*screen_height)
selection_pos = (0.445095168374817*screen_width,0.41796875*screen_height)
merge_pos = (0.5600292825768668*screen_width,0.41796875*screen_height)
quick_pos = (0.6749633967789165*screen_width,0.41796875*screen_height)
shell_pos = (0.2152269399707174*screen_width,0.49609375*screen_height)
heap_pos = (0.3301610541727672*screen_width,0.49609375*screen_height)
counting_pos = (0.445095168374817*screen_width,0.49609375*screen_height)
radix_pos = (0.5600292825768668*screen_width,0.49609375*screen_height)
bucket_pos = (0.6749633967789165*screen_width,0.49609375*screen_height)

# Result Box
result_box_pos = (0.2152269399707174*screen_width,0.57421875*screen_height)

# Result
result_pos = (result_box_pos[0]+(result_box.get_width()*0.038560411311054),result_box_pos[1]+(result_box.get_height()*0.1065989847715736))

# ------ Rectangles ------
# Title
title_rect = title.get_rect()
title_rect.centerx = screen_width/2
title_rect.y = 0.1041666666666667*screen_height

# Close Button
close_rect = close_1.get_rect()
close_rect.x, close_rect.y = round(close_pos[0]), round(close_pos[1])

# SortIT Button
sortit_rect = pygame.Rect(sortit_pos[0],sortit_pos[1],sortit_1.get_width(),sortit_1.get_height())

# Sorting Options
bubble_rect = pygame.Rect(bubble_pos[0],bubble_pos[1],bubble_1.get_width(),bubble_1.get_height())
insertion_rect = pygame.Rect(insertion_pos[0],bubble_pos[1],insertion_1.get_width(),insertion_1.get_height())
selection_rect = pygame.Rect(selection_pos[0],selection_pos[1],selection_1.get_width(),selection_1.get_height())
merge_rect = pygame.Rect(merge_pos[0],merge_pos[1],merge_1.get_width(),merge_1.get_height())
quick_rect = pygame.Rect(quick_pos[0],quick_pos[1],quick_1.get_width(),quick_1.get_height())
shell_rect = pygame.Rect(shell_pos[0],shell_pos[1],shell_1.get_width(),shell_1.get_height())
heap_rect = pygame.Rect(heap_pos[0],heap_pos[1],heap_1.get_width(),heap_1.get_height())
counting_rect = pygame.Rect(counting_pos[0],counting_pos[1],counting_1.get_width(),counting_1.get_height())
radix_rect = pygame.Rect(radix_pos[0],radix_pos[1],radix_1.get_width(),radix_1.get_height())
bucket_rect = pygame.Rect(bucket_pos[0],bucket_pos[1],bucket_1.get_width(),bucket_1.get_height())

# Input Box
input_box_rect = pygame.Rect(input_box_pos[0],input_box_pos[1],input_box_1.get_width(),input_box_1.get_height())

# Enter Array
enter_array_rect = enter_array.get_rect()
enter_array_rect.centerx = input_box_pos[0]+(input_box_1.get_width()/2)
enter_array_rect.centery = input_box_pos[1]+(input_box_1.get_height()/2)

# User Input
user_input_rect = user_input.get_rect()
user_input_rect.x = input_box_pos[0]+(0.047244094488189*input_box_1.get_width())
user_input_rect.centery = input_box_pos[1]+(input_box_1.get_height()/2)

# Result
result_rect = result_text.get_rect()
result_rect.centerx = result_box_pos[0]+(result_box.get_width()/2)
result_rect.centery = result_box_pos[1]+(result_box.get_height()/2)