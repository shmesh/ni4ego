class y4enik:
    def __init__(self,name,age,addres):
        self.name = name
        self.age = age
        self.addres = addres
    def happy_bithday(self,age):
        self.age -= age
    def set_addres(self,addres):
        self.addres = addres






y41 = y4enik('Gleb',13,'planeta Obezian')
y42 = y4enik('Andrey',78,'nadavno svorovanaya nora')


y42.happy_bithday(15)
y42.set_addres('planeta Obezian')

print(y41.name)
print(y41.age)
print(y41.addres)
print(y42.name)
print(y42.age)
print(y42.addres)




