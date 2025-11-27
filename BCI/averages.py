

class Average:

    def StudentAverage(stu):
        
        total_gpa = 0.0
        count = 0
        for student in stu:
            total_gpa += float(student.showAverage())
            count += 1
        if count > 0:
            average = total_gpa / count
        print("Average: {}".format(average))


    def cou_ave(degree):
        print("\n Course Average Summary...\n")
        for course in degree:
            avg = sum(course.SubMarks.values()) / len(course.SubMarks)
            print(f"- {course.CourseName}: {round(avg, 1)}")




#def create_courses():
    #return[
        #Course("BSSE1237", "Database", "3", 45),
        #Course("BSIT1254", "Python", "4", 34),
        #Course("BSIT1345", "HTML", "4",42),
        #Course("BSSE1345", "C++", "4",35),
        #Course("BSSE1340", "Epic", "2",53)
    #]
    
#def create_student(courses):
 #   students = []

  #  for i in range(1,6):
   #     s = Student()
    #    course = random.choice(courses).get_course_name()
     #   course_hours = random.choice(courses).get_course_hours()
      #  final_rusult = random.randint(50,100)
       # s.setStudent(f"S{1:03}", f"Student{i}", course, f"200{i}-01-01", final_rusult, course_hours)
        #students.append(s)

    #return students
    
#def calculate_avg(students):
 #   total = sum(s.get_final_result() for s in students)
  #  return total / len(students)
        

#if __name__ == "__main__":
 #   courses = create_courses()
  #  students = create_student(courses)

   # print("Allocated Students amd Courses:\n")
    #for s in students:
     #   s.showStudent()

    #avg_result = calculate_avg(students)
    #print(f"\nAverage Final Result of Students: {avg_result:.2f}")
            


