class ATM:
    def __init__(self, balance: int, transactions: list):
        self.balance = balance
        self.transactions = transactions

    def print_transactions(self):
        for transaction in range(len(self.transactions)):
            print(self.transactions[transaction])

    def check_balance(self) -> int:
        """Returns the account Balance"""
        self.transactions.append(f'Checked Account Balance: {self.balance}')
        return self.balance

    def deposit(self, amount: int) -> int:
        """Deposits the given amount in the account"""
        self.balance = self.balance + amount
        self.transactions.append(f'Deposit to Account: {amount}')
        return self.balance

    def check_withdrawal(self, amount: int) -> bool:
        """Returns True if the withdrawn amount won't put the account in the negative"""
        if self.balance - amount >= 0:
            self.transactions.append(f'Checked Withdrawal: -{amount} from {self.balance}')
            return True
        else:
            self.transactions.append(f'Checked Withdrawal: -{amount} from {self.balance}')
            return False

    def withdraw(self, amount: int) -> int:
        """Withdraws the amount from the account and returns it"""
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            self.transactions.append(f'Withdrew from Account: -{amount}')
            return self.balance
        pass
