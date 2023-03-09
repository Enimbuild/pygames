import pygame, sys



#General setup
pygame.init()
clock = pygame.time.Clock() # how fast the game runs

#Create the display surface
screen = pygame.display.set_mode((600,600)) # tuple



while True:   # while loop checks for inputs from user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  #opposite of pygame.init()
            sys.exit()

    screen.fill((0,0,255))  # r,g,b from 0, 255


    pygame.display.flip() # draws the game
    clock.tick(60)        # frame rate 60 milli sec. speed of animation