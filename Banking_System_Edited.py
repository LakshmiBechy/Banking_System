import datetime
import pwinput

# defining a customer class


class Customer:
    def __init__(self,acct_no,name,pin,balance=0.0):
        self.acct_no=acct_no
        self.name=name
        self.pin=pin
        self.balance=balance
        self.transactions=[]
        date_of_acct_creation=datetime.datetime.now()
        formatted_date=date_of_acct_creation.strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append((formatted_date,'Account created with a balance of: {}'.format(self.balance)))

    def deposit(self,amount):
        self.balance+=amount
        transaction_time=datetime.datetime.now()
        self.transactions.append((transaction_time.strftime("%Y-%m-%d %H:%M:%S"),'Deposited: {}'.format(amount)))
        print("Rs.{} has been credited to your account.\nYour current balance is: {}".format(amount,self.balance))

    def withdraw(self,amount):
        withdrawal_limit=500
        if amount > self.balance:
            print("Sorry, You have insufficient balance for this transaction")
        else:
            if self.balance-amount>500:
                self.balance -= amount
                transaction_time = datetime.datetime.now()
                self.transactions.append(
                    (transaction_time.strftime("%Y-%m-%d %H:%M:%S"), 'Withdrew: {}'.format(amount)))
                print("Rs.{} has been debited from your account. Your current balance is: {}".format(amount,
                                                                                                     self.balance))
            else:
                print("Sorry,Minimum balance should be 500")

    def display_balance(self):
        print("Account Number:",self.acct_no,"\nName:",self.name,"\nYour account balance is:",self.balance)

    def view_transactions(self):
        print("\nTransaction history:\n*******************")
        for t in self.transactions:
            print('{}:{}'.format(t[0],t[1]))

    def close_account(self):
        self.balance=0
        print("Account closed successfully")
# ------------------------------------------End of Class----------------------------------------------------------------


# list to store customer details
account_holders = []


# function to input user information to create a new bank account
def create_account(account_no):
    name=input("Enter your Full Name: ")
    while True:
        pin = int(pwinput.pwinput("Enter six digit PIN:",mask='*'))
        if pin < 100000 or pin >= 1000000:
            print("PIN number should have six digits. Try again")
            continue
        else:
            break
    while True:
        balance = float(input("Enter starting balance(Minimum amount:500): "))
        if balance >= 500:
            account=Customer(account_no, name, pin, balance)
            account_holders.append(account)
            print("Account created successfully")
            print("Name: ", account.name, "\nAccount Number: ", account.acct_no, "\nBalance amount:",account.balance)
            break
        else:
            print("Starting balance should be Rs.500 or above. Please try again:")
            continue

# ----------------------------------------End of create_account function------------------------------------------------


# function to allow user to login and perform transactions
def login(user_acct):
    print("Welcome, ", user_acct.name)
    while True:
        print("1.Deposit\n2.Withdrawal\n3.View Balance\n4.View Transactions\n5.Close account\n6.Log out")
        c = input("Enter Choice (1-6): ")
        if c == '1':
            amt = float(input("Enter amount:"))
            user_acct.deposit(amt)
        elif c == '2':
            amt = float(input("Enter amount:"))
            user_acct.withdraw(amt)
        elif c == '3':
            user_acct.display_balance()
        elif c == '4':
            user_acct.view_transactions()
        elif c == '5':
            confirm = input("do you wish to close the account(Y/N): ")
            if confirm.upper() == 'Y':
                user_acct.close_account()
                account_holders.remove(user_acct)
                break
            elif confirm.upper() == 'N':
                continue
        elif c == '6':
            print("You have successfully logged out.")
            break
        else:
            print("Invalid Input. Please enter a choice from 1-6")
            continue


# --------------------------------------------End of login function-----------------------------------------------------
print("********************************ABC Bank*****************************************\n")
count=10000000000
while True:
    print("1.Create Account\n2.Login\n3.Exit")
    option = input("Enter Choice (1-3): ")
    if option=='1':
        count+=1
        account_no=count
        create_account(account_no)
    elif option=='2':
        acct_no = int(input("Enter account number:"))
        pin = int(pwinput.pwinput("Enter six digit PIN:", mask='*'))
        for account in account_holders:
            if account.acct_no == acct_no and account.pin == pin:
                login(account)
                break
        else:
            print("Invalid Credentials.")
    elif option=='3':
        print("*****THANK YOU********")
        break
    else:
        print("Invalid Input. Try again")
        continue








