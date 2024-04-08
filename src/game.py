#import des modules et des autres fichiers
import pygame
from gameconfig import GameConfig
from gamestate import GameState
from move import Move
from os import path

#fonctions utiles pour la gestion du jeu
def get_next_move():
    next_move=Move()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        next_move.right=True
        next_move.stand=False
    if keys[pygame.K_LEFT]:
        next_move.left=True
        next_move.stand=False
    if keys[pygame.K_UP]:
        next_move.up=True
        next_move.stand=False
    if keys[pygame.K_DOWN]:
        next_move.down=True
        next_move.stand=False
    if keys[pygame.K_SPACE]:
        next_move.attack=True
        next_move.stand=True
    return next_move

def display_message(window,texte,font_size,x,y,coul):
    if font_size == 100:
        img = GameConfig.FONT100.render(texte,True,coul)
    elif font_size == 50:
        img = GameConfig.FONT50.render(texte,True,coul)
    elif font_size == 30:
        img = GameConfig.FONT30.render(texte,True,coul)
    elif font_size == 20:
        img = GameConfig.FONT20.render(texte,True,coul)
    display_rect = img.get_rect()
    display_rect.center = (x,y)
    window.blit(img,display_rect)

def introduction_jeu(window):
    for i in range(0,256,2):
        window.fill(GameConfig.BLACK)
        display_message(window,"Bienvenue dans",50,GameConfig.WINDOW_W/2,200,(i,i,i))
        display_message(window,"The catacombs of skeletons",100,GameConfig.WINDOW_W/2,270,(i,i,i))
        pygame.display.update()
        pygame.time.delay(20)
    
    display_message(window,"Appuyer sur D pour débuter",30,GameConfig.WINDOW_W/2,500,GameConfig.WHITE)
    if path.exists("save_data.txt"):
        display_message(window,"Appuyer sur espace pour continuer",30,GameConfig.WINDOW_W/2,600,GameConfig.WHITE)
    
    pygame.display.update()
    pygame.time.delay(20)

    EXIT = False
    suite = ""

    while not EXIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EXIT = True
                suite = "quit"
        keys=pygame.key.get_pressed()
        if keys[pygame.K_d]:
            suite = "begin"
            EXIT = True
        elif keys[pygame.K_SPACE] and path.exists("save_data.txt"):
            suite = "continue"
            EXIT = True
    
    return suite

def animation_mort(window):
    image_noire = pygame.transform.scale(GameConfig.IMG_NOIRE,(GameConfig.WINDOW_W,GameConfig.WINDOW_H))
    rect = image_noire.get_rect()
    rect.topleft = (0,0)
    for i in range(0,50,1):
        image_noire.set_alpha(i)
        window.blit(image_noire,rect)
        pygame.display.update()
        pygame.time.delay(20)
    display_message(window,"Vous avez péri...",100,GameConfig.WINDOW_W/2,300,GameConfig.RED)
    display_message(window,"Appuyez sur espace pour continuer",30,GameConfig.WINDOW_W/2,500,GameConfig.RED)
    pygame.display.update()
    pygame.time.delay(20)

def play_again():
    while True:
        for event in pygame.event.get([pygame.QUIT]):
            if event.type == pygame.QUIT:
                return False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        pygame.time.delay(50)

#affichage des messages, rejouer, etc

#boucle de jeu
def game_loop(window):
    suite = introduction_jeu(window)
    game_over = False
    if suite == "quit":
        quitting = True
    else:
        quitting = False
        game_state = GameState(suite)
    while not game_over and not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
        
        if game_state.is_over():
            animation_mort(window)
            game_over = True
        else:
            next_move = get_next_move()
            game_state.advance_state(next_move)
            game_state.draw(window)

            pygame.display.update()
            pygame.time.delay(20)

    if not quitting and play_again():
        game_loop(window)

#lancement du jeu
if __name__=="__main__":
    pygame.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
    pygame.display.set_caption("The catacombs of skeletons")
    GameConfig.init()
    game_loop(window)
    pygame.quit()
    quit()