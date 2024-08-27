#####################################################################
#                                                                   #
# Creating a customer banking system that allows users to calculate #
# and track interest earned on savings and CD accounts.             #
# By running this application, users will be able to enter their    #
# savings and CD account information, see the interest earned,      #
# and view the updated balances after a specified number of months. #
#                                                                   #
#####################################################################



# Import the create_cd_account and create_savings_account functions

from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
   
    savings_balance = input("Input the savings balance: ")
    savings_interest = input("Input the Interest rate: ")
    savings_maturity = input("Input the savings maturity/months: ")
    print("Initial Savings balance",savings_balance)
    print("Interest rate", savings_interest)
    print("Savings maturity/Number of months", savings_maturity)
 


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    
    print(f"Updated saving account balance :${updated_savings_balance:,.2f}")
    print(f"Interest earned for the given months :${interest_earned:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
   
    cd_balance = input("Input the cd balance: ")
    cd_interest = input("Input the Interest rate: ")
    cd_maturity = input("Input the cd maturity/months: ")
    print("Initial CD balance",cd_balance)
    print("Interest rate", cd_interest)
    print("CD Maturing/Number of months", cd_maturity)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    
    print(f"Updated CD account balance :${updated_cd_balance:,.2f}")
    print(f"Interest earned for the given number of months :${interest_earned:,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
    
