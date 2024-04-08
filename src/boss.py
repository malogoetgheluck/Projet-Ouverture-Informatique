from enemies import Enemies
from gameconfig import GameConfig
import pygame
from object import Object
from background import Background
from door import Coffre


class Boss(Enemies):
    def __init__(self, x, y,sens):
        #hauteur et largeur du boss
        self.H=GameConfig.BOSS_SIZE
        self.W=GameConfig.BOSS_SIZE
        
        #nécéssaire pour Enemies(créer le rect)
        self.clas=Boss
        self.sprites_count=0
        self.sprites_num=GameConfig.NB_FRAMES_PER_SPRITE_SQUELETTE
        self.sprites_attaque_num=GameConfig.NB_FRAMES_PER_SPRITE_ATTAQUE_BOSS
        self.moving=True

        Enemies.__init__(self,x,y,sens)

        #initialisation des variable de l'attaque
        self.attaque_player=False
        self.attaque_count=-1
        self.attaque_delay=0
        self.alonge=[]

        self.image = GameConfig.BOSS_WALK_LEFT_IMG[0]
        self.mask = GameConfig.BOSS_WALK_LEFT_MASKS[0]

        #variable des mécaniques exclusive au boss: drop un coffre, à des vies, se supprime de la sauvegarde
        self.x=x
        self.y=y
        self.ini_sens=sens
        self.defence_delay=10
        self.life=5


    # gere les sprites de marche d'idle et d'attaque du boss
    def init_sprites():
        Boss.WALK_IMAGES={Enemies.LEFT :GameConfig.BOSS_WALK_LEFT_IMG,
        Enemies.RIGHT :GameConfig.BOSS_WALK_RIGHT_IMG,
        Enemies.UP :GameConfig.BOSS_WALK_UP_IMG,
        Enemies.DOWN :GameConfig.BOSS_WALK_DOWN_IMG}

        Boss.WALK_MASKS={Enemies.LEFT :GameConfig.BOSS_WALK_LEFT_MASKS,
        Enemies.RIGHT :GameConfig.BOSS_WALK_RIGHT_MASKS,
        Enemies.UP :GameConfig.BOSS_WALK_UP_MASKS,
        Enemies.DOWN :GameConfig.BOSS_WALK_DOWN_MASKS}

        Boss.ATTAQUE_IMAGES={Enemies.LEFT :GameConfig.BOSS_ATTAQUE_LEFT_IMG,
        Enemies.RIGHT :GameConfig.BOSS_ATTAQUE_RIGHT_IMG,
        Enemies.UP :GameConfig.BOSS_ATTAQUE_UP_IMG,
        Enemies.DOWN :GameConfig.BOSS_ATTAQUE_DOWN_IMG}

        Boss.ATTAQUE_MASKS={Enemies.LEFT :GameConfig.BOSS_ATTAQUE_LEFT_MASKS,
        Enemies.RIGHT :GameConfig.BOSS_ATTAQUE_RIGHT_MASKS,
        Enemies.UP :GameConfig.BOSS_ATTAQUE_UP_MASKS,
        Enemies.DOWN :GameConfig.BOSS_ATTAQUE_DOWN_MASKS}


        Boss.IDLE_IMAGES={Enemies.LEFT :GameConfig.BOSS_IDLE_LEFT_IMG,
        Enemies.RIGHT :GameConfig.BOSS_IDLE_RIGHT_IMG,
        Enemies.UP :GameConfig.BOSS_IDLE_UP_IMG,
        Enemies.DOWN :GameConfig.BOSS_IDLE_DOWN_IMG}

        Boss.IDLE_MASKS={Enemies.LEFT :GameConfig.BOSS_IDLE_LEFT_MASKS,
        Enemies.RIGHT :GameConfig.BOSS_IDLE_RIGHT_MASKS,
        Enemies.UP :GameConfig.BOSS_IDLE_UP_MASKS,
        Enemies.DOWN :GameConfig.BOSS_IDLE_DOWN_MASKS}


        Boss.ALLONGE_IMAGES={Enemies.LEFT :GameConfig.BOSS_ALLONGE_LEFT_IMG,
        Enemies.RIGHT :GameConfig.BOSS_ALLONGE_RIGHT_IMG,
        Enemies.UP :GameConfig.BOSS_ALLONGE_UP_IMG,
        Enemies.DOWN :GameConfig.BOSS_ALLONGE_DOWN_IMG}

        Boss.ALLONGE_MASKS={Enemies.LEFT :GameConfig.BOSS_ALLONGE_LEFT_MASKS,
        Enemies.RIGHT :GameConfig.BOSS_ALLONGE_RIGHT_MASKS,
        Enemies.UP :GameConfig.BOSS_ALLONGE_UP_MASKS,
        Enemies.DOWN :GameConfig.BOSS_ALLONGE_DOWN_MASKS}



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


    def boss_attack(self):
        self.attaque_count+=1
        if self.attaque_count==0:
            xp,yp=self.rect.topleft
            # creer une lame paramètre de Object ,x,y,H,W,img,mask
            if self.sens==Enemies.LEFT:
                
                self.alonge.append(Object(xp-GameConfig.B_ATTAQUE_SIZE/2-20,yp-GameConfig.B_ATTAQUE_SIZE/2+50,GameConfig.B_ATTAQUE_SIZE,
                GameConfig.B_ATTAQUE_SIZE,GameConfig.BOSS_ALLONGE_LEFT_IMG[0],GameConfig.BOSS_ALLONGE_LEFT_MASKS[0]))

            if self.sens==Enemies.RIGHT:
                
                self.alonge.append(Object(xp-GameConfig.B_ATTAQUE_SIZE/2+80,yp-GameConfig.B_ATTAQUE_SIZE/2+50,GameConfig.B_ATTAQUE_SIZE,
                GameConfig.B_ATTAQUE_SIZE,GameConfig.BOSS_ALLONGE_RIGHT_IMG[0],GameConfig.BOSS_ALLONGE_RIGHT_MASKS[0]))

            if self.sens==Enemies.UP:
                self.alonge.append(Object(xp-GameConfig.B_ATTAQUE_SIZE/2+35,yp-GameConfig.B_ATTAQUE_SIZE/2-50,GameConfig.B_ATTAQUE_SIZE,
                GameConfig.S_ATTAQUE_SIZE,GameConfig.BOSS_ALLONGE_UP_IMG[0],GameConfig.BOSS_ALLONGE_UP_MASKS[0]))

            if self.sens==Enemies.DOWN:
                
                self.alonge.append(Object(xp-GameConfig.B_ATTAQUE_SIZE/2+29,yp-GameConfig.B_ATTAQUE_SIZE/2+100,GameConfig.B_ATTAQUE_SIZE,
                GameConfig.B_ATTAQUE_SIZE,GameConfig.BOSS_ALLONGE_DOWN_IMG[0],GameConfig.BOSS_ALLONGE_DOWN_MASKS[0]))
                
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
        if self.attaque_count>=self.sprites_attaque_num*len(Boss.ALLONGE_IMAGES[self.sens]):
            self.attaque_count=-1
            self.attaque_player=False
            self.moving=True

        #il n'a a pas d'animation d'attaque (une seule image mais c'était prévue)
        self.image = self.clas.ATTAQUE_IMAGES[self.sens][0]#self.attaque_count//self.sprites_attaque_num]
        self.mask = self.clas.ATTAQUE_MASKS[self.sens][0]#self.attaque_count//self.sprites_attaque_num]

        for i in self.alonge:
            i.img=self.clas.ALLONGE_IMAGES[self.sens][self.attaque_count//self.sprites_attaque_num]
            i.mask = self.clas.ALLONGE_MASKS[self.sens][self.attaque_count//self.sprites_attaque_num]
    
    def est_touche(self,alonge,salle,inlist,chestlist):
        for i in alonge:
            if pygame.sprite.collide_mask(self,i) and self.defence_delay<=0:
                self.life-=1
                self.defence_delay=10
                if self.life==0:
                    Background.data_salles[salle][1]["boss"].remove((self.x,self.y,self.ini_sens))
                    inlist.remove(self)
                    Background.data_salles[salle][2]["coffre"]=[(self.x,self.y,"cle Salle_018")]
                    chestlist.append(Coffre(self.x,self.y,"cle Salle_018"))
        
        self.defence_delay-=1
            




    def advance_state(self,centeraim,mur,alonge,salle,inlist,chestlist):
        x,y=centeraim
        xp,yp=self.rect.center
        #ia
        if not self.attaque_player and self.sens==Enemies.RIGHT:
            
            if x-xp>=GameConfig.BOSS_A_RANGE/2+GameConfig.BOSS_SIZE*1/4:
                self.rect=self.rect.move(GameConfig.BOSS_DEPLACEMENT_DISTANCE,0)
                self.collision(Enemies.UP,-1,0,mur)

            elif GameConfig.BOSS_SIZE/4<x-xp<GameConfig.BOSS_SIZE/4+GameConfig.BOSS_A_RANGE/2 and GameConfig.BOSS_SIZE/2<abs(y-yp)<GameConfig.BOSS_SIZE/2+GameConfig.BOSS_A_RANGE/2:
                self.rect=self.rect.move(GameConfig.BOSS_DEPLACEMENT_DISTANCE,0)
                self.collision(Enemies.UP,-1,0,mur)

            elif 0<=x-xp<=GameConfig.BOSS_A_RANGE/2+GameConfig.BOSS_SIZE*1/4 and  GameConfig.BOSS_SIZE/4>=abs(y-yp):
                self.attack_lunch()
                #lance l'attaque

            else:
                self.sens=Enemies.UP


        if not self.attaque_player and self.sens==Enemies.UP:
            if yp-y>=GameConfig.BOSS_A_RANGE/2+GameConfig.BOSS_SIZE*1/2:
                self.rect=self.rect.move(0,-GameConfig.BOSS_DEPLACEMENT_DISTANCE)

                self.collision(Enemies.UP,0,1,mur)

            elif  GameConfig.BOSS_SIZE/4<yp-y<GameConfig.BOSS_SIZE/2 and GameConfig.BOSS_SIZE/4<abs(x-xp)<GameConfig.BOSS_SIZE/4+GameConfig.BOSS_A_RANGE/2:
                self.rect=self.rect.move(0,-GameConfig.BOSS_DEPLACEMENT_DISTANCE)

                self.collision(Enemies.UP,0,1,mur)

            elif 0<=yp-y<=GameConfig.BOSS_A_RANGE/2+GameConfig.BOSS_SIZE*1/2 and  GameConfig.BOSS_SIZE/4>=abs(x-xp):
                self.attack_lunch()

            else:
                self.sens=Enemies.LEFT


        if not self.attaque_player and self.sens==Enemies.LEFT:
            if xp-x>=GameConfig.BOSS_A_RANGE/2+GameConfig.BOSS_SIZE*1/4:
                self.rect=self.rect.move(-GameConfig.BOSS_DEPLACEMENT_DISTANCE,0)
                self.collision(Enemies.UP,1,0,mur)

            elif GameConfig.BOSS_SIZE/4<xp-x<GameConfig.BOSS_SIZE/4+GameConfig.BOSS_A_RANGE/2 and GameConfig.BOSS_SIZE/2<abs(y-yp)<GameConfig.BOSS_SIZE/2+GameConfig.BOSS_A_RANGE/2:
                self.rect=self.rect.move(-GameConfig.BOSS_DEPLACEMENT_DISTANCE,0)

                self.collision(Enemies.UP,1,0,mur)

            elif 0<=xp-x<=GameConfig.BOSS_A_RANGE/2+GameConfig.BOSS_SIZE*1/4 and  GameConfig.BOSS_SIZE/4>=abs(y-yp):
                self.attack_lunch()

            else:
                self.sens=Enemies.DOWN


        if not self.attaque_player and self.sens==Enemies.DOWN:
            if y-yp>=GameConfig.BOSS_A_RANGE/2+20+GameConfig.BOSS_SIZE*1/4:
                self.rect=self.rect.move(0,GameConfig.BOSS_DEPLACEMENT_DISTANCE)
                
                self.collision(Enemies.UP,0,-1,mur)

            elif GameConfig.BOSS_SIZE/4<y-yp<GameConfig.BOSS_SIZE/2 and GameConfig.BOSS_SIZE/4<abs(x-xp)<GameConfig.BOSS_SIZE/4+GameConfig.BOSS_A_RANGE/2:
                self.rect=self.rect.move(0,GameConfig.BOSS_DEPLACEMENT_DISTANCE)

                self.collision(Enemies.UP,0,-1,mur)
                

            elif 0<=y-yp<GameConfig.BOSS_A_RANGE/2+20+GameConfig.BOSS_SIZE*1/4 and  GameConfig.BOSS_SIZE/4>=abs(x-xp):
                self.attack_lunch()
                
            else:
                self.sens=Enemies.RIGHT

        #gestion de l'attaque
        if self.attaque_player:
            self.boss_attack()
        else:
            self.enemie_sprite_manager()
            if self.attaque_delay !=0:
                self.attaque_delay-=1
        #gestion des vie
        self.est_touche(alonge,salle,inlist,chestlist)