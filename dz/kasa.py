import pygame as pg
import random as r



count = 0




class Kasa:
    def __init__(self,lenta):
        self.lenta = lenta
        #self.money = 0
        self.pcount = 0
        #self.day = 0
        #self.dayc = 0
        #self.zlentu = 0
        #self.lenta = self.zlentu

        # while True:
        #     if self.day == 0  and  self.day == self.dayc:
        #         self.zlentu = r.randint(3, 13)
        #         print
        #     self.lenta = 1
        #     self.pcount += 1
        #     print(self.lenta,self.zlentu)
        #     #random money


                # if self.lenta == 0 :
                #     self.zlentu -= 1
                #     self.lenta += 1
                #     print('касир заправил касовый апарат')
                #
                #
                #     if self.zlentu == 0 :
                #             if self.zlentu == 0:
                #                 self.money = r.randint(1000, 10000)
                #                 self.day += 1
                #                 print('Выручка за сегодня составила -',self.money,'Обслужено клиентов -', self.pcount)
                #                 print('Касир закрыавет магазин ')
                #                 self.dayc += 1
                #                 input


    def obsushivanie(self):

        for i in range(self.lenta):
            self.lenta -= 1
            self.pcount += 1
            print(self.pcount, '- обслужено')

    def count(self,kasa2):
            self.lenta =- 1

            self.pcount += 1


            kasa2.lenta =- 1

            self.pcount += 1
            print(self.pcount, '- обслужено')





kasa1 = Kasa(4)
kasa2 = Kasa(4)
kasa1.count(kasa2)
