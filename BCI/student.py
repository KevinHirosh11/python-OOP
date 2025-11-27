from abc import ABC,abstractmethod

class Student(ABC):
    
    TotalStudnet = 0

    def __init__(self, stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult):
        self.StudentID = stuID
        self.StudentName = stuName
        self.StudentCourse = stuCourse
        self.StudentDOB = stuDOB
        self.StudentAddress = stuAddress
        self.StudentGPA = stuGPA
        self.StudentFinalResult = stuResult
        Student.TotalStudnet += 1

    @abstractmethod
    def showAverage(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def updateStudentFinalResult(self, newFinalResult):
        pass
        
    @abstractmethod    
    def ShowStudent(self):
        pass

class BCIstudent(Student):
    
    TotalStudnet = 0

    def __init__(self, stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult):
        self.StudentID = stuID
        self.StudentName = stuName
        self.StudentCourse = stuCourse
        self.StudentDOB = stuDOB
        self.StudentAddress = stuAddress
        self.StudentGPA = stuGPA
        self.StudentFinalResult = stuResult
        Student.TotalStudnet += 1
    
    def showAverage(self):
        return self.StudentGPA
    
    def __str__(self):
         return f"{self.StudentName}"
    
    def updateStudentFinalResult(self, newFinalResult):
        self.StudentFinalResult = newFinalResult

    def ShowStudent(self):
        print(f"Student ID: {self.StudentID}\n Student Name: {self.StudentName}\n Student Course: {self.StudentCourse}\n Student DOB: {self.StudentDOB}\n Student Address: {self.StudentAddress} \n Student GPA: {self.StudentGPA} \n Student Result {self.StudentFinalResult} \n")

class BCIUnderGraduates(BCIstudent):

    def __init__(self, stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult):
        super().__init__(stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult)

    def ShowStudent(self):
        super().ShowStudent()
        print(f"Student ID: {self.StudentID}\n Student Name: {self.StudentName}\n Student Course: {self.StudentCourse}\n Student DOB: {self.StudentDOB}\n Student Address: {self.StudentAddress} \n Student GPA: {self.StudentGPA} \n Student Result {self.StudentFinalResult} \n")


class BCIPostGraduates(BCIstudent):

    def __init__(self, stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult):
        super().__init__(stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult)


    def ShowStudent(self):
        super().ShowStudent()
        print(f"Student ID: {self.StudentID}\n Student Name: {self.StudentName}\n Student Course: {self.StudentCourse}\n Student DOB: {self.StudentDOB}\n Student Address: {self.StudentAddress} \n Student GPA: {self.StudentGPA} \n Student Result {self.StudentFinalResult} \n")


if __name__ == "__main__":
    students = [
        BCIUnderGraduates("BSSE241021", "Clare", "SE", "06-18-2004", "No:15,Sriwikkramarajasingha", "2.4", "Fail"),
        BCIUnderGraduates("BSIT241021", "Kevin", "Data Science", "08-11-2004", "No:90,Angampitiya","3.0", "Pass"),
        BCIUnderGraduates("BSIT241019", "Chethi", "IT", "06-29-2003", "No: 100, Kuliyapitiya", "2.9", "pass"),
        BCIUnderGraduates("BSIT241002", "Sithum", "IT", "05-24-2004", "No:78, ja-Ella", "2.5", "pass")

    ]
    print("=== Student Details ===")
    for student in students:
        student.ShowStudent()



