class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name)
        print(self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


t1 = BankAccount("Sumedha",0)

t1.display()
t1.withdraw(1000)
t1.display()
t1.deposit(1500)
t1.display()

