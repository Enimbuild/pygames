import pygame, sys

#1.Surfaces- A layer that contains visuals (img, solid color)
# Display surface- Main layer that is displayed to the user
 
# 
# Regular surface-An additional layer that can be attached.


#2. Game loop-Every cycle moves an image. All games run in the loop.


#General setup
pygame.init()
clock = pygame.time.Clock() # how fast the game runs

#Create the display surface
screen = pygame.display.set_mode((600,600)) # tuple with width and height of screen
second_surface = pygame.Surface([100,200]) #2
second_surface.fill((0,0,255)) #3

piggy = pygame.image.load('piggy.png')
#piggy_rect = piggy.get_rect()  #2 image
piggy_rect = piggy.get_rect(topleft =[100,200])  #5 image
#print(piggy_rect.w)    #2 print image.width
#print(piggy_rect.h)     #2 print image.height
# print(piggy_rect.center) # 2pring image.center
# print(piggy_rect.topleft) # 2 print.image topleft 0,0 relative to the image

while True:   # while loop checks for inputs from user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  #opposite of pygame.init()
            sys.exit()
            
    screen.fill((255,0,255))  # r,g,b from 0, 255
    screen.blit(second_surface,(0,50))   #2 specify second surface for the main
    #screen.blit(piggy,(100,200))  #2
    screen.blit(piggy,piggy_rect)  #4
    piggy_rect.right += 5          #3
    print(piggy_rect.right)        #3
    pygame.display.flip() # draws the game
    clock.tick(60)        # frame rate 60 milli sec. speed of animation