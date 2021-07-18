import pygame as pg
from funksii import find_left_corner

pg.font.init()


class Text :
    def __init__(self,text,id,pos,size,col):
        self.text = text
        self.id = id
        self.pos = pos
        self.size = size
        self.col = col
        font = pg.font.Font(None, self.size)
        self.print = font.render(text[id], True, col )

    def set_id(self,id):
        self.id = id
        font = pg.font.Font(None, self.size)
        self.print = font.render(self.text[self.id], True, self.col)

    def blit(self,sc,):
        sc.blit(self.print, (find_left_corner(self.print.get_size())))


