import random
import pygame

class Funs:
    def __init__(self, img_file,x, y):
        self.__img_file = pygame.image.load(img_file)
        self.__y = y
        self.__x = x
    
    
    def dance(self):
        self.__y += random.randint(-10, 10)


    def get_image(self):
        return self.__img_file

    
    def get_local(self):
        return (self.__x, self.__y)
