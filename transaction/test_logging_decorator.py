import unittest

from transaction.logging_decorator import LoggingTransactionDecorator
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TestLoggingTransactionDecorator(unittest.TestCase):

    def test_decorator_exposes_amount_and_category(self):
        original = Transaction(80, TransactionCategory.EXPENSE)
        decorated = LoggingTransactionDecorator(original)
        self.assertEqual(decorated.amount, 80)
        self.assertEqual(decorated.category, TransactionCategory.EXPENSE)

    def test_log_marks_transaction_as_logged(self):
        original = Transaction(25, TransactionCategory.INCOME)
        decorated = LoggingTransactionDecorator(original)
        self.assertFalse(decorated.logged)
        decorated.log()
        self.assertTrue(decorated.logged)

    def test_unwrap_returns_original_transaction(self):
        original = Transaction(10, TransactionCategory.INCOME)
        decorated = LoggingTransactionDecorator(original)
        self.assertEqual(decorated.unwrap(), original)

    def test_equality_with_transaction(self):
        original = Transaction(40, TransactionCategory.EXPENSE)
        decorated = LoggingTransactionDecorator(original)
        self.assertEqual(decorated, original)

    def test_rejects_non_transaction(self):
        with self.assertRaises(TypeError):
            LoggingTransactionDecorator("not-a-transaction")


if __name__ == "__main__":
    unittest.main()
