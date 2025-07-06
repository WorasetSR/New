class Animal:
    name = ''
    ku = ''
    def kuu(self):
        print(self.name,':',self.ku)
class Dog(Animal):
    atk = ''
    def atkk(self):
        print(self.name,':',self.atk)

animal = Animal()
animal.ku = 'uhhhhh'
animal.name = 'poom'
animal.kuu()
dog = Dog()
dog.name = 'jane'
dog.ku = 'aaa'
dog.kuu()
dog.atk = 'punch'
dog.atkk()