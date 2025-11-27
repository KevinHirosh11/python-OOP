class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def showDetails(self):
        print(f"Student ID: {self.student_id}, Name: {self.name}")

class UndergraduateStudent(Student):
    def __init__(self, student_id, name, year):
        super().__init__(student_id, name)
        self.year = year

    def showDetails(self):
        print(f"Undergraduate ID: {self.student_id}, Name: {self.name}, Year: {self.year}")

class PostgraduateStudent(Student):
    def __init__(self, student_id, name, research_topic):
        super().__init__(student_id, name)
        self.research_topic = research_topic

    def showDetails(self):
        print(f"Postgraduate ID: {self.student_id}, Name: {self.name}, Research Topic: {self.research_topic}")


if __name__ == "__main__":
    students = [
        UndergraduateStudent("U001", "Kasun", "Year 2"),
        PostgraduateStudent("P001", "Nadeesha", "AI in Education"),
        UndergraduateStudent("U002", "Sahan", "Year 3"),
        PostgraduateStudent("P002", "Ishara", "Quantum Computing")
    ]

    print("=== Student Details ===")
    for student in students:
        student.showDetails()  # Polymorphic call