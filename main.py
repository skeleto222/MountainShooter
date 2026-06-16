import pygame

print('Game Start')
pygame.init()

window = pygame.display.set_mode(size=(640, 480))
print('Game End')

print('Loop Start')
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ('Quiting...')
            pygame.quit() # Close window
            quit() # End pygame


