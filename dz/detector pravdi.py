class Human:
    def __init__(self, name,sername, age, balance):
        self.name = name
        self.sername = sername
        self.age = age
        self.balance = balance


    def detektor(self):
        print('это детектор "ПРАВДЫ",он сделан что-бы понянь настоколько человек чист.')
        if self.age <= 10:
            if self.balance > 1000000:
                if self.name == 'Ричард':
                    return 'ричард , иди гуляй!!!!111!!!'
        if self.age >= 40 :
            if self.balance > 500000:
                return 'Ты крутой порядочеый человек'
        if self.age >= 19 :
            if self.balance > 100000 :
                return 'Ты Таксист'
        return 'Ты случайноли не ричард?'




richard = Human('Олег','Коваленко',41,100)
r = richard.detektor()
print(r)
