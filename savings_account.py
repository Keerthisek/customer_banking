"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):    
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    saving_account = Account(balance, interest_rate)
    interest_earned = float(saving_account.balance)*float(interest_rate)/100*float(months)
    saving_account.set_interest(interest_earned)
    saving_account.set_balance(float(saving_account.balance)+float(interest_earned))
    return saving_account.balance, saving_account.interest
