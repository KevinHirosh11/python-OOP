from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = float(emp_salary)

    @abstractmethod
    def show_employee(self):
        pass

class SalaryEmployee(Employee):

    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = float(emp_salary)

    def show_employee(self):
        print(f"Id: {self.emp_id} \tName: {self.emp_name} \tSalary: {self.emp_salary}")

class Lecture(SalaryEmployee):

    def __init__(self, emp_id, emp_name, emp_salary,hours):
        super().__init__(emp_id, emp_name, emp_salary)
        self.Hours = hours

    def cal_H_Salary(self):
        self.total_cal = self.Hours * self.emp_salary
    
    def show_employee(self):
        super().show_employee()
        print(f"Lecture Total Hourly Salary: {self.total_cal}")

class Administrators(SalaryEmployee):
    def __init__(self, emp_id, emp_name, emp_salary):
        super().__init__(emp_id, emp_name, emp_salary)
        self.Commission = float(input("Enter Commission Amount: "))

    def cal_commission(self):
        return self.Commission + self.emp_salary

    def show_employee(self):
        super().show_employee()
        print(f"Total Salary: {self.cal_commission()}")

class CommissionBasedEmployee(Employee):

    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = float(emp_salary)

    def show_employee(self):
        print(f"Id: {self.emp_id} \tName: {self.emp_name} \tSalary: {self.emp_salary}")

class Marketing(CommissionBasedEmployee):

    def __init__(self, emp_id, emp_name, emp_salary):
        super().__init__(emp_id, emp_name, emp_salary)
        self.NumAdvetisment = int(input("Enter Number of Advertisment: "))
        self.Commission = float(input("Enter Commission Amount: "))

    def cal_amount(self):
        self.total = self.NumAdvetisment * self.Commission
        self.Total_amount = self.total * self.emp_salary
    
    def show_employee(self):
        super().show_employee()
        print(f"Number of Advertisment: {self.NumAdvetisment}\nCommission Amount: {self.Commission}\t\tTotal of Employee Salary: {self.Total_amount}")
    
