def main():
    while True:

        print("\n\t\t\t=== Welcome BOC Bank. ===")
        print("1) Savings Account.")
        print("2) Current Account.")
        print("3) Exit")
        choice = input("Enter your choice number: ")
        
        if choice == '1':
            acc = int(input("\nEnter number:"))
            if len(str(acc))>8 or len(str(acc))<8:
                name = input("Enter your name: ")
                balance = int(input("Enter your Account Balance: "))
                print(f"\nAccount Number: {acc}")
                print(f"Your Name: {name}")
                print(f"Balance: {balance}")

                withdrow = int(input("Enter your withdrow amount: "))
                total_balance = balance - withdrow
                if total_balance <500:
                    print("Insufficient Amount.")
                else:
                    print(f"Your Total balance: {total_balance}")

            else:
                print("Invalid Password. Try again..")
            break

        elif choice == '2':
            acc = int(input("\nEnter number:"))
            if len(str(acc))>8 or len(str(acc))<8:
                name = input("Enter your name: ")
                balance = int(input("Enter your Account Balance: "))
                print(f"\nAccount Number: {acc}")
                print(f"Your Name: {name}")
                print(f"Balance: {balance}")

                withdrow = int(input("Enter your withdrow amount: "))
                total_balance = balance - withdrow
                print(f"Your Total balance: {total_balance}")
            else:
                print("Invalid Password. Try again..")
            break

        elif choice == '3':
            print("Exit BOC System.")
            break
        else:
            print("Invalid Number. Try again.")


if __name__ == "__main__":
    main()
