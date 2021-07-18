import pygame as pg
from scene import scene_1, scene_2, scene_3, scene_4

# Основное
pg.font.init()
sc = pg.display.set_mode((1920,1080))
sc.fill((255, 255, 255))


count = 0

fps = 1
clock = pg.time.Clock()

game = True
while game:
    sc.fill((255, 255, 255))

    if count == 0:
        scene_1(sc)
    if count == 1:
        scene_2(sc)
    if count == 2:
        scene_3(sc)
    if count == 3:
        scene_4(sc)
    count += 1
    pg.display.update()
    clock.tick(fps)
