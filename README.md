# BudJet CLI

An early Python budgeting experiment for recording income and expenses in a CSV file.

The command-line workflow asks for a transaction date, amount, category, and description, then appends a row to `finance_data.csv`. It is the predecessor to the [Django prototype](https://github.com/clechz/budjet2.0).

## Structure

- `app.py` handles CSV initialization, transaction entry, and balance calculation.
- `data.py` contains input helpers.
- `finance_data.csv` stores the transaction rows.

## Run locally

Use Python in an isolated environment and a disposable copy of the data file:

```bash
python -m venv .venv
# Activate .venv using the command for your shell.
python -m pip install pandas
python app.py
```

Run from the repository root. Follow the prompts; dates use `dd-mm-yyyy`.

## Prototype limits

The balance calculation assumes existing numeric balances. The first transaction in an empty file can receive no balance, and later reads can then fail. Backdated entries do not recalculate subsequent balances. The script also prints transaction rows for debugging.

This repository preserves the original learning experiment. Use synthetic data when exploring it.
