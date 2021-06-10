import pygame as pg
from funksii import knopka
BLACK = [0,0,0]
WHITE = [255,255,255]
rect_1 = [200,50,100,40]
rect_2 = [400,50,100,40]
rect_3 = [600,50,100,40]
rect_4 = [800,50,100,40]
choice_1 = ['Бенджи','Виола','Артемида','Исаак']
sc = pg.display.set_mode((1000,800))
sc.fill((255, 255, 255))
pg.draw.rect(sc,BLACK,rect_1)
pg.draw.rect(sc,BLACK,rect_2)
pg.draw.rect(sc,BLACK,rect_3)
pg.draw.rect(sc,BLACK,rect_4)
while True:
    pg.display.flip()



    for i in pg.event.get():
        print(i)
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                pos = pg.mouse.get_pos()
                print(pos)
                knopka(pos,rect_1)
                knopka(pos,rect_2)
                knopka(pos,rect_3)
                knopka(pos,rect_4)






