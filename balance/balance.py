# balance.py

from transaction.transaction_category import TransactionCategory


class Balance:
    """Singleton to track the balance and notify observers of changes."""

    _instance = None

    def __init__(self):
        """Prevent direct instantiation; use get_instance() instead."""
        raise RuntimeError("Use Balance.get_instance() to access the Balance singleton.")

    @classmethod
    def get_instance(cls):
        """Return the single Balance instance, creating it if needed."""
        if cls._instance is None:
            instance = cls.__new__(cls)
            instance._net_balance = 0.0
            instance._observers = []
            cls._instance = instance
        return cls._instance

    def reset(self):
        """Reset the net balance to zero and clear observers."""
        self._net_balance = 0.0
        self._observers = []

    def register_observer(self, observer):
        """Register an observer to receive balance updates."""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        """Unregister an observer."""
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify_observers(self, transaction):
        """Notify all registered observers after a transaction is applied."""
        for observer in list(self._observers):
            observer.update(self, transaction)

    def add_income(self, amount):
        """Add income to the balance."""
        self._net_balance += amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self._net_balance -= amount

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        if transaction.category == TransactionCategory.INCOME:
            self.add_income(transaction.amount)
        elif transaction.category == TransactionCategory.EXPENSE:
            self.add_expense(transaction.amount)
        else:
            raise ValueError("Invalid transaction category")
        self._notify_observers(transaction)

    def get_balance(self):
        """Get the current net balance."""
        return self._net_balance

    def summary(self):
        """Return a summary string of the net balance."""
        return f"Net Balance: ${self._net_balance:.2f}"
