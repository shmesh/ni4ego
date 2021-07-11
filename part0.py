import pygame as pg
from funksii import find_left_corner

class Part :
    def __init__(self,part):
        self.part = part




    def story(self,text,sc):
        story_text = text
        counter = 0
        if self.part == 0 :
            for i in range(len(story_text)):
                counter += 1
                storyp = pg.font.Font(None, 36)
                story = storyp.render(story_text[counter], True, (0, 0, 0))
                sc.blit(story, (find_left_corner(story.get_size())))






