import pygame
from gameconfig import GameConfig

class Wall(pygame.sprite.Sprite) :
    #initialise le wall
    def __init__(self,img) :
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, GameConfig.WINDOW_W, GameConfig.WINDOW_H)
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    #permet d'afficher le mur
    def draw(self, window) :
        window.blit(self.img,(0,0))