import pygame
from slime import Slime
from gameconfig import GameConfig
from squelette import Squelette
from player import Player
from background import Background
from wall import Wall
from transitionzone import TransitionZone
from projectiles import PiegeProjectile
from door import Coffre
from door import Door
from object import Pique
from object import Checkpoint
from boss import Boss

class GameState:
    def __init__(self,save):
        
        Background.init(save)
        Player.init_sprites()
        Slime.init_sprite()
        Squelette.init_sprites()
        Boss.init_sprites()
        PiegeProjectile.init_sprites()
        
        x,y = Background.data_depart["Position"]
        inventaire = Background.data_depart["Clees"]
        self.player = Player(x, y, inventaire)
        self.salle_actuelle = Background.data_depart["Salle"]
        self.poss_epee = Background.data_depart["Epee"]
        
        self.enemies_list = []
        Ennemis = Background.data_salles[self.salle_actuelle][1]
        for cle,valeur in Ennemis.items():
            if cle == "slime":
                for donnees_mob in valeur:
                    (v1,v2,v3,v4,v5) = donnees_mob
                    self.enemies_list.append(Slime(v1,v2,v3,v4,v5))
            elif cle == "squelette":
                for donnees_mob in valeur:
                    (v1,v2,v3) = donnees_mob
                    self.enemies_list.append(Squelette(v1,v2,v3))
            elif cle == "boss":
                for donnees_mob in valeur:
                    (v1,v2,v3) = donnees_mob
                    self.enemies_list.append(Boss(v1,v2,v3))
        
        self.mur = Wall(pygame.transform.scale(pygame.image.load(Background.data_salles[self.salle_actuelle][0][0]),(GameConfig.WINDOW_W,GameConfig.WINDOW_H)).convert_alpha())
        self.img_sol = pygame.transform.scale(pygame.image.load(Background.data_salles[self.salle_actuelle][0][1]),(GameConfig.WINDOW_W,GameConfig.WINDOW_H)).convert_alpha()
        
        self.zone_transition = []
        for zone in Background.data_salles[self.salle_actuelle][3]:
            ([(x1,y1),(x2,y2)],salle_suiv,(xpos,ypos)) = zone
            self.zone_transition.append(TransitionZone(x1,y1,x2-x1+1,y2-y1+1,salle_suiv,xpos,ypos))

        self.piege_fleche = []
        self.chest=[]
        self.door=[]
        self.piques=[]
        self.checkpoint = []
        for cle,valeur in Background.data_salles[self.salle_actuelle][2].items():
            if cle == "fleche":
                for (x,y,sens) in valeur:
                    self.piege_fleche.append(PiegeProjectile(x,y,sens))
            elif cle == "coffre":
                        for (x,y,code) in valeur:
                            self.chest.append(Coffre(x,y,code))
            elif cle=="porte":
                        for (x,y,sens,code,fut_salle,pos) in valeur:
                            self.door.append(Door(x,y,sens,code,fut_salle,pos))
            elif cle=="piques":
                        for (x,y) in valeur:
                            self.piques.append(Pique(x,y))
            elif cle =="checkpoint":
                (x,y)=valeur
                self.checkpoint.append(Checkpoint(x,y))
        
        self.messages = []


    def draw(self, window) :
        window.blit(self.img_sol,(0,0))
        Wall.draw(self.mur, window)
        for pique in self.piques:
            pique.draw(window)
        for enemies in self.enemies_list:
            enemies.draw_enemie(window)
        self.player.draw(window)
        for piege in self.piege_fleche:
            piege.draw(window)
        for chest in self.chest:
            chest.draw(window)
        for door in self.door:
            door.draw(window)
        for checkpoint in self.checkpoint:
            checkpoint.draw(window)
        for message in self.messages:
            message.draw(window)
        if self.player.life == 3 :
            window.blit(GameConfig.LIFE,(128,0))
        if self.player.life >= 2 :
            window.blit(GameConfig.LIFE,(64,0))
        if self.player.life >= 1 :
            window.blit(GameConfig.LIFE,(0,0))

    def advance_state(self, next_move) :
        self.player.advance_state(next_move, self.enemies_list, self.mur, self.piques, self.piege_fleche, self.poss_epee)
        for enemies in self.enemies_list:
            if enemies.clas==Boss:
                enemies.advance_state(self.player.rect.center, self.mur,self.player.alonge,self.salle_actuelle,self.enemies_list,self.chest)
            else:
                enemies.advance_state(self.player.rect.center, self.mur)
        for piege in self.piege_fleche:
            piege.advance_state(self.mur)
        for chest in self.chest:
            if chest.advance_state(self.player,self.salle_actuelle,self.chest,self.messages):
                self.poss_epee = "oui"
        for door in self.door:
            door.advance_state(self.player.keycode_list,self.salle_actuelle,self.door,self.zone_transition)
        for message in self.messages:
            message.advance_state(self.messages)

        for zone_trans in self.zone_transition:
            if self.player.collide_trans(zone_trans):
                #Le joueur change de salle
                self.salle_actuelle = zone_trans.salle_suivante
                self.mur = Wall(pygame.transform.scale(pygame.image.load(Background.data_salles[self.salle_actuelle][0][0]),(GameConfig.WINDOW_W,GameConfig.WINDOW_H)).convert_alpha())
                self.img_sol = pygame.transform.scale(pygame.image.load(Background.data_salles[self.salle_actuelle][0][1]),(GameConfig.WINDOW_W,GameConfig.WINDOW_H)).convert_alpha()
        
                self.zone_transition = []
                for zone in Background.data_salles[self.salle_actuelle][3]:
                    ([(x1,y1),(x2,y2)],salle_suiv,(xpos,ypos)) = zone
                    self.zone_transition.append(TransitionZone(x1,y1,x2-x1+1,y2-y1+1,salle_suiv,xpos,ypos))
                
                self.enemies_list = []
                Ennemis = Background.data_salles[zone_trans.salle_suivante][1]
                for cle,valeur in Ennemis.items():
                    if cle == "slime":
                        for donnees_mob in valeur:
                            (v1,v2,v3,v4,v5) = donnees_mob
                            self.enemies_list.append(Slime(v1,v2,v3,v4,v5))
                    elif cle == "squelette":
                        for donnees_mob in valeur:
                            (v1,v2,v3) = donnees_mob
                            self.enemies_list.append(Squelette(v1,v2,v3))
                    elif cle == "boss":
                        for donnees_mob in valeur:
                            (v1,v2,v3) = donnees_mob
                            self.enemies_list.append(Boss(v1,v2,v3))
                
                self.piege_fleche = []
                self.chest=[]
                self.door=[]
                self.piques=[]
                self.checkpoint=[]
                for cle,valeur in Background.data_salles[self.salle_actuelle][2].items():
                    if cle == "fleche":
                        for (x,y,sens) in valeur:
                            self.piege_fleche.append(PiegeProjectile(x,y,sens))
                    elif cle == "coffre":
                        for (x,y,code) in valeur:
                            self.chest.append(Coffre(x,y,code))
                    elif cle=="porte":
                        for (x,y,sens,code,fut_salle,pos) in valeur:
                            self.door.append(Door(x,y,sens,code,fut_salle,pos))
                    elif cle=="piques":
                        for (x,y) in valeur:
                            self.piques.append(Pique(x,y))
                    elif cle =="checkpoint":
                        (x,y)=valeur
                        self.checkpoint.append(Checkpoint(x,y))
                for door in self.door:
                    door.advance_state(self.player.keycode_list,self.salle_actuelle,self.door,self.zone_transition)
                
                self.messages = []
                break
        
        if self.player.collide_checkpoint(self.checkpoint):
            self.player.life = 3
            Background.save(self.salle_actuelle,self.player.rect.topleft,self.poss_epee,self.player.keycode_list)
    
    def is_over(self):
        if self.player.life == 0:
            return True
        else: return False