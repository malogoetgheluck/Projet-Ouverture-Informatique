import pygame
from gameconfig import GameConfig

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,W,H,img,mask):
        self.rect=pygame.Rect(x,y,W,H)
        self.mask=mask
        self.img=img
    def draw(self,window):
        window.blit(self.img,self.rect.topleft)

class Pique(Object):
    def __init__(self,x,y):
        Object.__init__(self,x,y,GameConfig.PIQUE_SIZE,GameConfig.PIQUE_SIZE,GameConfig.PIQUE_IMG,GameConfig.PIQUE_MASK)

#checpoint, collision gérer pour le player, le signal est ensuite envoyer à gamestate puis a background pour sauvegarder
class Checkpoint(Object):
    def __init__(self,x,y):
        Object.__init__(self,x,y,GameConfig.CHECKPOINT_SIZE,GameConfig.CHECKPOINT_SIZE,GameConfig.CHECKPOINT_IMG,GameConfig.CHECKPOINT_MASK)