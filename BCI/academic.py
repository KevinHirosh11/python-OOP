class Academic:
    def __init__(self, courseName, courseCode, courseCredits,courseFee):
        self.CourseName = courseName
        self.CourseCode = courseCode
        self.CourseCredits = courseCredits
        self.CourseFee = courseFee

course1 = Academic("Information Technology", "IT101", "120", "Rs. 190,000")
course2 = Academic("Software Engineering", "SE102", "100", "Rs. 180,000")
course3 = Academic("Database Systems", "DB103", "80", "Rs. 170,000")

courses = [course1, course2, course3]

for course in courses:
    print("Course Name: {}\n Course Code: {}\n Course Credits: {}\n Course Fee: {} \n"
          .format(course.CourseName, course.CourseCode, course.CourseCredits, course.CourseFee))