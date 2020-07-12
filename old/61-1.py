from house_class import Horse
import pygame

pygame.init()
screen = pygame.display.set_mode( (800, 600) )
img_bg = pygame.image.load("D://py//img//草原.jpg")

h_list = [Horse('海洋饼干', 5, 'D://py//img//1.jpg', 200),
          Horse('魅影', 7, 'D://py//img//2.jpg', 400)]

while True:
    screen.blit( img_bg, (0,0))

    for h in h_list:
        screen.blit(h.get_image(), h.get_local())
        h.run()

    pygame.display.update()
    pygame.time.delay(50)

pygame.quit()
##git hub11111
###git lenovo