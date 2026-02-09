import pygame

print('setup da janela comeca')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('janela fecha')

print('looping comeca')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Closse window
            quit() # end pygame




