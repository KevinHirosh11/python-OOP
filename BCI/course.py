from abc import ABC, abstractmethod
class Course(ABC):
        
    def __init__(self, couID, couName, couCredit,subject):
        self.__CourseID = couID
        self.CourseName = couName
        self.CourseCredit = int(couCredit)
        self.Sub = subject
        self.SubMarks = {}

    def get_course_name(self):
        return self.CourseName
    
    @abstractmethod
    def showCourse(self):
        print(f"Course ID: {self.__CourseID} \nCourse Name: {self.CourseName} \nTotal Course Credit: {self.CourseCredit}\nSubject: {self.Sub}")
        if self.SubMarks:
            print("Subject Marks:")
            for sub, mark in self.SubMarks.items():
                print(f"  - {sub}: {mark}")

class Degree(Course):

    def __init__(self, StuNameObj, couID, couName, couCredit, subject,couMonths):
        super().__init__(couID, couName, couCredit,subject)
        self.StudentName = StuNameObj
        self.CourseMonths = float(couMonths)

    def addSubMarks(self, marks):
        self.SubMarks =  marks


    def showCourse(self):
        super().showCourse()
        print(f"Student Name: {self.StudentName} \nCourse Months: {self.CourseMonths}")
        avg = sum(self.SubMarks.values()) / len(self.SubMarks)
        print(f"Average Marks: {round(avg, 1)}")
        gpa = avg/self.CourseCredit
        print(f"GPA: {gpa}\n")


class Diploma(Course):

    def __init__(self, StuNameObj, couID, couName, couCredit, subject):
        super().__init__(couID, couName, couCredit, subject)
        self.StudentName = StuNameObj

    def addSubMarks(self, marks):
        self.SubMarks =  marks

    def showCourse(self):
        super().showCourse()
        print(f"Student Name: {self.StudentName}")
        
    def couAve(self):
        total = sum(self.SubMarks.values())
        average = total / len(self.SubMarks)
        print(f"Average Subject Marks: {average} \n")
        return average

class ShortCourses(Course):

    def __init__(self, couID, couName, couCredit,subject):
        super().__init__(couID, couName, couCredit, subject)

    def showCourse(self):
        super().showCourse()

