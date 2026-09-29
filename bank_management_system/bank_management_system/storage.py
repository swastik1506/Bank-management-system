import json
import os

DATA_FOLDER = "data"
ACCOUNTS_FILE = os.path.join(DATA_FOLDER, "accounts.json")
TRANSACTIONS_FILE = os.path.join(DATA_FOLDER, "transactions.json")


def ensure_data_folder():
    """Create the data folder if it does not already exist."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


def load_accounts():
    """Load the list of accounts from file. Returns [] if none exist."""
    ensure_data_folder()
    if not os.path.exists(ACCOUNTS_FILE):
        return []
    with open(ACCOUNTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_accounts(accounts):
    """Save the list of accounts to file."""
    ensure_data_folder()
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=4)


def load_transactions():
    """Load the list of transactions from file. Returns [] if none exist."""
    ensure_data_folder()
    if not os.path.exists(TRANSACTIONS_FILE):
        return []
    with open(TRANSACTIONS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_transactions(transactions):
    """Save the list of transactions to file."""
    ensure_data_folder()
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump(transactions, f, indent=4)
