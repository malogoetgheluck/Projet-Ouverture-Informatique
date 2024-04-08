from gameconfig import GameConfig

class Message():
    
    def __init__(self,pos,texte,time,taille):
        self.time_rest = time
        if taille == 100:
            self.img = GameConfig.FONT100.render(texte,True,GameConfig.WHITE)
        elif taille == 50:
            self.img = GameConfig.FONT50.render(texte,True,GameConfig.WHITE)
        elif taille == 30:
            self.img = GameConfig.FONT30.render(texte,True,GameConfig.WHITE)
        elif taille == 20:
            self.img = GameConfig.FONT20.render(texte,True,GameConfig.WHITE)
        self.display_rect = self.img.get_rect()
        self.display_rect.topleft = pos
    
    def draw(self,window):
        window.blit(self.img,self.display_rect)

    def advance_state(self,list_mess):
        self.time_rest-=1
        if self.time_rest == 0:
            list_mess.remove(self)