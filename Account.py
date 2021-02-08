
class Account:

    def __init__(self, number, holder, balance, limit = 1000):
        print("Construindo objeto ... {}".format(self))
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def bank_statement(self):
        print("The current bank balance is ${}".format(self.balance))

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value
