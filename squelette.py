from enemies import Enemies
from gameconfig import GameConfig
import pygame
from object import Object


class Squelette(Enemies):
    def __init__(self, x, y,sens):
        #hauteur et largeur du squelette
        self.H=GameConfig.SQUELETTE_H
        self.W=GameConfig.SQUELETTE_W
        
        #nécéssaire pour Enemies(créer le rect)
        self.clas=Squelette
        self.sprites_count=0
        self.sprites_num=GameConfig.NB_FRAMES_PER_SPRITE_SQUELETTE
        self.sprites_attaque_num=GameConfig.NB_FRAMES_PER_SPRITE_ATTAQUE_SQUELETTE
        self.moving=True

        Enemies.__init__(self,x,y,sens)

        self.attaque_player=False
        self.attaque_count=-1
        self.attaque_delay=0
        self.alonge=[]

        self.image = GameConfig.SQUELETTE_WALK_DOWN_IMG[0]
        self.mask = GameConfig.SQUELETTE_WALK_DOWN_MASKS[0]


    # gere les sprites de marche d'idle et d'attaque du squelette
    def init_sprites():
        Squelette.WALK_IMAGES={Enemies.LEFT :GameConfig.SQUELETTE_WALK_LEFT_IMG,
        Enemies.RIGHT :GameConfig.SQUELETTE_WALK_RIGHT_IMG,
        Enemies.UP :GameConfig.SQUELETTE_WALK_UP_IMG,
        Enemies.DOWN :GameConfig.SQUELETTE_WALK_DOWN_IMG}

        Squelette.WALK_MASKS={Enemies.LEFT :GameConfig.SQUELETTE_WALK_LEFT_MASKS,
        Enemies.RIGHT :GameConfig.SQUELETTE_WALK_RIGHT_MASKS,
        Enemies.UP :GameConfig.SQUELETTE_WALK_UP_MASKS,
        Enemies.DOWN :GameConfig.SQUELETTE_WALK_DOWN_MASKS}

        Squelette.ATTAQUE_IMAGES={Enemies.LEFT :GameConfig.SQUELETTE_ATTAQUE_LEFT_IMG,
        Enemies.RIGHT :GameConfig.SQUELETTE_ATTAQUE_RIGHT_IMG,
        Enemies.UP :GameConfig.SQUELETTE_ATTAQUE_UP_IMG,
        Enemies.DOWN :GameConfig.SQUELETTE_ATTAQUE_DOWN_IMG}

        Squelette.ATTAQUE_MASKS={Enemies.LEFT :GameConfig.SQUELETTE_ATTAQUE_LEFT_MASKS,
        Enemies.RIGHT :GameConfig.SQUELETTE_ATTAQUE_RIGHT_MASKS,
        Enemies.UP :GameConfig.SQUELETTE_ATTAQUE_UP_MASKS,
        Enemies.DOWN :GameConfig.SQUELETTE_ATTAQUE_DOWN_MASKS}


        Squelette.IDLE_IMAGES={Enemies.LEFT :GameConfig.SQUELETTE_IDLE_LEFT_IMG,
        Enemies.RIGHT :GameConfig.SQUELETTE_IDLE_RIGHT_IMG,
        Enemies.UP :GameConfig.SQUELETTE_IDLE_UP_IMG,
        Enemies.DOWN :GameConfig.SQUELETTE_IDLE_DOWN_IMG}

        Squelette.IDLE_MASKS={Enemies.LEFT :GameConfig.SQUELETTE_IDLE_LEFT_MASKS,
        Enemies.RIGHT :GameConfig.SQUELETTE_IDLE_RIGHT_MASKS,
        Enemies.UP :GameConfig.SQUELETTE_IDLE_UP_MASKS,
        Enemies.DOWN :GameConfig.SQUELETTE_IDLE_DOWN_MASKS}


        Squelette.ALLONGE_IMAGES={Enemies.LEFT :GameConfig.SQUELETTE_ALLONGE_LEFT_IMG,
        Enemies.RIGHT :GameConfig.SQUELETTE_ALLONGE_RIGHT_IMG,
        Enemies.UP :GameConfig.SQUELETTE_ALLONGE_UP_IMG,
        Enemies.DOWN :GameConfig.SQUELETTE_ALLONGE_DOWN_IMG}

        Squelette.ALLONGE_MASKS={Enemies.LEFT :GameConfig.SQUELETTE_ALLONGE_LEFT_MASKS,
        Enemies.RIGHT :GameConfig.SQUELETTE_ALLONGE_RIGHT_MASKS,
        Enemies.UP :GameConfig.SQUELETTE_ALLONGE_UP_MASKS,
        Enemies.DOWN :GameConfig.SQUELETTE_ALLONGE_DOWN_MASKS}



    def draw_enemie(self,window):
            if self.attaque_count>=0:
                for i in self.alonge:
                    i.draw(window)
            window.blit(self.image,self.rect.topleft)
    def attack_lunch(self):
        if self.attaque_delay==0:
            self.attaque_player=True
            self.moving=False
            self.attaque_count=-GameConfig.SQUELETTE_DELAY_ATTAQUE

    def squelette_attack(self):
        self.attaque_count+=1
        if self.attaque_count==0:
            xp,yp=self.rect.topleft
            # creer une lame paramètre de Object ,x,y,H,W,img,mask
            if self.sens==Enemies.LEFT:
                
                self.alonge.append(Object(xp-GameConfig.S_ATTAQUE_SIZE/2+16,yp-GameConfig.S_ATTAQUE_SIZE/2+39,GameConfig.S_ATTAQUE_SIZE,
                GameConfig.S_ATTAQUE_SIZE,GameConfig.SQUELETTE_ALLONGE_LEFT_IMG[0],GameConfig.SQUELETTE_ALLONGE_LEFT_MASKS[0]))

            if self.sens==Enemies.RIGHT:
                
                self.alonge.append(Object(xp-GameConfig.S_ATTAQUE_SIZE/2+53,yp-GameConfig.S_ATTAQUE_SIZE/2+39,GameConfig.S_ATTAQUE_SIZE,
                GameConfig.S_ATTAQUE_SIZE,GameConfig.SQUELETTE_ALLONGE_RIGHT_IMG[0],GameConfig.SQUELETTE_ALLONGE_RIGHT_MASKS[0]))

            if self.sens==Enemies.UP:
                self.alonge.append(Object(xp-GameConfig.S_ATTAQUE_SIZE/2+35,yp-GameConfig.S_ATTAQUE_SIZE/2+14,GameConfig.S_ATTAQUE_SIZE,
                GameConfig.S_ATTAQUE_SIZE,GameConfig.SQUELETTE_ALLONGE_UP_IMG[0],GameConfig.SQUELETTE_ALLONGE_UP_MASKS[0]))

            if self.sens==Enemies.DOWN:
                
                self.alonge.append(Object(xp-GameConfig.S_ATTAQUE_SIZE/2+29,yp-GameConfig.S_ATTAQUE_SIZE/2+53,GameConfig.S_ATTAQUE_SIZE,
                GameConfig.S_ATTAQUE_SIZE,GameConfig.SQUELETTE_ALLONGE_DOWN_IMG[0],GameConfig.SQUELETTE_ALLONGE_DOWN_MASKS[0]))
                
        if self.attaque_count>=0:
            self.attack_sprites_manager()
        else:
            self.enemie_sprite_manager()
            #delay avant d'attaquer pour donner une chance au joueur

            #gère un delay entre les attack et suprime la lame a la fin de l'attaque
        if self.attaque_player==False:
            self.attaque_delay=30
            self.alonge = []
            
