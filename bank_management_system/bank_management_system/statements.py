from transactions import get_transactions_for_account
from accounts import find_account


def _signed_amount(txn):
    """Return the amount as it affected the balance (+ or -)."""
    if txn["type"] in ("DEPOSIT", "TRANSFER_IN"):
        return txn["amount"]
    return -txn["amount"]


def generate_statement(account_number, month, year):
    """
    Print a statement for account_number for the given month/year.
    month: 1-12, year: e.g. 2026
    """
    account = find_account(account_number)
    if account is None:
        print("Account not found.")
        return

    all_txns = get_transactions_for_account(account_number)

    # Keep only transactions that happened in the requested month/year.
    month_txns = []
    for t in all_txns:
        txn_year, txn_month, _ = t["date"].split("-")
        if int(txn_year) == year and int(txn_month) == month:
            month_txns.append(t)

    print("\n" + "=" * 45)
    print(f"MONTH-END STATEMENT - {month:02d}/{year}")
    print("=" * 45)
    print(f"Account Number : {account['account_number']}")
    print(f"Account Holder : {account['name']}")
    print("-" * 45)

    if not month_txns:
        print("No transactions this month.")
    else:
        opening_balance = month_txns[0]["balance_after"] - _signed_amount(month_txns[0])
        print(f"Opening Balance: {opening_balance:.2f}\n")
        print(f"{'Date':<12}{'Type':<15}{'Amount':>10}{'Balance':>10}")
        for t in month_txns:
            print(f"{t['date']:<12}{t['type']:<15}{t['amount']:>10.2f}{t['balance_after']:>10.2f}")
        print(f"\nClosing Balance: {month_txns[-1]['balance_after']:.2f}")

    print(f"Current Balance: {account['balance']:.2f}")
    print("=" * 45 + "\n")
