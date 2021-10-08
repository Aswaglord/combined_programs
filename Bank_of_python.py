account_balance = 1000.00
program_running = True

def withdraw(account_balance):
    withdraw_amount = float(input("how much would you like to withdraw: "))
    if withdraw_amount > account_balance:
        print("Error, your trying to withdraw more than you have")
    else:
        account_balance -= withdraw_amount   
        print(f"you have received {withdraw_amount:.2f}, your new balance is {account_balance:.2f}")
    return account_balance
    
def deposit(account_balance):
    deposit_amount = float(input("how much money would you like to deposit: "))
    if deposit_amount < 0:
        print("you cannot deposit a negative amount")
    else:
        account_balance += deposit_amount
        print(f"you have deposited {deposit_amount:.2f}, your new balance is: {account_balance:.2f}")
    return account_balance

def check_balance(account_balance):
    print(f"your current balance is: {account_balance:.2f}")    
    return account_balance

while program_running: 
    print()
    options = input("please select from the following menu options:\n(B)alance\n(D)eposit\n(W)ithdraw\n(Q)uit\n").capitalize()
    print()
    if options == "B":
        account_balance = check_balance(account_balance)
    elif options == "D":
        account_balance = deposit(account_balance)
    elif options == "W":
        account_balance = withdraw(account_balance)
    elif options == "Q":
        print("Goodbye. Please come again")
        program_running = False
        quit()