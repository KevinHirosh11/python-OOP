
def main():
    while True:
        print("\n \t \t Welcome to the BCI Campus Management System...\n")
        print("1.Student Management System")
        print("2.Academic Management System")
        print("3.Non-Academic Management System")
        print("4.Building Management System")
        print("5.Exit")
        print("-------------------------")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            from student import Student
            
        elif choice == "2":
            from academic import Academic

        elif choice == "3":
            from nonacademic import NonAcademic
            
        elif choice == "4":
            from building import Building

        elif choice == "5":
            print("Exiting the BCI Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()