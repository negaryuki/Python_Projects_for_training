#To-Do List: Bank Account Simulation

	#	1.	Define the BankAccount Class:
	#	•	Create a class named BankAccount.
	#	•	Define the __init__ method to initialize attributes like account_number, balance, and owner_name.
				    
				
		
	# 2.	Create Deposit and Withdraw Methods:
	# •	Define methods deposit and withdraw within the BankAccount class.
	#	•	Implement the logic to update the balance when a deposit or withdrawal is made.
	
	#	3.	Add a Method to Check Balance:
	#	•	Create a method named get_balance to retrieve the current balance.
		
		
	#	4.	Test the Class:
	#	•	Create instances of the BankAccount class.
	#	•	Use the methods to perform deposits, withdrawals, and balance checks.
	
class BankAccount:
		def __init__(self,account_no,owner,balance = 0):
			self.accountno = account_no
			self.owner = owner
			self.balance = balance
			
		def deposit (self,amount):
			self.balance += amount
			return (f'You added: {amount} $, Your current Balance : {self.balance} $')
			
		def withdraw (self,amount):
			if self.balance >= amount:
				self.balance -= amount
				return (f'You withdrew: {amount}, Your current Balance :{self.balance}')
			else:
				return ("Insufficient funds")
			  
		def get_balance(self):
			return(f' Your balance is: {self.balance} $')
			
# Create instances of BankAccount
account1 = BankAccount("12345", "Negar", 1000)
account2 = BankAccount("67890", "Angela", 500)


# Perform operations on accounts
print(account1.deposit(200))     # Output: Deposited 200. New balance: 1200
print(account1.withdraw(300))    # Output: Withdrew 300. New balance: 900
print(account1.get_balance())    # Output: Current balance: 900

print(account2.deposit(100))     # Output: Deposited 100. New balance: 600
print(account2.withdraw(800))    # Output: Insufficient funds
print(account2.get_balance())    # Output: Current balance: 600

print(account1.deposit(200))     # Suggested by a friend


