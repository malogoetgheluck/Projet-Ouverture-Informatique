import pygame
from gameconfig import GameConfig
from background import Background
from transitionzone import TransitionZone
from message import Message

class Door(pygame.sprite.Sprite):
    def __init__(self,x,y,sens,code,futursal,futurpos):
        pygame.sprite.Sprite.__init__(self)
        self.rect=pygame.Rect(x,y,GameConfig.DOOR_SIZE,GameConfig.DOOR_SIZE)
        (x,y) = self.rect.topleft

        #gère l'image et la zone de transition qui sera créer si la porte est ouverte
        #code haut bas gauche ou droite(direction de la porte),future salle: salle vers laquelle pointera la zone de transition,
        # futurepos:position une fois la transition effectuée
        if sens==1:
            self.img=GameConfig.PORTE_IMG_RIGHT
            self.mask=GameConfig.PORTE_MASK_RIGHT
            self.futurtranspos = [(x+GameConfig.DOOR_SIZE,y),(x+GameConfig.DOOR_SIZE,y+GameConfig.DOOR_SIZE)]
        elif sens==-1:
            self.img=GameConfig.PORTE_IMG_LEFT
            self.mask=GameConfig.PORTE_MASK_LEFT
            self.futurtranspos = [(x-1,y),(x-1,y+GameConfig.DOOR_SIZE)]
        elif sens==-2:
            self.img=GameConfig.PORTE_IMG_UP
            self.mask=GameConfig.PORTE_MASK_UP
            self.futurtranspos = [(x,y-1),(x+GameConfig.DOOR_SIZE,y-1)]
        elif sens==2:
            self.img=GameConfig.PORTE_IMG_DOWN
            self.mask=GameConfig.PORTE_MASK_DOWN
            self.futurtranspos = [(x,y+GameConfig.DOOR_SIZE),(x+GameConfig.DOOR_SIZE,y+GameConfig.DOOR_SIZE)]
        self.salletrans = futursal
        self.postrans = futurpos
        self.code=code
        self.sens=sens
        self.x,self.y=x,y

    def advance_state(self,keycode,salle,inlist,list_trans):
        #si le player a la clés dans keycode_list, enlève l'objet porte de la save et de la salle, 
        # rajoute a la liste de transition et a la save la zone de transition
        for i in keycode:
            if i == self.code:
                Background.data_salles[salle][2]["porte"].remove((self.x,self.y,self.sens,self.code,self.salletrans,self.postrans))
                Background.data_salles[salle][3].append((self.futurtranspos,self.salletrans,self.postrans))
                inlist.remove(self)
                ([(x1,y1),(x2,y2)],salle_suiv,(xpos,ypos)) = (self.futurtranspos,self.salletrans,self.postrans)
                list_trans.append(TransitionZone(x1,y1,x2-x1+1,y2-y1+1,salle_suiv,xpos,ypos))
    def draw(self,window):
        window.blit(self.img,self.rect.topleft)



class Coffre(pygame.sprite.Sprite):
    def __init__(self,x,y,code):
        #code comme door
        pygame.sprite.Sprite.__init__(self)
        self.rect=pygame.Rect(x,y,GameConfig.COFFRE_SIZE,GameConfig.COFFRE_SIZE)
        self.img=GameConfig.CHEST_IMG
        self.mask=GameConfig.CHEST_MASK
        self.code=code
        self.sprite_num=0
        self.open_annimation=False
        self.x=x
        self.y=y
    
    def advance_state(self,player,salle,inlist,list_mess):
        if self.open_annimation:
            self.sprite_manager()
            if self.sprite_num==len(GameConfig.CHEST_OPEN)*GameConfig.INTER_FRAME_CHEST:
                Background.data_salles[salle][2]["coffre"].remove((self.x,self.y,self.code))
                if len(Background.data_salles[salle][2]["coffre"])==0:
                    del Background.data_salles[salle][2]["coffre"]
                inlist.remove(self)
        # le else regarde si le joueur touche le coffre si oui donne l'épee ou une clée 
        # ensuite le if détruit le coffre de la save et de la salle après l'animation
        else:
            if pygame.sprite.collide_mask(self,player):
                if self.code == "epee":
                    self.open_annimation=True
                    list_mess.append(Message((64,704),"Vous avez obtenu l'épée !",200,30))
                    list_mess.append(Message((64,734),"Appuyez sur espace pour attaquer",200,20))
                    return True
                elif self.code not in player.keycode_list:
                    player.keycode_list.append(self.code)
                    list_mess.append(Message((64,704),"Vous avez obtenu une clé !",200,30))
                self.open_annimation=True
        return False
        
        
    def draw(self,window):
        window.blit(self.img,self.rect.topleft)
    def sprite_manager(self):
        self.img=GameConfig.CHEST_OPEN[self.sprite_num//GameConfig.INTER_FRAME_CHEST]
        self.sprite_num+=1
        