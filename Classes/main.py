from lab25_ATM import ATM

account1 = ATM(5000, [])


def main(account):
    while True:
        user_input = input(
            "What would you like to do? (deposit, withdraw, check balance, history)"
        )

        if user_input == "deposit":
            deposit_amount = int(input("How much would you like to deposit?: $"))
            account.deposit(deposit_amount)
        elif user_input == "withdraw":
            withdraw_amount = int(input("How much would you like to withdraw?: $"))
            account.withdraw(withdraw_amount)
        elif user_input == "check balance":
            print(f"Your balance is: ${account.check_balance()}")
        elif user_input == "history":
            account.print_transactions()
        elif user_input == "q":
            return False


main(account1)
