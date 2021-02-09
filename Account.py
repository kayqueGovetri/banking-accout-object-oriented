class Account:

    def __init__(self, number, holder, balance, limit=1000):
        print("Building object ... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def bank_statement(self):
        print("The current bank balance is ${}".format(self.__balance))

    def deposit(self, value):
        self.__balance += value

    def __can_withdraw(self, value):
        available_withdraw = self.balance + self.limit
        return value <= available_withdraw

    def withdraw(self, value):
        if self.__can_withdraw(value):
            self.__balance -= value
        else:
            print("The value ${} has crossed the limit.".format(value))

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @property
    def number(self):
        return self.__number

    @staticmethod
    def bank_code():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

    @limit.setter
    def limit(self, value):
        self.__limit = value
