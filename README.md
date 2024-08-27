Customer Banking

Overview:

Creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

Files:

Main file: Customer_banking.py

Other supportive files that we are importing into main file:

account.py

savings_Account.py

cd_account.py

https://github.com/Keerthisek/customer_banking

Repo name - customer_banking

File names and variables definitions:

The Accounts.py file contains the Account class with methods to set the balance and interest.

In the savings_account.py file, we import the Account class and create a create_savings_account function that will create a savings account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned. (savings_account.balance and interest_earned)

In the cd_account.py file, we import the Account class and create a create_cd_account function that will create a CD account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.(cd_account.balance and interest_earned)

In the customer_banking.py file, we will import the create_savings_account and create_cd_account functions, then create a main function  that prompts the user to enter the savings and CD account details, call the corresponding functions to calculate the interest earned and update the balances, and display the results. 


Code Source: 

Given starters file and building the logic on the given files. 

Results:

Open the customer_banking.py file and import the create_cd_account and create_savings_account functions from the appropriate files.

In the main function, prompt the user to set the savings balance, interest rate, and months for the savings account.

Print out the interest earned and updated savings account balance with interest earned for the given months seperatly for savings account and CD account.





