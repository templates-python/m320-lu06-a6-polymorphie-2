from customer import Customer
from bank_account import BankAccount
from salary_account import SalaryAccount


if __name__ == '__main__':
    customer        = Customer('Pia', 23)
    customer.address = 'Hochdorf'
    #
    account_1       = BankAccount(customer, 1000.0, 1.25)
    account_2       = SalaryAccount(customer, 1000.0, 2.25, 500.0)
    #
    print('Angaben zu Kunde')
    print(f'\tName: {customer.name}\n\tAlter: {customer.age}\n\tAdresse: {customer.address}')
    print('Angaben zum den Konti')
    for index in range(2):
        print(f'\t {customer.take_bank_account(index).type}')
    #-----------------------------------------------------------------------------------------------
    print('\nvon jedem Konto 750.0 beziehen')
    print(f'\tBezug von {account_1.type}')
    if account_1.is_withdraw_money(750):
        print(f'\tSaldo = {account_1.balance}')
    else:
        print(f'\tFehler: Bezug ist zu hoch für Saldo von {account_1.balance}')

    print(f'\tBezug von {account_2.type}')
    if account_2.is_withdraw_money(750):
        print(f'\tSaldo = " {account_2.balance}')
    else:
        print(f'\tFehler: Bezug ist zu hoch für Saldo von {account_2.balance}')
    print('Aktuelles Vermögen: ' + str(customer.current_assets))
    #----------------------------------------------------------------------------------------------
    print('\nvon jedem Konto noch einmal 400.0 beziehen')
    print(f'\tBezug von {account_1.type}')
    if account_1.is_withdraw_money(400):
        print(f'\tSaldo = " {account_1.balance}')
    else:
        print(f'\tFehler: Bezug ist zu hoch für Saldo von {account_1.balance}')

    print(f'\tBezug von {account_2.type}')
    if account_2.is_withdraw_money(400):
        print(f'\tSaldo = {account_2.balance}')
    else:
        print(f'\tFehler: Bezug ist zu hoch für Saldo von {account_2.balance}')
    print(f'Aktuelles Vermögen: {customer.current_assets}')
    #-----------------------------------------------------------------------------------------------
    print('\nEnde Monat: 3000.- Lohn wird eingezahlt')
    account_2.pay_in_money(3000.00)
    print(f'Aktuelles Vermögen: {customer.current_assets}')
