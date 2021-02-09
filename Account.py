
class Account:

    def __init__(self, number, holder, balance, limit = 1000):
        print("Construindo objeto ... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def bank_statement(self):
        print("The current bank balance is ${}".format(self.__balance))

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value
