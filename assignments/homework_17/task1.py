def animal_talk(animal):
    print(animal.talk())

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return 'woof woof'
class Cat(Animal):
    def talk(self):
        return 'meow meow'
class Goose(Animal):
    def talk(self):
        return 'ga ga ga ga'

dog = Dog()
cat = Cat()
goose = Goose()

animal_talk(dog)
animal_talk(cat)
animal_talk(goose)