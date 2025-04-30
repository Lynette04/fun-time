#This is a simple bank program. The user is askedd to enter their account number and password inorder to carry out a withdraw, deposit or just quit the session.
#It implements functions and a while loop with multiple if statements. A sample of account numbers and their passwords is given for testing purposes. 

Accounts={
    "6081234567890":"pass@345L",
    "6084567846578":"Secret564",
    "6087564536845":"Acfste45!"
}

def get_minimum_balance(Account_number):
    return 20000
def get_current_balance(Account_number):
    return 20000 #Assuming the current balance starts as the minimum balance before any deposit is made.
def check_withdraw_possibility(minimum_balance,current_balance,withdraw):
    if withdraw > current_balance:
        print("You have insufficient funds.")  
        return current_balance
    if current_balance-withdraw < minimum_balance:
        print("You cannot withdraw since your minimum balance should remain UGX 20000. ")
        return current_balance
    current_balance-=withdraw
    print(f"You have withdrawn UGX {withdraw} and your current balance is UGX {current_balance}.")
    return current_balance
  
Account_number=input("Welcome! Please enter your Account_number: ")

if len(Account_number)!=13 and Account_number[:3]!='608':
    print("Please enter a valid Account_number that is 13 digits long and starts with '608': ")
elif Account_number not in Accounts:
    print("The account number does not exist.")
else:
    password=input("Enter your account password: ")
    if password!=Accounts[Account_number]:
        print("Invalid password, Access denied!")
    else:
        print("Access granted!")
        minimum_balance=get_minimum_balance(Account_number)
        current_balance=get_current_balance(Account_number)
     
        while True: 
            operation=input("Do you want to deposit(D),withdraw(W) or quit(Q): ").upper()
            if operation=='D':
              deposit=int(input("Enter an amount to deposit: "))
              current_balance=deposit+current_balance
              print(f"You have deposited UGX {deposit} and now your current balance is UGX {current_balance}.")
            elif operation=='W':
              withdraw=int(input("Enter an amount to withdraw: "))
              print(f"current_balance={current_balance}")
              previous_balance=current_balance
              current_balance=check_withdraw_possibility(minimum_balance,current_balance,withdraw)
              if previous_balance==current_balance:
                  print("Withdrawal attempt failed!")
            elif operation=='Q':
               print("You have closed your session.")
               break
            else:
                print("I don't understand what you want to do.")
    print("Thank you for banking with us!")            