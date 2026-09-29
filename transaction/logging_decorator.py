# logging_decorator.py
"""Decorator pattern: wrap a Transaction to add logging behavior."""

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class LoggingTransactionDecorator:
    """
    Decorator that wraps a Transaction and logs details when accessed/applied.

    Keeps the same amount/category interface so Balance.apply_transaction
    can use decorated transactions without changes.
    """

    def __init__(self, transaction: Transaction):
        if not isinstance(transaction, Transaction):
            raise TypeError(
                "LoggingTransactionDecorator requires a Transaction"
            )
        self._transaction = transaction
        self.logged = False

    @property
    def amount(self):
        return self._transaction.amount

    @property
    def category(self) -> TransactionCategory:
        return self._transaction.category

    def log(self):
        """Emit a log line for this transaction and mark it as logged."""
        print(
            f"[LOG] Preparing to apply {self._transaction} "
            f"(amount={self.amount}, category={self.category.name})"
        )
        self.logged = True
        return self

    def unwrap(self) -> Transaction:
        """Return the underlying Transaction."""
        return self._transaction

    def __str__(self):
        return f"Logged({self._transaction})"

    def __eq__(self, other):
        if isinstance(other, LoggingTransactionDecorator):
            return self._transaction == other._transaction
        if isinstance(other, Transaction):
            return self._transaction == other
        return NotImplemented
