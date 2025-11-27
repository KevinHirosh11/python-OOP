from account import SavingAccount, CurrentAccount

def main():
    print("\n\t\t\t=== Welcome BOC Bank. ===")
    print("1) Savings Account.")
    print("2) Current Account.")
    print("3) Exit")
    choice = input("Enter your choice number: ")

    if choice == '1':
        saving_account = SavingAccount()
        saving_account.withdraw()
        saving_account.showDetails()

    elif choice == '2':
        current_account = CurrentAccount()
        current_account.withdraw()
        current_account.showDetails()

    elif choice == '3':
        print("Thank you for using BOC Bank. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()