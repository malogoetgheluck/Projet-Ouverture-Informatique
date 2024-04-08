from gameconfig import GameConfig
from enemies import Enemies
class Slime(Enemies):
    def init_sprite():
        Slime.WALK_IMAGES={Enemies.UP: GameConfig.SLIME_IMG,
        Enemies.DOWN: GameConfig.SLIME_IMG,
        Enemies.LEFT: GameConfig.SLIME_IMG,
        Enemies.RIGHT: GameConfig.SLIME_IMG}
        Slime.WALK_MASKS={Enemies.UP: GameConfig.SLIME_MASKS,
        Enemies.DOWN: GameConfig.SLIME_MASKS,
        Enemies.LEFT: GameConfig.SLIME_MASKS,
        Enemies.RIGHT: GameConfig.SLIME_MASKS}

    def __init__(self,x,y,sens,deplacement_pos,deplacement_neg):
        """x y pos de depart, sens 1 droite 2 bas -1 gauche -2 haut direction de depart du slime,
        deplacement pos c'est le nombre de pixel vers les x ou y postif selon le sens """

        self.H=GameConfig.SLIME_H
        self.W=GameConfig.SLIME_W

        #variable de ennemy sprite manager
        self.clas=Slime
        self.sprites_count=0
        self.sprites_num=GameConfig.NB_FRAMES_PER_SPRITE_SLIME
        self.moving=True

        Enemies.__init__(self,x,y,sens)

        self.posxstart=x
        self.posystart=y
        
        self.deplaplus=deplacement_pos
        self.deplamoins=deplacement_neg

        self.image=GameConfig.SLIME_IMG[0]
        self.mask=GameConfig.SLIME_MASKS[0]
        
        """sens si true vas vers les x ou y positif si negatif vers les x ou y negatif """
    def draw_enemie(self,window):
        window.blit(self.image,self.rect.topleft)

    def advance_state(self,popo,popi):
        # gere le mouvement des slime
        if  self.sens==Enemies.RIGHT or self.sens==Enemies.LEFT:
            
            if self.sens==Enemies.RIGHT:
                if self.rect.topleft[0]<self.posxstart+self.deplaplus:
                    self.rect=self.rect.move(GameConfig.SLIME_DEPLACEMENT_DISTANCE,0)
                else:
                    self.sens=Enemies.LEFT
            else:
                if self.rect.topleft[0]>self.posxstart-self.deplamoins:
                    self.rect=self.rect.move(-GameConfig.SLIME_DEPLACEMENT_DISTANCE,0)
                else:
                    self.sens=Enemies.RIGHT
        else:
            
            if self.sens==Enemies.DOWN: 
                if self.rect.topleft[1]<self.posystart+self.deplaplus:
                    self.rect=self.rect.move(0,GameConfig.SLIME_DEPLACEMENT_DISTANCE)
                else:
                    self.sens=Enemies.UP
            else:
                if self.rect.topleft[1]>self.posystart-self.deplamoins:
                    self.rect=self.rect.move(0,-GameConfig.SLIME_DEPLACEMENT_DISTANCE)
                else:
                    self.sens=Enemies.DOWN
        self.enemie_sprite_manager()
    
            
                
                    



    
                    
    
