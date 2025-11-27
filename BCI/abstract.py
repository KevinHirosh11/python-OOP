from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = float(emp_salary)

    @abstractmethod
    def show_employee(self):
        pass

class BCIAcademicEmployee(Employee):
    def __init__(self, emp_id, emp_name, emp_salary, subject):
        super().__init__(emp_id, emp_name, emp_salary)
        self.subject = subject

    def show_employee(self):
        print(f"Academic Employee => Id: {self.emp_id} \tName: {self.emp_name} \tSalary: {self.emp_salary} \tSubject: {self.subject}")

class BCINonAcademicEmployee(Employee):
    def __init__(self, emp_id, emp_name, emp_salary, commission):
        super().__init__(emp_id, emp_name, emp_salary)
        self.commission = float(commission)

    def Cal_Salary(self):
        return self.emp_salary + self.commission
    
    def show_employee(self):
        print(f"Non-Academic Employee => Id: {self.emp_id} \tName: {self.emp_name} \tSalary: {self.emp_salary} \tCommission: {self.commission}, Total Salary: {self.Cal_Salary()}")

if __name__ == "__main__":
    employee = [
        BCIAcademicEmployee("BCI003", "Duthika", 2500000.00, "IT"),
        BCINonAcademicEmployee("BCI004", "Wasantha", 50000.00, 8000)
    ]

    print("=== Employee Details ===")
    for emp in employee:
        emp.show_employee()
