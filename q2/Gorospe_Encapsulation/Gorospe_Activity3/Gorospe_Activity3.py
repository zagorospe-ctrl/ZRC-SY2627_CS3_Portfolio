class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return f"{self.__account_number:.1f}"

    @property
    def balance(self):
        return f"{self.__balance:.1f}"

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = float(value)
        else:
            print("BALANCE MUST NOT BE LESS THAN 0")

print("Account 1")
a1 = BankAccount(12345, 1000)
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance}\n")

print("Update balance to -100")
a1.balance = -100
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance}")
