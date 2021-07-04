import pygame as pg

class Human:
     def __init__(self,name,age,balance):
         self.name = name
         self.age = age
         self.balance = balance


     def age_changer(self):
         self.age += 1


     def balance_changer(self,money):
         self.balance = money

     def svinia_kalkulator(self):
         #1008grn stoimost svinii
         svinii = self.balance // 1008
         return svinii


     def info(self):
         print('Это',self.name)
         if self.age <= 20:
             print('он еще совсем ребенок ему -', self.age)
         elif self.age >= 20:
             print('он далеко не ребенок ему -', self.age)
         if self.balance >= 10000:
             print(self.name,'может купить себе свеней :',self.svinia_kalkulator())





vova = Human('Vova',46,-10000)
vova.age_changer()
vova.balance_changer(11000)
vova.info()

