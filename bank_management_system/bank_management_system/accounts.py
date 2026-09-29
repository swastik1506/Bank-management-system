from storage import load_accounts, save_accounts


def generate_account_number(accounts):
    """Generate the next account number (starts at 1001)."""
    if not accounts:
        return 1001
    return max(acc["account_number"] for acc in accounts) + 1


def create_account(name, opening_balance):
    """Create a new account and save it. Returns the new account dict."""
    accounts = load_accounts()
    new_account = {
        "account_number": generate_account_number(accounts),
        "name": name,
        "balance": round(opening_balance, 2)
    }
    accounts.append(new_account)
    save_accounts(accounts)
    return new_account


def find_account(account_number):
    """Return the account dict matching account_number, or None."""
    accounts = load_accounts()
    for acc in accounts:
        if acc["account_number"] == account_number:
            return acc
    return None


def update_balance(account_number, new_balance):
    """Update an account's balance and save it."""
    accounts = load_accounts()
    for acc in accounts:
        if acc["account_number"] == account_number:
            acc["balance"] = round(new_balance, 2)
    save_accounts(accounts)


def list_all_accounts():
    """Return the list of all accounts."""
    return load_accounts()
