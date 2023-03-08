import pygame
clock = pygame.time.Clock()

# Initialize Pygame
pygame.init()

# Set the dimensions of the surface
surface = pygame.display.set_mode((600,600))



# Fill the surface with a color (in this case, white)
surface.fill((255, 0, 0))
# Wait for the user to close the window

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
        # Quit Pygame
            pygame.quit()
        
            clock.tick(60)
