import pygame as pg
from funksii import find_left_corner





class Text :
    def __init__(self,text,id,pos,size,col):
        self.pos = pos
        self.size = size
        font = pg.font.Font(None, self.size)
        self.print = font.render(text[id], True, col )




    def blit (self,sc,):
        sc.blit(self.print, (find_left_corner(self.print.get_size())))


