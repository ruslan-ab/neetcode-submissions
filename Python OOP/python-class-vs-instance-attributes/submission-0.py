class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name: string, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
# TODO: Print the information using the mentioned format
aa = BankAccount("Alice", 1000)
ba = BankAccount("Bob", 2000)

print(f"{aa.name}'s balance: ${aa.balance}")
print(f"{ba.name}'s balance: ${ba.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")