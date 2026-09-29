import unittest
from io import StringIO
from unittest.mock import patch

from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver, PrintObserver
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TestLowBalanceAlertObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_alert_triggers_on_low_balance(self):
        observer = LowBalanceAlertObserver(threshold=50)
        self.balance.register_observer(observer)

        income_100 = Transaction(100, TransactionCategory.INCOME)
        expense_60 = Transaction(60, TransactionCategory.EXPENSE)

        self.balance.apply_transaction(income_100)
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(expense_60)
        self.assertTrue(observer.alert_triggered)

        self.balance.apply_transaction(income_100)
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(expense_60)
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(expense_60)
        self.assertTrue(observer.alert_triggered)


class TestPrintObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_print_observer_outputs_on_transaction(self):
        observer = PrintObserver()
        self.balance.register_observer(observer)
        income = Transaction(30, TransactionCategory.INCOME)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.balance.apply_transaction(income)
            output = mock_stdout.getvalue()

        self.assertIn("Balance changed", output)
        self.assertIn("30.00", output)


if __name__ == "__main__":
    unittest.main()
