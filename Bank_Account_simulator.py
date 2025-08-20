#Bank Account

class Bank_Account:
    def __init__(self,account_holder, inital_balance =0):
        self.account_holder = account_holder
        self.balance = inital_balance
        
    # Deposit Money
    def deposit(self , amount):
        if amount >0:
            self.balance += amount
            print(f" Depsoited ${amount}.New balance: ${self.balance}")
            
        else:
            print("Invalid amount")
            
    
    #Withdraw Money
    
    def withdraw(self , amount):
        if amount> 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount or insufficient balance")
            
            
    #Show Details:
    
    def show_details(self):
        print("\n---Account Details ---")
        print(f"Accountholder: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        
        
#Main program

accounts = {}

def create_account():
    name = input("Enter the holder name. ").strip()
    initial_balance = float(input("Enter the initial balance: $").strip())
    accounts[name] = Bank_Account(name, initial_balance)
    print(f"Account created for {name} with initial balance ${initial_balance}")

def access_account():
    name = input("Enter your name: ").strip()
    if name in accounts:
        print(f"Welcome {name}")
        accounts[name].show_details()
        while True:
            print("\n---Account Menu---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                amount = float(input("Enter the amount to deposit: $").strip())
                accounts[name].deposit(amount)
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: $").strip())
                accounts[name].withdraw(amount)
            elif choice == "3":
                accounts[name].show_details()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Account Not found . Please create an account first.")
        


#Main Menu

while True:
    print("\n---Bank Account Simulator---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    choice = input("Enter your choice(1-3): ").strip()
    if choice == "1":
        create_account()
    elif choice == "2":
        access_account()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
        
    
    