class MoneyNotEnoughError(Exception):
    """The money to be sent must be less than or equal to the initial balance."""
    pass


class PINCodeError(Exception):
    """The given PIN code must match the initial one."""
    pass


class UnderageTransactionError(Exception):
    """To perform online transactions, you must be 18 or older."""
    pass


class MoneyIsNegativeError(Exception):
    """If the given money is a negative number."""
    pass


def send_money(bank_account, command, valid_age):
    user_pin_code, initial_balance, age = bank_account
    money = int(command[1])
    pin_code = int(command[2])

    if money > initial_balance:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
    elif pin_code != user_pin_code:
        raise PINCodeError("Invalid PIN code")
    elif age < valid_age:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

    bank_account[1] -= money
    print(f"Successfully sent {money:.2f} money to a friend")
    print(f"There is {bank_account[1]:.2f} money left in the bank account")


def receive_money(bank_account, command):
    money = int(command[1])
    if money < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")
    bank_account[1] += money/2
    print(f"{money/2:.2f} money went straight into the bank account")


bank_account_details = list(map(int, input().split(", ")))

LEGAL_AGE = 18

command_input = input().split("#")

while command_input[0] != "End":

    if command_input[0] == "Send Money":
        send_money(bank_account_details, command_input, LEGAL_AGE)
    elif command_input[0] == "Receive Money":
        receive_money(bank_account_details, command_input)

    command_input = input().split("#")
