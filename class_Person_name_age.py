class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = Person('Anton', 21)
person2 = Person('Jordan', 24)
person3 = Person('Liza', 28)


print(f'Имя1: {person1.name} - Возраст: {person1.age}')
print(f'Имя2: {person2.name} - Возраст: {person2.age}')
print(f'Имя3: {person3.name} - Возраст: {person3.age}')



