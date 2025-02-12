#Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
#Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.

class Animal:
    numInstances = 0
    def __init__(self):
        Animal.numInstances+=1
    def voice(self):
        pass

def printNumInstances():
    print(Animal.numInstances)

class Cat(Animal):
    def voice(self, sound='meow'):
        print(sound)

class Dog(Animal):
    def voice(self, sound='woof'):
        print(sound)

class Cow(Animal):
    def voice(self, sound='moo'):
        print(sound)

kitty = Cat()
tuzik = Dog()
murka = Cow()

printNumInstances()