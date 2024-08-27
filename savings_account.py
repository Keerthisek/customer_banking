"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    saving_account = Account(balance, interest_rate)
    interest_earned = float(saving_account.balance)*float(interest_rate)/100*float(months)
    saving_account.set_interest(interest_earned)
    saving_account.set_balance(float(saving_account.balance)+float(interest_earned))
    return saving_account.balance, saving_account.interest
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    

    # Calculate interest earned
    

    # Update the savings account balance by adding the interest earned
    

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    

    # Return the updated balance and interest earned.
    
