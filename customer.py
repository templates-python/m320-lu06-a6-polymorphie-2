from person import Person
from account_index_exception import AccountIndexException



class Customer(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._accounts = []

    @property
    def number_of_accounts(self):
        return len(self._accounts)

    def take_bank_account(self, index):
        if index < self.number_of_accounts:
            return self._accounts[index]
        else:
            raise AccountIndexException(index, self.number_of_accounts)

    def add_bank_account(self, account):
        self._accounts.append(account)

    @property
    def current_assets(self):
        asset = 0
        for account in self._accounts:
            asset += account.balance
        return asset


    def print(self):
        super().print()
        for account in self._accounts:
            print(account.print())


if __name__ == '__main__':
    from bank_account import BankAccount
    from salary_account import SalaryAccount
    c  = Customer('Pia', 34)
    bc = BankAccount(c, 1000.00, 1.5)
    sc = SalaryAccount(c, 5000.00, 2.25, 2500.0)
    c.print()
