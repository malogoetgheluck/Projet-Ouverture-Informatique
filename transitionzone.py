import pygame

class TransitionZone(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height, salle_suiv, xpos, ypos) :
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, width, height)
        self.img = pygame.transform.scale(pygame.image.load('Ressources/Image_noire.png'),(width, height))
        self.mask = pygame.mask.from_surface(self.img)
        self.salle_suivante = salle_suiv
        self.posx = xpos
        self.posy = ypos