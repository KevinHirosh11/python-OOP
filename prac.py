class Student:

    def __init__(self,studentFName,studentLName,studentAge,studentGender,studentID):
        self.StudentFName = studentFName
        self.StudentLName = studentLName
        self.StudentAge = studentAge
        self.StudentGender = studentGender
        self.StudentID = studentID
    
student1 = Student("Clare","Victoria", "21", "Female ", "BSSE2410")
student2 = Student("Anu", "Minipura", "22", "Female", "BSIT241015")
student3 = Student("Sithu", "Anupama", "22", "Female", "BSIT241018")

students = (student1,student2,student3)
for student in students:
    print("Student FName: {}\n Student LName: {}\n Student Age: {}\n Student Gender: {}\n Student ID: {} \n"
          .format(student.StudentFName, student.StudentLName, student.StudentAge, student.StudentGender, student.StudentID))

