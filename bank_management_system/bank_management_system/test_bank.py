from accounts import create_account, find_account
from transactions import deposit, withdraw, transfer


def test_create_account():
    account = create_account("Test User A", 1000)
    assert account["balance"] == 1000
    print("test_create_account PASSED")
    return account["account_number"]


def test_deposit(acc_no):
    success, _ = deposit(acc_no, 500)
    account = find_account(acc_no)
    assert success is True
    assert account["balance"] == 1500
    print("test_deposit PASSED")


def test_withdraw(acc_no):
    success, _ = withdraw(acc_no, 5000)          # should fail: too much
    assert success is False
    success, _ = withdraw(acc_no, 500)           # should succeed
    assert success is True
    account = find_account(acc_no)
    assert account["balance"] == 1000
    print("test_withdraw PASSED")


def test_transfer(acc_no):
    account_b = create_account("Test User B", 0)
    success, _ = transfer(acc_no, account_b["account_number"], 400)
    assert success is True
    assert find_account(acc_no)["balance"] == 600
    assert find_account(account_b["account_number"])["balance"] == 400
    print("test_transfer PASSED")


if __name__ == "__main__":
    acc_no = test_create_account()
    test_deposit(acc_no)
    test_withdraw(acc_no)
    test_transfer(acc_no)
    print("\nAll tests passed!")
