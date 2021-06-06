import pygame as pg
import sys
from funksii import find_left_corner

pg.font.init()


sc = pg.display.set_mode((1920,1080))
sc.fill((255, 255, 255))


x = 500
y = 1000

count = 0

WHITE = [255,255,255]

ch1 = ['Ты оказываешься в машине полной подростков .',
       'Которые едут на тусовку на старом , но стильном фургончике .',
       'Машина глохнет',
       'Компания подростков решает переждать дождь и дозвониться эвакуатору ',
       'Ближайшим местом оказалась маленькая католическая церковь ',
       'Там горел свет , они отправились туда.',
       'Внутри они встретили пастора',
       'При них пастор открывает подсобку , достает пледы и закрывает подсобку ключом  ',
       'Пастор предлагает позвонить эвакуатору из его комнаты ',
       'Mы(Alex) подымаемся в комнату пастора звонить, нам становится плохо , мы теряем сознание , нас ловит пастор , ТЕМНОТА.',]


choice_1 = ['Бенджи','Виола','Артемида','Исаак']



storyp = pg.font.Font(None, 36)


story = storyp.render(ch1[0], True,(0, 0, 0))



sc.blit(story, (find_left_corner(story.get_size())))

pg.display.update()


game = True

while game:
    for i in pg.event.get():


        if i.type == pg.QUIT:
            game = False


        if i.type == pg.KEYUP:
            if i.key == pg.K_SPACE:
                story =  storyp.render(ch1[count], True, (0, 0, 0))
                sc.blit(story, (find_left_corner(story.get_size())))
                pg.display.update()
                sc.fill(WHITE )
                print(story.get_size())
                count += 1