import pygame
from gameconfig import GameConfig
from object import Object
from squelette import Squelette
from boss import Boss

class Player(pygame.sprite.Sprite) :
    LEFT = -1
    RIGHT = 1
    UP = -2
    DOWN = 2
    NONE = 0

    LIFE = 3

    #Initialise le player
    def __init__(self,x,y,inventaire) :
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, GameConfig.PLAYER_W, GameConfig.PLAYER_H) #définit la position initiale du player et sa taille
        self.image = GameConfig.STANDING_DOWN_IMG[0]
        self.mask = GameConfig.STANDING_DOWN_MASK[0]
        self.vx = 0
        self.vy = 0
        self.sprite_count = 0
        self.direction = Player.DOWN
        self.inv_time = 0
        self.attacking = False
        self.attack_frame = 0
        self.alonge = []
        self.keycode_list=inventaire
        self.life = 3

    #Détermine quelle animation correspond à quel déplacement pour le player
    def init_sprites():
        Player.IMAGES = {Player.LEFT : GameConfig.WALK_LEFT_IMG,
                         Player.RIGHT : GameConfig.WALK_RIGHT_IMG,
                         Player.UP : GameConfig.WALK_UP_IMG,
                         Player.DOWN : GameConfig.WALK_DOWN_IMG}

        Player.MASKS = {Player.LEFT : GameConfig.WALK_LEFT_MASKS,
                        Player.RIGHT : GameConfig.WALK_RIGHT_MASKS,
                        Player.UP : GameConfig.WALK_UP_MASKS,
                        Player.DOWN : GameConfig.WALK_DOWN_MASKS}

        Player.STAND_IMAGES = {Player.LEFT : GameConfig.STANDING_LEFT_IMG,
                               Player.RIGHT : GameConfig.STANDING_RIGHT_IMG,
                               Player.UP : GameConfig.STANDING_UP_IMG,
                               Player.DOWN : GameConfig.STANDING_DOWN_IMG}

        Player.STAND_MASKS = {Player.LEFT : GameConfig.STANDING_LEFT_MASK,
                               Player.RIGHT : GameConfig.STANDING_RIGHT_MASK,
                               Player.UP : GameConfig.STANDING_UP_MASK,
                               Player.DOWN : GameConfig.STANDING_DOWN_MASK}
        
        Player.ATTACKING_IMG = {Player.LEFT : GameConfig.ATTACKING_LEFT_IMG,
                             Player.RIGHT : GameConfig.ATTACKING_RIGHT_IMG,
                             Player.UP : GameConfig.ATTACKING_UP_IMG,
                             Player.DOWN : GameConfig.ATTACKING_DOWN_IMG}

        Player.ATTACKING_MASKS = {Player.LEFT : GameConfig.ATTACKING_LEFT_MASK,
                               Player.RIGHT : GameConfig.ATTACKING_RIGHT_MASK,
                               Player.UP : GameConfig.ATTACKING_UP_MASK,
                               Player.DOWN : GameConfig.ATTACKING_DOWN_MASK}

        Player.ATTACK_IMG = {Player.LEFT : GameConfig.ATTACK_LEFT_IMG,
                             Player.RIGHT : GameConfig.ATTACK_RIGHT_IMG,
                             Player.UP : GameConfig.ATTACK_UP_IMG,
                             Player.DOWN : GameConfig.ATTACK_DOWN_IMG}

        Player.ATTACK_MASKS = {Player.LEFT : GameConfig.ATTACK_LEFT_MASKS,
                               Player.RIGHT : GameConfig.ATTACK_RIGHT_MASKS,
                               Player.UP : GameConfig.ATTACK_UP_MASKS,
                               Player.DOWN : GameConfig.ATTACK_DOWN_MASKS}
        

    #Permet d'afficher le player    
    def draw(self, window) :
        if self.attacking :
            self.alonge[self.attack_frame-1].draw(window)
        window.blit(self.image,self.rect.topleft)

    #Gère l'attaque du player
    def attack(self, enemies_list) :
        if  self.attacking == True :

            #Si l'animation est finie, arrête l'attaque.
            if self.attack_frame >= GameConfig.NB_FRAMES_PER_SPRITE_ATTACK*len(Player.ATTACK_IMG[self.direction]):
                self.attack_frame = 0
                self.attacking = False
                self.alonge = []
                return

            xp,yp = self.rect.topleft
            #Attaque selon la direction du player.
            if self.direction == Player.LEFT :
                self.alonge.append(Object(xp-GameConfig.SWORD_SIZE/2+53,yp-GameConfig.SWORD_SIZE/2+75,GameConfig.SWORD_SIZE,
                GameConfig.SWORD_SIZE,Player.ATTACK_IMG[self.direction][self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK],
                Player.ATTACK_MASKS[self.direction][self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK]))
            if self.direction == Player.RIGHT :
                self.alonge.append(Object(xp-GameConfig.SWORD_SIZE/2+78,yp-GameConfig.SWORD_SIZE/2+74,GameConfig.SWORD_SIZE,
                GameConfig.SWORD_SIZE,Player.ATTACK_IMG[self.direction][self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK],
                Player.ATTACK_MASKS[self.direction][self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK]))
            if self.direction == Player.UP :
                self.alonge.append(Object(xp-GameConfig.SWORD_SIZE/2+65,yp-GameConfig.SWORD_SIZE/2+54,GameConfig.SWORD_SIZE,
                GameConfig.SWORD_SIZE,Player.ATTACK_IMG[self.direction][self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK],
                Player.ATTACK_MASKS[self.direction][self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK]))
            if self.direction == Player.DOWN :
                self.alonge.append(Object(xp-GameConfig.SWORD_SIZE/2+60,yp-GameConfig.SWORD_SIZE/2+80,GameConfig.SWORD_SIZE,
                GameConfig.SWORD_SIZE,Player.ATTACK_IMG[self.direction][self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK],
                Player.ATTACK_MASKS[self.direction][self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK]))

            #Si l'attaque touche un ennemi, le tue en l'effaçant de la liste des ennemis.
            for i in enemies_list :
                if pygame.sprite.collide_mask(self.alonge[self.attack_frame//GameConfig.NB_FRAMES_PER_SPRITE_ATTACK], i) and i.clas!=Boss :
                    enemies_list.remove(i)

            self.attack_frame += 1

    #Gère les déplacements du player et les collisions du player
    def advance_state(self, next_move, enemies_list, mask_mur, liste_pique, liste_fleche, poss_epee) :
        
        fx = 0
        fy = 0
        
        #Si le player est en frame d'invicibilité, diminue self.inv_time de 1.
        if self.inv_time > 0 :
            self.inv_time -= 1

        #Si le player entre en collision avec un ennemi alors qu'il n'est pas en frame d'invincibilité,
        #alors il perds une vie et entre en frame d'invinciblité.
        for i in enemies_list :
                if pygame.sprite.collide_mask(self, i) and self.inv_time == 0 :
                    self.life = self.life-1
                    self.inv_time = GameConfig.INVUNERABLE_TIME
                if (type(i) == Squelette or type(i) == Boss) and len(i.alonge)>0 and pygame.sprite.collide_mask(self, i.alonge[0]) and self.inv_time == 0 :
                    self.life = self.life-1
                    self.inv_time = GameConfig.INVUNERABLE_TIME        

        #Si le player entre en collision avec un piège alors qu'il n'est pas en frame d'invincibilité,
        #alors il perds une vie et entre en frame d'invinciblité.
        for i in liste_pique :
                if pygame.sprite.collide_mask(self, i) and self.inv_time == 0 :
                    self.life = self.life-1
                    self.inv_time = GameConfig.INVUNERABLE_TIME
        
        #Si le player entre en collision avec un piège alors qu'il n'est pas en frame d'invincibilité,
        #alors il perds une vie et entre en frame d'invinciblité.
        for i in liste_fleche :
            for j in i.arrow :
                if pygame.sprite.collide_mask(self, j) and self.inv_time == 0 :
                    self.life = self.life-1
                    self.inv_time = GameConfig.INVUNERABLE_TIME

        if  self.attacking == False :
            #Pour chaque direction, on teste la collision et on ne fait avancer le player que si il n'entre en collision avec aucun élément.
            if next_move.left :
                fx = GameConfig.FORCE_LEFT
                self.vx = fx*GameConfig.DT
                self.rect = self.rect.move(self.vx*GameConfig.DT, 0)
                while pygame.sprite.collide_mask(self, mask_mur):
                    self.rect = self.rect.move(1, 0)
                
            elif next_move.right :
                fx = GameConfig.FORCE_RIGHT
                self.vx = fx*GameConfig.DT
                self.rect = self.rect.move(self.vx*GameConfig.DT, 0)
                while pygame.sprite.collide_mask(self, mask_mur):
                    self.rect = self.rect.move(-1, 0)

            if next_move.up :
                fy = GameConfig.FORCE_UP
                self.vy = fy*GameConfig.DT
                self.rect = self.rect.move(0, self.vy*GameConfig.DT)
                while pygame.sprite.collide_mask(self, mask_mur):
                    self.rect = self.rect.move(0, 1)

            elif next_move.down :
                fy = GameConfig.FORCE_DOWN
                self.vy = fy*GameConfig.DT
                self.rect = self.rect.move(0, self.vy*GameConfig.DT)
                while pygame.sprite.collide_mask(self, mask_mur):
                    self.rect = self.rect.move(0, -1)

            #Anime le player selon la direction de son déplacement, ou s'il est immobile.
            if next_move.left:
                self.direction = Player.LEFT
            elif next_move.right:
                self.direction = Player.RIGHT
            elif next_move.up:
                self.direction = Player.UP
            elif next_move.down:
                self.direction = Player.DOWN

            if next_move.stand == False :
                self.sprite_count+=1
                if self.sprite_count >= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER*len(Player.IMAGES[self.direction]):
                    self.sprite_count = 0
                self.image = Player.IMAGES[self.direction][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
                self.mask = Player.MASKS[self.direction][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
            else :
                self.image = Player.STAND_IMAGES[self.direction][0]
                self.mask = Player.STAND_MASKS[self.direction][0]

            if next_move.attack and poss_epee == "oui":
                self.attacking = True

            if self.attacking :
                self.image = Player.ATTACKING_IMG[self.direction][0]
                self.mask = Player.ATTACKING_MASKS[self.direction][0]

        self.attack(enemies_list)

    #Gère les collisions entre le joueur et une zone de transition
    def collide_trans(self, zone_trans):
        if pygame.sprite.collide_mask(self, zone_trans):
            if zone_trans.posx == -1:
                x = self.rect.left
            else : 
                x = zone_trans.posx-32
            if zone_trans.posy == -1:
                y = self.rect.top
            else : 
                y = zone_trans.posy-32
            self.rect = pygame.Rect(x, y, GameConfig.PLAYER_W, GameConfig.PLAYER_H)
            return True
        else: 
            return False
    
    def collide_checkpoint(self,checkpoint_list):
        for checkpoint in checkpoint_list:
            if pygame.sprite.collide_mask(self,checkpoint):
                return True
        return False
