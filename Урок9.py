# class User:
#     name = 'Jordan'
#     age = 23
#     job = 'Programmer'


# class Car:
#     name = 'Bugatti'
#     color = 'black'
#     max_speed = 360


# class Car:
#     def __init__(self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# gentra  = Car('Chevrolet','black',2023)
# print(gentra.model, gentra.color, gentra.year)


# class Comment:
#     def __init__(self,username,text,likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
# man1 = Comment('Anton', 'Best', 99)
# man2 = Comment('Qwerty', 'c# better', 5)
# print(man1.username,man1.text,man1.likes)
# print(man2.username,man2.text,man2.likes)



# class Car:
#      def __init__(self,model,color,year):
#          self.model = model
#          self.color = color
#          self.year = year
#
#      def start(self):
#          print('Проежайте')
#
#      def stop(self):
#          print('Машина остановилось')
#
# bmw = Car('x5', 'black', 2020)
# bmw.stop()


class BankAccount:

    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def cash(self, amount):
        if self.balance >= amount:
         self.balance -= amount
        else:
            print("Недостаточно средств на счете")

    def my_balance(self):
        print(f'Баланс клиента {self.name}: {self.balance}')







