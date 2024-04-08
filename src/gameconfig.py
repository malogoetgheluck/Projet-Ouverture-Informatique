import pygame

class GameConfig:
    #constantes du jeu
    WINDOW_H=768
    WINDOW_W=1152
    PLAYER_W = 128
    PLAYER_H = 128
    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    FORCE_UP = -20
    FORCE_DOWN = -FORCE_UP
    NB_FRAMES_PER_SPRITE_PLAYER = 2
    INVUNERABLE_TIME = 30

    LIFE_H = 64
    LIFE_W = 64

    SWORD_SIZE = 96
    NB_FRAMES_PER_SPRITE_ATTACK = 2

    SLIME_W=64
    SLIME_H=64

    SQUELETTE_W=64
    SQUELETTE_H=64

    SLIME_DEPLACEMENT_DISTANCE=5
    NB_FRAMES_PER_SPRITE_SLIME=3

    SQUELETTE_DEPLACEMENT_DISTANCE=3
    NB_FRAMES_PER_SPRITE_SQUELETTE=3
    NB_FRAMES_PER_SPRITE_ATTAQUE_SQUELETTE=5
    SQUELETTE_DELAY_ATTAQUE=5


    # a = attaque
    SQUELETTE_A_RANGE=10
    S_ATTAQUE_SIZE=64

    ARROW_SPEED=10
    NB_FRAMES_PER_SPRITE_PIEGE=6
    PIEGE_SIZE=32
    ARROW_SIZE=32

    DOOR_SIZE=64
    COFFRE_SIZE=64
    INTER_FRAME_CHEST=6

    PIQUE_SIZE=64
    CHECKPOINT_SIZE=64

    NB_FRAMES_PER_SPRITE_ATTAQUE_BOSS = 10
    BOSS_SIZE=256
    BOSS_A_RANGE=128
    BOSS_DEPLACEMENT_DISTANCE=2
    B_ATTAQUE_SIZE=64

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)

    def init():
        GameConfig.LIFE = pygame.transform.scale(pygame.image.load('Ressources/Elements/Coeur.png'),(GameConfig.LIFE_H,GameConfig.LIFE_W))

        GameConfig.WALK_RIGHT_IMG = [
            pygame.image.load('Ressources/Sprite_perso/Walking_right1.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_right2.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_right3.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_right4.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_right5.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_right6.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_right7.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_right8.png').convert_alpha()]
        GameConfig.WALK_LEFT_IMG = [
            pygame.image.load('Ressources/Sprite_perso/Walking_left1.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_left2.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_left3.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_left4.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_left5.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_left6.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_left7.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_left8.png').convert_alpha()]
        GameConfig.WALK_UP_IMG = [
            pygame.image.load('Ressources/Sprite_perso/Walking_back1.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_back2.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_back3.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_back4.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_back5.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_back6.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_back7.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_back8.png').convert_alpha()]
        GameConfig.WALK_DOWN_IMG = [
            pygame.image.load('Ressources/Sprite_perso/Walking_front1.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_front2.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_front3.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_front4.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_front5.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_front6.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_front7.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_perso/Walking_front8.png').convert_alpha()]
            
        GameConfig.STANDING_RIGHT_IMG = [
            pygame.image.load('Ressources/Sprite_perso/Standing_right.png').convert_alpha()]
        GameConfig.STANDING_LEFT_IMG = [
            pygame.image.load('Ressources/Sprite_perso/Standing_left.png').convert_alpha()]
        GameConfig.STANDING_UP_IMG = [
            pygame.image.load('Ressources/Sprite_perso/Standing_back.png').convert_alpha()]
        GameConfig.STANDING_DOWN_IMG = [
            pygame.image.load('Ressources/Sprite_perso/Standing_front.png').convert_alpha()]

        GameConfig.WALK_RIGHT_MASKS = []
        GameConfig.WALK_LEFT_MASKS = []
        GameConfig.WALK_UP_MASKS = []
        GameConfig.WALK_DOWN_MASKS = []
        
        for im in GameConfig.WALK_RIGHT_IMG:
            GameConfig.WALK_RIGHT_MASKS.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_LEFT_IMG:
            GameConfig.WALK_LEFT_MASKS.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_UP_IMG:
            GameConfig.WALK_UP_MASKS.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_DOWN_IMG:
            GameConfig.WALK_DOWN_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.STANDING_RIGHT_MASK = [pygame.mask.from_surface(GameConfig.STANDING_RIGHT_IMG[0])]
        GameConfig.STANDING_LEFT_MASK = [pygame.mask.from_surface(GameConfig.STANDING_LEFT_IMG[0])]
        GameConfig.STANDING_UP_MASK = [pygame.mask.from_surface(GameConfig.STANDING_UP_IMG[0])]
        GameConfig.STANDING_DOWN_MASK = [pygame.mask.from_surface(GameConfig.STANDING_DOWN_IMG[0])]

        GameConfig.ATTACKING_RIGHT_IMG = [pygame.image.load('Ressources/Sprite_perso/Attacking_right.png').convert_alpha()]
        GameConfig.ATTACKING_LEFT_IMG = [pygame.image.load('Ressources/Sprite_perso/Attacking_left.png').convert_alpha()]
        GameConfig.ATTACKING_UP_IMG = [pygame.image.load('Ressources/Sprite_perso/Attacking_back.png').convert_alpha()]
        GameConfig.ATTACKING_DOWN_IMG = [pygame.image.load('Ressources/Sprite_perso/Attacking_front.png').convert_alpha()]

        GameConfig.ATTACKING_RIGHT_MASK = [pygame.mask.from_surface(GameConfig.ATTACKING_RIGHT_IMG[0])]
        GameConfig.ATTACKING_LEFT_MASK = [pygame.mask.from_surface(GameConfig.ATTACKING_LEFT_IMG[0])]
        GameConfig.ATTACKING_UP_MASK = [pygame.mask.from_surface(GameConfig.ATTACKING_UP_IMG[0])]
        GameConfig.ATTACKING_DOWN_MASK = [pygame.mask.from_surface(GameConfig.ATTACKING_DOWN_IMG[0])]

        GameConfig.ATTACK_RIGHT_IMG = [
            pygame.image.load('Ressources/Sword/Sword_right1.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_right2.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_right3.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_right4.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_right5.png').convert_alpha()]
        for i in range (0,len(GameConfig.ATTACK_RIGHT_IMG)):
            GameConfig.ATTACK_RIGHT_IMG[i]=pygame.transform.scale(GameConfig.ATTACK_RIGHT_IMG[i],(GameConfig.SWORD_SIZE,GameConfig.SWORD_SIZE))
        GameConfig.ATTACK_LEFT_IMG = [
            pygame.image.load('Ressources/Sword/Sword_left1.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_left2.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_left3.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_left4.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_left5.png').convert_alpha()]
        for i in range (0,len(GameConfig.ATTACK_LEFT_IMG)):
            GameConfig.ATTACK_LEFT_IMG[i]=pygame.transform.scale(GameConfig.ATTACK_LEFT_IMG[i],(GameConfig.SWORD_SIZE,GameConfig.SWORD_SIZE))
        GameConfig.ATTACK_UP_IMG = [
            pygame.image.load('Ressources/Sword/Sword_up1.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_up2.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_up3.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_up4.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_up5.png').convert_alpha()]
        for i in range (0,len(GameConfig.ATTACK_UP_IMG)):
            GameConfig.ATTACK_UP_IMG[i]=pygame.transform.scale(GameConfig.ATTACK_UP_IMG[i],(GameConfig.SWORD_SIZE,GameConfig.SWORD_SIZE))
        GameConfig.ATTACK_DOWN_IMG = [
            pygame.image.load('Ressources/Sword/Sword_down1.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_down2.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_down3.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_down4.png').convert_alpha(),
            pygame.image.load('Ressources/Sword/Sword_down5.png').convert_alpha()]
        for i in range (0,len(GameConfig.ATTACK_DOWN_IMG)):
            GameConfig.ATTACK_DOWN_IMG[i]=pygame.transform.scale(GameConfig.ATTACK_DOWN_IMG[i],(GameConfig.SWORD_SIZE,GameConfig.SWORD_SIZE))

        GameConfig.ATTACK_RIGHT_MASKS = []
        GameConfig.ATTACK_LEFT_MASKS = []
        GameConfig.ATTACK_UP_MASKS = []
        GameConfig.ATTACK_DOWN_MASKS = []

        for im in GameConfig.ATTACK_RIGHT_IMG:
            GameConfig.ATTACK_RIGHT_MASKS.append(pygame.mask.from_surface(im))
        for im in GameConfig.ATTACK_LEFT_IMG:
            GameConfig.ATTACK_LEFT_MASKS.append(pygame.mask.from_surface(im))
        for im in GameConfig.ATTACK_UP_IMG:
            GameConfig.ATTACK_UP_MASKS.append(pygame.mask.from_surface(im))
        for im in GameConfig.ATTACK_DOWN_IMG:
            GameConfig.ATTACK_DOWN_MASKS.append(pygame.mask.from_surface(im))
        

        """ SPRITE DES ENEMIES """

        #sprite et masks du slime
        GameConfig.SLIME_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Slime1.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_ennemies/Slime2.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_ennemies/Slime3.png').convert_alpha(),
            pygame.image.load('Ressources/Sprite_ennemies/Slime4.png').convert_alpha()]
        GameConfig.SLIME_MASKS=[]
        for im in GameConfig.SLIME_IMG:
            GameConfig.SLIME_MASKS.append(pygame.mask.from_surface(im))




        #sprite et masks de marche du squelette
        GameConfig.SQUELETTE_WALK_RIGHT_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Squelette_right1.png').convert_alpha()]

        GameConfig.SQUELETTE_WALK_RIGHT_MASKS=[]
        for im in GameConfig.SQUELETTE_WALK_RIGHT_IMG:
            GameConfig.SQUELETTE_WALK_RIGHT_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.SQUELETTE_WALK_UP_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Squelette_back1.png').convert_alpha()]
        
        GameConfig.SQUELETTE_WALK_UP_MASKS=[]
        for im in GameConfig.SQUELETTE_WALK_UP_IMG:
            GameConfig.SQUELETTE_WALK_UP_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.SQUELETTE_WALK_DOWN_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Squelette_front1.png').convert_alpha()]
        
        GameConfig.SQUELETTE_WALK_DOWN_MASKS=[]
        for im in GameConfig.SQUELETTE_WALK_DOWN_IMG:
            GameConfig.SQUELETTE_WALK_DOWN_MASKS.append(pygame.mask.from_surface(im))
        
        GameConfig.SQUELETTE_WALK_LEFT_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Squelette_left1.png').convert_alpha()]
        
        GameConfig.SQUELETTE_WALK_LEFT_MASKS=[]
        for im in GameConfig.SQUELETTE_WALK_LEFT_IMG:
            GameConfig.SQUELETTE_WALK_LEFT_MASKS.append(pygame.mask.from_surface(im))


        # sprite idle avec direction

        GameConfig.SQUELETTE_IDLE_LEFT_IMG=pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_left1.png').convert_alpha()
        GameConfig.SQUELETTE_IDLE_LEFT_MASKS=pygame.mask.from_surface(GameConfig.SQUELETTE_IDLE_LEFT_IMG)

        GameConfig.SQUELETTE_IDLE_RIGHT_IMG=pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_right1.png').convert_alpha()
        GameConfig.SQUELETTE_IDLE_RIGHT_MASKS=pygame.mask.from_surface(GameConfig.SQUELETTE_IDLE_RIGHT_IMG)

        GameConfig.SQUELETTE_IDLE_UP_IMG=pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_back1.png').convert_alpha()
        GameConfig.SQUELETTE_IDLE_UP_MASKS=pygame.mask.from_surface(GameConfig.SQUELETTE_IDLE_UP_IMG)

        GameConfig.SQUELETTE_IDLE_DOWN_IMG=pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_front1.png').convert_alpha()
        GameConfig.SQUELETTE_IDLE_DOWN_MASKS=pygame.mask.from_surface(GameConfig.SQUELETTE_IDLE_DOWN_IMG)


        #sprite et masks d'attaque du squelette


        GameConfig.SQUELETTE_ATTAQUE_RIGHT_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_right1.png').convert_alpha()]
        GameConfig.SQUELETTE_ATTAQUE_RIGHT_MASKS=[]
        for im in GameConfig.SQUELETTE_ATTAQUE_RIGHT_IMG:
            GameConfig.SQUELETTE_ATTAQUE_RIGHT_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.SQUELETTE_ATTAQUE_UP_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_back1.png').convert_alpha()]
        GameConfig.SQUELETTE_ATTAQUE_UP_MASKS=[]
        for im in GameConfig.SQUELETTE_ATTAQUE_UP_IMG:
            GameConfig.SQUELETTE_ATTAQUE_UP_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.SQUELETTE_ATTAQUE_DOWN_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_front1.png').convert_alpha()]
        GameConfig.SQUELETTE_ATTAQUE_DOWN_MASKS=[]
        for im in GameConfig.SQUELETTE_ATTAQUE_DOWN_IMG:
            GameConfig.SQUELETTE_ATTAQUE_DOWN_MASKS.append(pygame.mask.from_surface(im))
        
        GameConfig.SQUELETTE_ATTAQUE_LEFT_IMG =[pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_left1.png').convert_alpha()]
        GameConfig.SQUELETTE_ATTAQUE_LEFT_MASKS=[]
        for im in GameConfig.SQUELETTE_ATTAQUE_LEFT_IMG:
            GameConfig.SQUELETTE_ATTAQUE_LEFT_MASKS.append(pygame.mask.from_surface(im))

        #allonge de l'épee

        GameConfig.SQUELETTE_ALLONGE_LEFT_IMG=[pygame.image.load('Ressources/Sword/Sword_left1.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_left2.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_left3.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_left4.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_left5.png').convert_alpha()]
        GameConfig.SQUELETTE_ALLONGE_LEFT_MASKS=[]
        for im in GameConfig.SQUELETTE_ALLONGE_LEFT_IMG:
            GameConfig.SQUELETTE_ALLONGE_LEFT_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.SQUELETTE_ALLONGE_UP_IMG=[pygame.image.load('Ressources/Sword/Sword_up1.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_up2.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_up3.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_up4.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_up5.png').convert_alpha()]
        GameConfig.SQUELETTE_ALLONGE_UP_MASKS=[]
        for im in GameConfig.SQUELETTE_ALLONGE_UP_IMG:
            GameConfig.SQUELETTE_ALLONGE_UP_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.SQUELETTE_ALLONGE_RIGHT_IMG=[pygame.image.load('Ressources/Sword/Sword_right1.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_right2.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_right3.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_right4.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_right5.png').convert_alpha()]
        GameConfig.SQUELETTE_ALLONGE_RIGHT_MASKS=[]
        for im in GameConfig.SQUELETTE_ALLONGE_RIGHT_IMG:
            GameConfig.SQUELETTE_ALLONGE_RIGHT_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.SQUELETTE_ALLONGE_DOWN_IMG=[pygame.image.load('Ressources/Sword/Sword_down1.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_down2.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_down3.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_down4.png').convert_alpha(),
        pygame.image.load('Ressources/Sword/Sword_down5.png').convert_alpha()]
        GameConfig.SQUELETTE_ALLONGE_DOWN_MASKS=[]
        for im in GameConfig.SQUELETTE_ALLONGE_DOWN_IMG:
            GameConfig.SQUELETTE_ALLONGE_DOWN_MASKS.append(pygame.mask.from_surface(im))

        #piege

        GameConfig.PIEGE_IMG_DOWN=[pygame.image.load('Ressources/Elements/Piège_fleche_down_1.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_down_2.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_down_3.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_down_4.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_down_5.png').convert_alpha()]
        GameConfig.PIEGE_MASKS_DOWN=[]
        for im in GameConfig.PIEGE_IMG_DOWN:
            GameConfig.PIEGE_MASKS_DOWN.append(pygame.mask.from_surface(im))
        
        GameConfig.PIEGE_IMG_UP=[pygame.image.load('Ressources/Elements/Piège_fleche_up_1.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_up_2.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_up_3.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_up_4.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_up_5.png').convert_alpha()]
        GameConfig.PIEGE_MASKS_UP=[]
        for im in GameConfig.PIEGE_IMG_UP:
            GameConfig.PIEGE_MASKS_UP.append(pygame.mask.from_surface(im))
        
        GameConfig.PIEGE_IMG_LEFT=[pygame.image.load('Ressources/Elements/Piège_fleche_left_1.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_left_2.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_left_3.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_left_4.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_left_5.png').convert_alpha()]
        GameConfig.PIEGE_MASKS_LEFT=[]
        for im in GameConfig.PIEGE_IMG_LEFT:
            GameConfig.PIEGE_MASKS_LEFT.append(pygame.mask.from_surface(im))

        GameConfig.PIEGE_IMG_RIGHT=[pygame.image.load('Ressources/Elements/Piège_fleche_right_1.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_right_2.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_right_3.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_right_4.png').convert_alpha(),
        pygame.image.load('Ressources/Elements/Piège_fleche_right_5.png').convert_alpha()]
        GameConfig.PIEGE_MASKS_RIGHT=[]
        for im in GameConfig.PIEGE_IMG_RIGHT:
            GameConfig.PIEGE_MASKS_RIGHT.append(pygame.mask.from_surface(im))
            
        #arrow

        GameConfig.ARROW_IMG_DOWN=pygame.image.load('Ressources/Elements/Fleche_down.png').convert_alpha()
        GameConfig.ARROW_MASK_DOWN=pygame.mask.from_surface(GameConfig.ARROW_IMG_DOWN)

        GameConfig.ARROW_IMG_LEFT=pygame.image.load('Ressources/Elements/Fleche_left.png').convert_alpha()
        GameConfig.ARROW_MASK_LEFT=pygame.mask.from_surface(GameConfig.ARROW_IMG_LEFT)


        GameConfig.ARROW_IMG_UP=pygame.image.load('Ressources/Elements/Fleche_up.png').convert_alpha()
        GameConfig.ARROW_MASK_UP=pygame.mask.from_surface(GameConfig.ARROW_IMG_UP)

        GameConfig.ARROW_IMG_RIGHT=pygame.image.load('Ressources/Elements/Fleche_right.png').convert_alpha()
        GameConfig.ARROW_MASK_RIGHT=pygame.mask.from_surface(GameConfig.ARROW_IMG_RIGHT)

        #porte

        GameConfig.PORTE_IMG_DOWN=pygame.image.load('Ressources/Elements/Porte_fermee_down.png').convert_alpha()
        GameConfig.PORTE_MASK_DOWN=pygame.mask.from_surface(GameConfig.PORTE_IMG_DOWN)

        GameConfig.PORTE_IMG_UP=pygame.image.load('Ressources/Elements/Porte_fermee_up.png').convert_alpha()
        GameConfig.PORTE_MASK_UP=pygame.mask.from_surface(GameConfig.PORTE_IMG_UP)

        GameConfig.PORTE_IMG_LEFT=pygame.image.load('Ressources/Elements/Porte_fermee_left.png').convert_alpha()
        GameConfig.PORTE_MASK_LEFT=pygame.mask.from_surface(GameConfig.PORTE_IMG_LEFT)

        GameConfig.PORTE_IMG_RIGHT=pygame.image.load('Ressources/Elements/Porte_fermee_right.png').convert_alpha()
        GameConfig.PORTE_MASK_RIGHT=pygame.mask.from_surface(GameConfig.PORTE_IMG_RIGHT)

        #cle

        GameConfig.CHEST_IMG=pygame.image.load('Ressources/Elements/Chest_close.png').convert_alpha()
        GameConfig.CHEST_MASK=pygame.mask.from_surface(GameConfig.CHEST_IMG)

        GameConfig.CHEST_OPEN=[pygame.image.load('Ressources/Elements/Chest_open.png'),
                                pygame.image.load('Ressources/Elements/Chest_open.png'),
                                pygame.image.load('Ressources/Elements/Chest_open.png'),
                                pygame.image.load('Ressources/Elements/Chest_open.png')]

        #pique

        GameConfig.PIQUE_IMG=pygame.image.load('Ressources/Elements/Piques.png').convert_alpha()
        GameConfig.PIQUE_MASK=pygame.mask.from_surface(GameConfig.PIQUE_IMG)

        #Checkpoint
        GameConfig.CHECKPOINT_IMG=pygame.image.load('Ressources/Elements/Checkpoint.png').convert_alpha()
        GameConfig.CHECKPOINT_MASK=pygame.mask.from_surface(GameConfig.CHECKPOINT_IMG)

        #boss

        #sprite et masks de marche du boss
        GameConfig.BOSS_WALK_RIGHT_IMG =[pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_right1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]

        GameConfig.BOSS_WALK_RIGHT_MASKS=[]
        for im in GameConfig.BOSS_WALK_RIGHT_IMG:
            GameConfig.BOSS_WALK_RIGHT_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.BOSS_WALK_UP_IMG =[pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_back1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        
        GameConfig.BOSS_WALK_UP_MASKS=[]
        for im in GameConfig.BOSS_WALK_UP_IMG:
            GameConfig.BOSS_WALK_UP_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.BOSS_WALK_DOWN_IMG =[pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_front1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        
        GameConfig.BOSS_WALK_DOWN_MASKS=[]
        for im in GameConfig.BOSS_WALK_DOWN_IMG:
            GameConfig.BOSS_WALK_DOWN_MASKS.append(pygame.mask.from_surface(im))
        
        GameConfig.BOSS_WALK_LEFT_IMG =[pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_left1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        
        GameConfig.BOSS_WALK_LEFT_MASKS=[]
        for im in GameConfig.BOSS_WALK_LEFT_IMG:
            GameConfig.BOSS_WALK_LEFT_MASKS.append(pygame.mask.from_surface(im))


        # sprite idle avec direction

        GameConfig.BOSS_IDLE_LEFT_IMG=pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_left1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()
        GameConfig.BOSS_IDLE_LEFT_MASKS=pygame.mask.from_surface(GameConfig.SQUELETTE_IDLE_LEFT_IMG)

        GameConfig.BOSS_IDLE_RIGHT_IMG=pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_right1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()
        GameConfig.BOSS_IDLE_RIGHT_MASKS=pygame.mask.from_surface(GameConfig.SQUELETTE_IDLE_RIGHT_IMG)

        GameConfig.BOSS_IDLE_UP_IMG=pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_back1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()
        GameConfig.BOSS_IDLE_UP_MASKS=pygame.mask.from_surface(GameConfig.SQUELETTE_IDLE_UP_IMG)

        GameConfig.BOSS_IDLE_DOWN_IMG=pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_front1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()
        GameConfig.BOSS_IDLE_DOWN_MASKS=pygame.mask.from_surface(GameConfig.SQUELETTE_IDLE_DOWN_IMG)


        #sprite et masks d'attaque du boss


        GameConfig.BOSS_ATTAQUE_RIGHT_IMG =[pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_right1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        GameConfig.BOSS_ATTAQUE_RIGHT_MASKS=[]
        for im in GameConfig.BOSS_ATTAQUE_RIGHT_IMG:
            GameConfig.BOSS_ATTAQUE_RIGHT_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.BOSS_ATTAQUE_UP_IMG =[pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_back1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        GameConfig.BOSS_ATTAQUE_UP_MASKS=[]
        for im in GameConfig.BOSS_ATTAQUE_UP_IMG:
            GameConfig.BOSS_ATTAQUE_UP_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.BOSS_ATTAQUE_DOWN_IMG =[pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_front1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        GameConfig.BOSS_ATTAQUE_DOWN_MASKS=[]
        for im in GameConfig.BOSS_ATTAQUE_DOWN_IMG:
            GameConfig.BOSS_ATTAQUE_DOWN_MASKS.append(pygame.mask.from_surface(im))
        
        GameConfig.BOSS_ATTAQUE_LEFT_IMG =[pygame.transform.scale(pygame.image.load('Ressources/Sprite_ennemies/Squelette_attaque_left1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        GameConfig.BOSS_ATTAQUE_LEFT_MASKS=[]
        for im in GameConfig.BOSS_ATTAQUE_LEFT_IMG:
            GameConfig.BOSS_ATTAQUE_LEFT_MASKS.append(pygame.mask.from_surface(im))

        #épée du boss

        GameConfig.BOSS_ALLONGE_LEFT_IMG=[pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_left1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_left2.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_left3.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_left4.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_left5.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        GameConfig.BOSS_ALLONGE_LEFT_MASKS=[]
        for im in GameConfig.BOSS_ALLONGE_LEFT_IMG:
            GameConfig.BOSS_ALLONGE_LEFT_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.BOSS_ALLONGE_UP_IMG=[pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_up1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_up2.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_up3.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_up4.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_up5.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        GameConfig.BOSS_ALLONGE_UP_MASKS=[]
        for im in GameConfig.BOSS_ALLONGE_UP_IMG:
            GameConfig.BOSS_ALLONGE_UP_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.BOSS_ALLONGE_RIGHT_IMG=[pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_right1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_right2.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_right3.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_right4.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_right5.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        GameConfig.BOSS_ALLONGE_RIGHT_MASKS=[]
        for im in GameConfig.BOSS_ALLONGE_RIGHT_IMG:
            GameConfig.BOSS_ALLONGE_RIGHT_MASKS.append(pygame.mask.from_surface(im))

        GameConfig.BOSS_ALLONGE_DOWN_IMG=[pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_down1.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_down2.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_down3.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_down4.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha(),
        pygame.transform.scale(pygame.image.load('Ressources/Sword/Sword_down5.png'),(GameConfig.BOSS_SIZE,GameConfig.BOSS_SIZE)).convert_alpha()]
        GameConfig.BOSS_ALLONGE_DOWN_MASKS=[]
        for im in GameConfig.BOSS_ALLONGE_DOWN_IMG:
            GameConfig.BOSS_ALLONGE_DOWN_MASKS.append(pygame.mask.from_surface(im))

        
        GameConfig.FONT100 = pygame.font.Font('Ressources/EXTRASerif-Regular.ttf',100)
        GameConfig.FONT50 = pygame.font.Font('Ressources/EXTRASerif-Regular.ttf',50)
        GameConfig.FONT30 = pygame.font.Font('Ressources/EXTRASerif-Regular.ttf',30)
        GameConfig.FONT20 = pygame.font.Font('Ressources/EXTRASerif-Regular.ttf',20)

        GameConfig.IMG_NOIRE = pygame.image.load('Ressources/Image_noire.png')
        

        



