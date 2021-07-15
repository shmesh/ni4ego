import pygame as pg
import sys
from funksii import find_left_corner
from knopo4ki import Knopo4ki
from Picture import Picture
from Text import Text

# Основное
pg.font.init()
sc = pg.display.set_mode((1920,1080))
sc.fill((255, 255, 255))

ch1 = ['Ты оказываешься в машине полной подростков .',
       'Которые едут на тусовку на старом , но стильном фургончике .',
       'Машина глохнет',
       'Компания подростков решает переждать дождь и дозвониться эвакуатору ',
       'Ближайшим местом оказалась маленькая католическая церковь ',
       'Там горел свет , они отправились туда.',
       'Внутри они встретили пастора',
       'При них пастор открывает подсобку , достает пледы и закрывает подсобку ключом  ',
       'Пастор предлагает позвонить эвакуатору из его комнаты ',
       'Mы(Alex) подымаемся в комнату пастора звонить, нам становится плохо , мы теряем сознание , нас ловит пастор , ТЕМНОТА.',
       'Выбырите персонажа']
pos1 = (500,640,150,70)
size = (36)
BLACK = (0,0,0)
text = Text(ch1,1,pos1,size,BLACK)


size = (600,800)
pos = (500,640)
path = 'kartinki\\furgon.jpg'
pic_1 = Picture(size,path,pos)

TEXT = "Hello W0rld"
pos = (600,400,150,50)
col = (0,50,0)
knopka_1 = Knopo4ki(TEXT,pos,col)






game = True
while game:
    pic_1.prorisovka(sc)

    text.blit(sc)

    knopka_1.prorisovka(sc)

    pg.display.update()