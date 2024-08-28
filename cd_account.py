"""Import the Account class from the Account.py file."""

from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    cd_account = Account(balance, interest_rate)
    interest_earned = float(cd_account.balance)*float(interest_rate)/100*float(months)
    cd_account.set_interest(interest_earned)
    cd_account.set_balance(float(cd_account.balance)+float(interest_earned))
    #balance = cd_account.balance+interest_earned
    return cd_account.balance, cd_account.interest
    
