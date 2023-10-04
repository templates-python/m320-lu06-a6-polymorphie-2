import pytest

from salary_account import SalaryAccount
from customer import Customer

class TestSalaryAccount:

    @pytest.fixture
    def owner(self):
        return Customer('Ria', 1995)

    @pytest.fixture
    def bc(self, owner):
        return SalaryAccount(owner, 1000.0, 4.5, 500)

    def test_salary_account_init(self, bc, owner):
        assert bc.owner == owner
        assert bc.balance == 1000.0
        assert bc.interest == 4.5
        assert bc.overdraw == 500
        assert bc.type == 'Salary bank account'

    def test_set_get_overdraw(self, bc):
        bc.overdraw = 250
        assert bc.overdraw == 250

    def test_withdraw_salary_account_well(self, bc):
        assert bc.is_withdraw_money(600.0) == True
        assert bc.balance == 400.0

    def test_withdraw_salary_account_overdraw(self, bc):
        assert bc.is_withdraw_money(1200.0) == True
        assert bc.balance == -200.0

    def test_withdraw_salary_account_empty(self, bc):
        assert bc.is_withdraw_money(1500)
        assert bc.balance == -500

    def test_withdraw_salary_account_ugly(self, bc):
        assert bc.is_withdraw_money(1501.0) == False

    def test_salary_account_print(self,bc, capsys):
        bc.print()
        captured = capsys.readouterr()
        assert captured.out == '------------------------------------------------\nKunde    : Ria\nKontotyp : Salary bank account\n\tSaldo: 1000.0\n\tZins : 4.5\n\tÜberzug: 500\n'