# systeme de gestion collision avec les mur
# dir direction suivante du squelette en cas de touche,x,y antidirection de mvt (pour le faire revenir dans l'aire de jeu)
    def collision(self,dir,x,y,mur):
        if pygame.sprite.collide_mask(self,mur):
            while pygame.sprite.collide_mask(self,mur):
                self.rect=self.rect.move(x,y) 
            self.sens=dir
        
    def attack_sprites_manager(self):
        if self.attaque_count>=self.sprites_attaque_num*len(Squelette.ALLONGE_IMAGES[self.sens]):
            self.attaque_count=-1
            self.attaque_player=False
            self.moving=True

        self.image = self.clas.ATTAQUE_IMAGES[self.sens][0]#self.attaque_count//self.sprites_attaque_num]
        self.mask = self.clas.ATTAQUE_MASKS[self.sens][0]#self.attaque_count//self.sprites_attaque_num]

        for i in self.alonge:
            i.img=self.clas.ALLONGE_IMAGES[self.sens][self.attaque_count//self.sprites_attaque_num]
            i.mask = self.clas.ALLONGE_MASKS[self.sens][self.attaque_count//self.sprites_attaque_num]    




    def advance_state(self,centeraim,mur):
        x,y=centeraim
        xp,yp=self.rect.center
        #ia
        if not self.attaque_player and self.sens==Enemies.RIGHT:
            
            if x-xp>=GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4:
                self.rect=self.rect.move(GameConfig.SQUELETTE_DEPLACEMENT_DISTANCE,0)
                #regarde si il s'approche du joueur juste avec la composante x
                #si collision on reverse le deplacement et on passe au prochain sens ex UP
                self.collision(Enemies.UP,-1,0,mur)


                #mieux avec SQUELETTE_W a la place du zero mais donne du temps au joueur d'attaquer le squelette
            elif 0<x-xp<GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4 and  GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_H*3/4>=abs(y-yp)>=GameConfig.SQUELETTE_H/2:
                self.rect=self.rect.move(GameConfig.SQUELETTE_DEPLACEMENT_DISTANCE,0)
                #regarde si le joueur n'est pas dans la diagonale proche du squelette 
                
                #si collision on reverse le deplacement et on passe au prochain sens ex UP
                self.collision(Enemies.UP,-1,0,mur)

            elif 0<x-xp<GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4 and  GameConfig.SQUELETTE_H/2>abs(y-yp):
                self.attack_lunch()
                #lance l'attaque

            else:
                self.sens=Enemies.UP


        if not self.attaque_player and self.sens==Enemies.UP:
            if yp-y>=GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_H*3/4:
                self.rect=self.rect.move(0,-GameConfig.SQUELETTE_DEPLACEMENT_DISTANCE)

                self.collision(Enemies.UP,0,1,mur)

            elif 0<yp-y<GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_H*3/4 and  GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4>=abs(x-xp)>=GameConfig.SQUELETTE_W/2:
                self.rect=self.rect.move(0,-GameConfig.SQUELETTE_DEPLACEMENT_DISTANCE)

                self.collision(Enemies.UP,0,1,mur)

            elif 0<yp-y<GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_H*3/4 and  GameConfig.SQUELETTE_W/2>=abs(x-xp):
                self.attack_lunch()

            else:
                self.sens=Enemies.LEFT


        if not self.attaque_player and self.sens==Enemies.LEFT:
            if xp-x>=GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4:
                self.rect=self.rect.move(-GameConfig.SQUELETTE_DEPLACEMENT_DISTANCE,0)
                self.collision(Enemies.UP,1,0,mur)

            elif 0<xp-x<GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4 and  GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_H*3/4>=abs(y-yp)>=GameConfig.SQUELETTE_H/2:
                self.rect=self.rect.move(-GameConfig.SQUELETTE_DEPLACEMENT_DISTANCE,0)

                self.collision(Enemies.UP,1,0,mur)

            elif 0<xp-x<GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4 and  GameConfig.SQUELETTE_H/2>abs(y-yp):
                self.attack_lunch()

            else:
                self.sens=Enemies.DOWN


        if not self.attaque_player and self.sens==Enemies.DOWN:
            if y-yp>=GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_H*3/4:
                self.rect=self.rect.move(0,GameConfig.SQUELETTE_DEPLACEMENT_DISTANCE)
                
                self.collision(Enemies.UP,0,-1,mur)

            elif 0<y-yp<GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4 and  GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4>abs(x-xp)>GameConfig.SQUELETTE_W/2:
                self.rect=self.rect.move(0,GameConfig.SQUELETTE_DEPLACEMENT_DISTANCE)

                self.collision(Enemies.UP,0,-1,mur)
                

            elif 0<y-yp<GameConfig.SQUELETTE_A_RANGE+GameConfig.SQUELETTE_W*3/4 and  GameConfig.SQUELETTE_W/2>abs(x-xp):
                self.attack_lunch()
                
            else:
                self.sens=Enemies.RIGHT

        #gestion de l'attaque
        if self.attaque_player:
            self.squelette_attack()
        else:
            self.enemie_sprite_manager()
            if self.attaque_delay !=0:
                self.attaque_delay-=1

        
        
        

        
