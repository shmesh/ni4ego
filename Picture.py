import pygame as pg
class Picture :
    def __init__(self,size,path,pos):
        self.size = size
        self.path = path
        self.pos = pos
    def prorisovka(self,sc):
        personashi = pg.image.load(self.path)
        personashi = pg.transform.scale(personashi,self.size)
        sc.blit(personashi,self.pos)
