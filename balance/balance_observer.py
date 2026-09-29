# balance_observer.py

class IBalanceObserver:
    def update(self, balance, transaction):
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    """Prints the balance whenever a transaction is applied."""

    def update(self, balance, transaction):
        """Print balance update message."""
        print(
            f"Balance changed after {transaction}. "
            f"Current balance: ${balance.get_balance():.2f}"
        )


class LowBalanceAlertObserver(IBalanceObserver):
    """Alerts when the balance falls below a configured threshold."""

    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def update(self, balance, transaction):
        """Alert if balance drops below threshold; clear alert when recovered."""
        current = balance.get_balance()
        if current < self.threshold:
            self.alert_triggered = True
            print(
                f"ALERT: Low balance! Current balance ${current:.2f} "
                f"is below threshold ${self.threshold:.2f}."
            )
        else:
            self.alert_triggered = False
