
class Account:

    def __init__(self, number, holder, balance, limit = 1000):
        print("Construindo objeto ... {}".format(self))
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit
        # number, holder, balance, limit
