import pygame as pg
import sys

pg.font.init()



ch1 = ['Ты оказываешься в машине полной подростков .Которые едут на тусовку на старом , но стильном фургончике .',
       '',
       '',]





sc = pg.display.set_mode((300, 200))
sc.fill((255, 255, 255))




storyp = pg.font.Font(None, 36)
text1 = f1.render9(ch1, True,
                  (180, 0, 0))




sc.blit(text1, (10, 50))


pg.display.update()
game = True
while game:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
