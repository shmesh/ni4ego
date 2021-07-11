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

    def robotakas(self,nomer, pkasa):
        self.lenta -= pkasa[0]

        self.pcount += pkasa[0]

        print(self.pcount, '- обслужено',nomer ,'-й','касой')

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




def obsushivanie(kasa1, kasa2, kasa3, pkasa, pkasa2, pkasa3):
    kasa1.robotakas(1,pkasa)
    kasa2.robotakas(2,pkasa2)
    kasa3.robotakas(3, pkasa3)



def rospredilenie(p):
     pkasa = []
     pkasa2 = []
     pkasa3 = [1]
     if p %2==0:
         pple = p //2
         pkasa.append(pple)
         pkasa2.append(pple)
         return pkasa , pkasa2 ,pkasa3
     if p %2!=0:
         pple = p //2 + 1
         pkasa.append(pple)
         pkasa2.append(pple + 1)
         return pkasa , pkasa2 , pkasa3




kasa1 = Kasa(10)
kasa2 = Kasa(10)
kasa3 = Kasa(10)
pple = rospredilenie(23)
obsushivanie(kasa1,kasa2,kasa3,pple[0],pple[1],pple[2])
