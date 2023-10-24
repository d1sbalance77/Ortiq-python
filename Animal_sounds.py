class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав!"

class Cat(Animal):
    def make_sound(self):
        return "Mяу!"

class Cow(Animal):
    def make_sound(self):
        return "Муу!"

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.make_sound())
print(cat.make_sound())
print(cow.make_sound())

