from customer import Customer

class BankAccount:
    """
    Ein (einfaches) Bankkonto
    """

    def __init__(self, owner, first_deposit, interest):
        self._owner   = owner
        self._balance = first_deposit
        self._interest = interest
        self._type = 'Standard bank account'
        owner.add_bank_account(self)

    def is_withdraw_money(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def pay_in_money(self, amount):
        self._balance += amount

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, interest):
        self._interest = interest

    @property
    def type(self):
        return self._type

    def print(self):
        print('------------------------------------------------')
        print(f'Kunde    : {self.owner.name}')
        print(f'Kontotyp : {self._type}')
        print(f'\tSaldo: {self.balance}')
        print(f'\tZins : {self.interest}')


#Test
if __name__ == '__main__':
    p  = Customer('Pia', 24)
    ac = BankAccount(p, 3500.00, 1.75)
    ac.print()
