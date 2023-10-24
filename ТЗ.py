
class BankAccount:
    def __init__(self, client_name, balance=0):
        self.client_name = client_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств на счете")

    def my_balance(self):
        print(f"Баланс клиента {self.client_name}: {self.balance}")


