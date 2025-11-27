from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self):
        self.account_number = int(input("Enter your Account Number: "))
        self.name = input("Enter your Name: ")
        self.balance = float(input("Enter your Initial Balance: "))

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def showDetails(self):
        pass

class BOCAccount(Account):
    def __init__(self):
        self.account_number = int(input("\nEnter your Account Number: "))
        if len(str(self.account_number))>8 or len(str(self.account_number))<8:
            self.name = input("Enter your Name: ")
            self.balance = float(input("Enter your Initial Balance: "))
        else:
            print("Invaild Password. Try again...")

    def withdraw(self):
        pass

    def showDetails(self):
        print(f"\nAccount Number: {self.account_number}\nAccount Holder Name: {self.name}\nAccount Balance: {self.balance}\n")

class SavingAccount(BOCAccount):
    def __init__(self):
        super().__init__()
        self.withdraw_amount = float(input("\nEnter the withdrawal amount: "))

    def withdraw(self):
        total_balance = self.balance - self.withdraw_amount
        if total_balance < 500:
            print("Insufficient Balance. Minimum balance of 500 must be maintained. Try again.")
            self.total_balance = self.balance
            return
        else:
            self.total_balance = total_balance

    def showDetails(self):
        print("\n--- Savings Account Details ---")
        super().showDetails()
        print(f"Withdrawal Amount: {self.withdraw_amount}\nTotal Balance after Withdrawal: {self.total_balance}\n")

class CurrentAccount(BOCAccount):
    def __init__(self):
        super().__init__()
        self.withdraw_amount = float(input("\nEnter the withdrawal amount: "))

    def withdraw(self):
        self.total_balance = self.balance - self.withdraw_amount

    def showDetails(self):
        print("\n--- Current Account Details ---")
        super().showDetails()
        print(f"Withdrawal Amount: {self.withdraw_amount}\nTotal Balance after Withdrawal: {self.total_balance}\n")
