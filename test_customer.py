import pytest

from customer import Customer
from bank_account import BankAccount
from account_index_exception import AccountIndexException

class TestCustomer:

    @pytest.fixture
    def tom(self):
        return Customer('Tom', 2000)

    @pytest.fixture
    def ba(self, tom):
        return BankAccount(tom, 1000, 3.3)

    def test_customer_init(self, tom):
        assert tom.name == 'Tom'
        assert tom.age == 2000


    def test_number_of_initial_accounts(self, tom, ba):
        # first account "ba" is assigned to the client's portfolio (in the constructor of BankAccount)
        assert tom.number_of_accounts == 1

    def test_take_account_well(self, tom, ba):
        assert tom.take_bank_account(0) == ba

    def test_take_account_ugly(self, tom, ba):
        with pytest.raises(AccountIndexException):
            assert tom.take_bank_account(1)

    def test_add_account(self, tom, ba):
        ba2 = BankAccount(tom, 5000, 2.2)
        assert tom.number_of_accounts == 2


    def test_current_assets(self, tom, ba):
        BankAccount(tom, 5000, 2.2)
        BankAccount(tom, 201, 5.5)
        assert tom.current_assets == 6201


    def test_customer_print(self, tom, ba, capsys):
        tom.address = 'Testadresse'
        tom.print()
        captured = capsys.readouterr()
        assert captured.out == 'Person: Tom\n\tAlter :   2000\n\tAdresse : Testadresse\n------------------------------------------------\nKunde    : Tom\nKontotyp : Standard bank account\n\tSaldo: 1000\n\tZins : 3.3\nNone\n'


