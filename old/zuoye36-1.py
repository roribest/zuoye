import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

img_bg = pygame.image.load('E://Github//zuoye//img//bg.png')
img_cat1 = pygame.image.load('E://Github//zuoye//img//cat_blue.png')
img_cat2 = pygame.image.load('E://Github//zuoye//img//cat_green.png')


i = 0
while True:
    pygame.display.update()
    screen.blit( img_bg,(0,0) )
    screen.blit( img_cat2, (i, 400) )
    i += 100
    pygame.time.delay(200)

    if i >800:
        break

pygame.quit()