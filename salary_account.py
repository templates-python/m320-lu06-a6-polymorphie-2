import ssl

from bank_account import BankAccount
from customer import Customer

class SalaryAccount(BankAccount):

    def __init__(self, owner, deposit, interest, overdraw):
        super().__init__(owner, deposit, interest)
        self.overdraw = overdraw
        self._type    = 'Salary bank account'

    def is_withdraw_money(self, amount):
        if amount <= (self._balance + self._overdraw):
            self._balance -= amount
            return True
        else:
            return False

    @property
    def overdraw(self):
        return self._overdraw

    @overdraw.setter
    def overdraw(self, overdraw):
        self._overdraw = overdraw


    def print(self):
        super().print()
        print(f'\tÜberzug: {self.overdraw}')

#Test
if __name__ == '__main__':
    p  = Customer('Pia', 24)
    sc = SalaryAccount(p, 3500.00, 1.75, 1000.00)
    sc.print()