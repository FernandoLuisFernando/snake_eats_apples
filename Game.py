import pygame, sys

pygame. init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill((0,0,255))
test_rect = test_surface.get_rect(topright = (200,250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((174,215,70))
    test_rect.right += 1
    pygame.draw.rect(screen,pygame.Color('red'), test_rect)
    screen.blit(test_surface,test_rect)    
    pygame.display.update()
    clock.tick(60)