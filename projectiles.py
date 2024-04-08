from object import Object
import pygame
from enemies import Enemies
from gameconfig import GameConfig


class PiegeProjectile(pygame.sprite.Sprite):
    def __init__(self,x,y,sens):
        self.arrow=[]
        #sens haut bas gauche droite
        self.sens=sens

        self.H,self.W=GameConfig.PIEGE_SIZE,GameConfig.PIEGE_SIZE
        pygame.sprite.Sprite.__init__(self)
        self.rect=pygame.Rect(x,y,self.W,self.H)

        self.x=x
        self.y=y
        self.sprites_num=GameConfig.NB_FRAMES_PER_SPRITE_PIEGE
        self.sprites_count=0

        #définie le point d'apparition des flèches,leur vitesse en x et y, leur image,celle du piège
        if self.sens==Enemies.UP:
            self.arrowx=x
            self.arrowy=y-GameConfig.ARROW_SIZE
            self.arrow_move_x=0
            self.arrow_move_y=-GameConfig.ARROW_SPEED

            self.image=GameConfig.PIEGE_IMG_UP[0]
            self.mask=GameConfig.PIEGE_MASKS_UP[0]
            self.ar_image=GameConfig.ARROW_IMG_UP
            self.ar_mask=GameConfig.ARROW_MASK_UP

        if self.sens==Enemies.LEFT:
            self.arrowx=x-GameConfig.ARROW_SIZE
            self.arrowy=y
            self.arrow_move_x=-GameConfig.ARROW_SPEED
            self.arrow_move_y=0

            self.image=GameConfig.PIEGE_IMG_LEFT[0]
            self.mask=GameConfig.PIEGE_MASKS_LEFT[0]
            self.ar_image=GameConfig.ARROW_IMG_LEFT
            self.ar_mask=GameConfig.ARROW_MASK_LEFT

        if self.sens==Enemies.RIGHT:
            self.arrowx=x+GameConfig.PIEGE_SIZE
            self.arrowy=y
            self.arrow_move_x=GameConfig.ARROW_SPEED
            self.arrow_move_y=0

            self.image=GameConfig.PIEGE_IMG_RIGHT[0]
            self.mask=GameConfig.PIEGE_MASKS_RIGHT[0]
            self.ar_image=GameConfig.ARROW_IMG_RIGHT
            self.ar_mask=GameConfig.ARROW_MASK_RIGHT

        if self.sens==Enemies.DOWN:
            self.arrowx=x
            self.arrowy=y+GameConfig.ARROW_SIZE
            self.arrow_move_x=0
            self.arrow_move_y=GameConfig.ARROW_SPEED

            self.image=GameConfig.PIEGE_IMG_DOWN[0]
            self.mask=GameConfig.PIEGE_MASKS_DOWN[0]
            self.ar_image=GameConfig.ARROW_IMG_DOWN
            self.ar_mask=GameConfig.ARROW_MASK_DOWN
    def init_sprites():
        PiegeProjectile.PIEGE_IMAGES={Enemies.LEFT :GameConfig.PIEGE_IMG_LEFT,
        Enemies.RIGHT :GameConfig.PIEGE_IMG_RIGHT,
        Enemies.UP :GameConfig.PIEGE_IMG_UP,
        Enemies.DOWN :GameConfig.PIEGE_IMG_DOWN}

        PiegeProjectile.PIEGE_MASKS={Enemies.LEFT :GameConfig.PIEGE_MASKS_LEFT,
        Enemies.RIGHT :GameConfig.PIEGE_MASKS_RIGHT,
        Enemies.UP :GameConfig.PIEGE_MASKS_UP,
        Enemies.DOWN :GameConfig.PIEGE_MASKS_DOWN}
        #gère l'animation,l'envoie des lèche et avance chaque flèche lancées
    def advance_state(self,mur):
        self.sprites_count+=1
        if self.sprites_count==len(PiegeProjectile.PIEGE_IMAGES[Enemies.DOWN])*self.sprites_num:
            self.sprites_count=0
        self.image = PiegeProjectile.PIEGE_IMAGES[self.sens][self.sprites_count//self.sprites_num]
        self.mask = PiegeProjectile.PIEGE_IMAGES[self.sens] [self.sprites_count//self.sprites_num]
        if self.sprites_count==0:
            self.arrow.append(Object(self.arrowx,self.arrowy,GameConfig.ARROW_SIZE,GameConfig.ARROW_SIZE,self.ar_image,self.ar_mask))
        for i in self.arrow:
            self.advance_arrow(i,mur)
    
    def draw(self,window):
        window.blit(self.image,(self.x,self.y))
        for i in self.arrow:
            i.draw(window)
    #avance chaque flèche lancées
    def advance_arrow(self,i,mur):
        i.rect=i.rect.move(self.arrow_move_x,self.arrow_move_y)
        if pygame.sprite.collide_mask(mur,i):
            self.arrow.remove(i)