import pygame

#class mère avec des des méthode pour tous les enemies
class Enemies(pygame.sprite.Sprite):
    LEFT=-1
    UP=-2
    DOWN=2
    RIGHT=1
    def __init__(self,x,y,sens):
        #initialise le rect
        pygame.sprite.Sprite.__init__(self)
        self.rect=pygame.Rect(x,y,self.W,self.H)
        if sens==1:
            self.sens=Enemies.RIGHT
        elif sens==-1:
            self.sens=Enemies.LEFT
        elif sens==-2:
            self.sens=Enemies.UP
        elif sens==2:
            self.sens=Enemies.DOWN
            #affiche l'enemie
            
    """ gere les sprites pour tous les ennemy en fonction de la class clas, la variable sprite num(temps entre changement de sprite),
    dir la direction ou regarde l'ennemie, et si l'ennemie bouge: booléen self.moving"""
    def enemie_sprite_manager(self):
        if self.moving==True:
            self.sprites_count+=1
            if self.sprites_count>=self.sprites_num*len(self.clas.WALK_IMAGES[self.sens]):
                self.sprites_count=0

            self.image = self.clas.WALK_IMAGES[self.sens][self.sprites_count//self.sprites_num]
            self.mask = self.clas.WALK_MASKS[self.sens] [self.sprites_count//self.sprites_num]
        else:
            self.sprites_count=0
            self.image=self.clas.IDLE_IMAGES[self.sens]
            self.mask=self.clas.IDLE_MASKS[self.sens]
    