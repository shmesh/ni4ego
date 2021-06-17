import pygame as pg
BLACK = [0,0,0]
WHITE = [255,255,255]




class knopo4ki:
    def __init__(self,text,pos):
        self.text = text
        self.action = None
        self.color = BLACK
        self.pos = pos

    def prorisovka(self,sc):
        storyp = pg.font.Font(None, 36)

        pg.draw.rect(sc, self.color, self.pos)

        knopka = storyp.render(self.text, True,WHITE)

        sc.blit(knopka,self.pos)

