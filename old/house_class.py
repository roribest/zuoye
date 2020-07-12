import random
import pygame

class Horse:
    def __init__(self, n, s, img_file, y):
        self.name = n
        self.speed = s
        self.__img_file = pygame.image.load(img_file)
        self.__y = y
        self.__x = 0
    
    
    def run(self):
        self.__x += round( self.speed *random.random())


    def get_image(self):
        return self.__img_file

    
    def get_local(self):
        return (self.__x, self.__y)
