# Personal Finance Manager — Design Patterns Project

A simplified personal finance manager built with classic object-oriented design patterns in Python.

## Features

- Track income and expenses through a shared balance
- Adapt third-party freelance income into internal transactions
- Observe balance changes and alert on low funds
- Optionally log selected transactions before they are applied

## Getting Started

### Requirements

- Python 3.8+ (3.10+ recommended)
- Standard library only (`unittest` for tests)

### Run the app

```bash
cd starter
python main.py
```

### Run tests

From the `starter/` folder:

```bash
python -m unittest discover
```

Single file example:

```bash
python -m unittest balance.test_balance_observer
```

## Project Structure

```
starter/
├── main.py
├── balance/
│   ├── balance.py                 # Singleton + subject for observers
│   ├── balance_observer.py        # PrintObserver, LowBalanceAlertObserver
│   ├── test_balance.py
│   └── test_balance_observer.py
└── transaction/
    ├── transaction.py             # Transaction model
    ├── transaction_category.py    # INCOME / EXPENSE enum
    ├── external_income_transaction.py
    ├── transaction_adapter.py     # Adapter pattern
    ├── logging_decorator.py       # Decorator pattern (4th pattern)
    ├── test_transaction.py
    ├── test_transaction_adapter.py
    └── test_logging_decorator.py
```

## Design Patterns Used

### 1. Singleton — `Balance`
Ensures one shared balance across the app via `Balance.get_instance()`. Direct construction raises an error. This avoids inconsistent balances from multiple instances.

### 2. Adapter — `TransactionAdapter`
Converts `ExternalFreelanceIncome` (invoice ID, project details, third-party shape) into a standard `Transaction` with `TransactionCategory.INCOME`, so the rest of the app never depends on external formats.

### 3. Observer — `PrintObserver` + `LowBalanceAlertObserver`
`Balance` notifies registered observers after each applied transaction. `PrintObserver` prints the updated balance; `LowBalanceAlertObserver` sets an alert when the balance falls below a threshold and clears it when the balance recovers.

### 4. Decorator — `LoggingTransactionDecorator` (student choice)
Wraps a `Transaction` and adds logging without changing `Balance` or `Transaction`. Decorated objects still expose `amount` and `category`, so they can be applied like normal transactions. This keeps logging optional and removable.

## Reflection

- **Singleton:** Centralized money state; trade-off is harder isolated testing unless `reset()` clears state (used in tests).
- **Adapter:** Keeps external freelance data out of core logic; trade-off is an extra class when formats are similar.
- **Observer:** Decouples alerts/UI side effects from balance math; trade-off is needing care with notification order and leftover registrations (cleared on `reset()`).
- **Decorator:** Adds logging without modifying core classes; trade-off is another wrapper type callers must remember to use when logging is desired.

## License

See repository `LICENSE.txt`.
