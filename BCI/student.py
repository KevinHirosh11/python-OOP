
class Student:

    def __init__(self):
        self.Write = open("Student.txt","w")
        self.n = int(input("How many entering details: "))
        for i in range(self.n):
            self.StudentFName = input("Enter Student First Name: ")
            self.StudentLName = input("Enter Student Last Name: ")
            self.StudentID = input("Enter Student ID: ")
            self.StudentAge = input("Enter Student Age: ")
            self.StudentGender = input("Enter Student Gender: ")
            self.StudentCourse = input("Enter Student Course: ")
            self.Write.write(
                f"{self.StudentFName} {self.StudentLName}\n{self.StudentID}\n{self.StudentAge}\n{self.StudentGender}\n{self.StudentCourse}\n"
)
student = Student()
student = {
    "Roll No": student.StudentID,
    "First Name": student.StudentFName,
    "Last Name": student.StudentLName,
    "Age": student.StudentAge,
    "Gender": student.StudentGender,
    "ID": student.StudentID,
    "Course": student.StudentCourse
}


print("\n Student Add Successfully!")
print("-------------------------\n")



