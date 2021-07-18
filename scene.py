import pygame as pg
import sys
from funksii import find_left_corner
from knopo4ki import Knopo4ki
from Picture import Picture
from Text import Text


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

text = Text(ch1, 1, pos=(500, 640, 150, 70), size=(36), col=(0, 0, 0))
text.set_id(1)
pic_1 = Picture(size=(600, 800), path='kartinki\\furgon.jpg', pos=(0, 0))
pic_2 = Picture(size=(600, 800), path='kartinki\\p.jpg', pos=(600, 0))
pic_3 = Picture(size=(600, 800), path='kartinki\\loc.jpg', pos=(1200, 0))

knopka_1 = Knopo4ki(text="1", pos=(200, 600, 150, 50), col=(0, 50, 0))
knopka_2 = Knopo4ki(text="2", pos=(400, 600, 150, 50), col=(50, 0, 0))
knopka_3 = Knopo4ki(text="3", pos=(600, 600, 150, 50), col=(0, 0, 50))
knopka_4 = Knopo4ki(text="4w", pos=(800, 600, 150, 50), col=(50, 50, 50))



def scene_1(sc):
    text.set_id(0)
    text.blit(sc)
def scene_2(sc):
    text.set_id(1)
    text.blit(sc)
def scene_3(sc):
    text.set_id(2)
    text.blit(sc)
def scene_4(sc):
    text.set_id(3)
    text.blit(sc)

