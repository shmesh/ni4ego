import pygame as pg
import sys
from funksii import find_left_corner
from knopo4ki import knopo4ki

pg.font.init()


sc = pg.display.set_mode((1920,1080))
sc.fill((255, 255, 255))


x = 500
y = 1000

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0




pos1 = (500,640,150,70)
pos2 = (700,640,150,70)
pos3 = (900,640,150,70)
pos4 = (1100,640,150,70)










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
       'Mы(Alex) подымаемся в комнату пастора звонить, нам становится плохо , мы теряем сознание , нас ловит пастор , ТЕМНОТА.',
       'Выбырите персонажа']


choice_1 = ['Бенджи','Виола','Артемида','Исаак']




storyp = pg.font.Font(None, 36)


story = storyp.render(ch1[0], True,(0, 0, 0))



sc.blit(story, (find_left_corner(story.get_size())))

pg.display.update()


game = True

while game:

    for i in pg.event.get():


        if i.type == pg.KEYUP:


            if count1 <= 10:


                if i.key == pg.K_SPACE:
                    sc.fill(WHITE)

                    story =  storyp.render(ch1[count1], True, (0, 0, 0))

                    sc.blit(story, (find_left_corner(story.get_size())))

                    pg.display.update()

                    print(story.get_size())

                    count1 += 1

                    if count1 == 11:
                        count2 = 3
                        pass

            if count2 == 3:
                #knopka 1
                knopka = knopo4ki(choice_1[0],pos1)

                knopka.prorisovka(sc)

                # knopka 2
                knopka = knopo4ki(choice_1[1],pos2)

                knopka.prorisovka(sc)

                #knopka 3
                knopka = knopo4ki(choice_1[2],pos3)

                knopka.prorisovka(sc)

                #knopka 4
                knopka = knopo4ki(choice_1[3],pos4)

                knopka.prorisovka(sc)

                pg.display.update()










