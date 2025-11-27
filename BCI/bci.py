from re import match
from averages import Average
from student import BCIUnderGraduates
from userpass import username, password
from course import Degree, Diploma,ShortCourses
from employee import Lecture, Administrators,Marketing
from faculties import BCIFaculty
from campus import BCICampus

def main():
    username
    password
    while True:
        print("\n\t\t\t***LOGIN***\n")
        name = input("Enter UserName: ")
        pwd = input("Enter Password: ")

        if name == username and pwd == password:

            print("\n \t \t Welcome to the BCI Campus Management System...\n")
            print("1.Student Management System")
            print("2.Course Management System")
            print("3.Employee System")
            print("4.Faculty information")
            print("5.Campus Information")
            print("6.Exit")
            print("-------------------------")
            choice = input("Enter your choice: ")
            
            if choice == "1":

                stu1 = BCIUnderGraduates("BSSE241021", "Clare", "SE", "06-18-2004", "No:15,Sriwikkramarajasingha", "2.4", "Fail")
                stu1.ShowStudent()
                stu2 = BCIUnderGraduates("BSIT241021", "Kevin", "IT", "08-11-2004", "No:90,Angampitiya","3.0", "Pass")
                stu2.ShowStudent()
                stu3 = BCIUnderGraduates("CGD250009", "Chuuty", "Graphic Design", "07-27-2004", "No:245,Senasuma", "2.6", "Pass")
                stu3.ShowStudent()
                stu4 = BCIUnderGraduates("BSIT241019", "Chethi", "IT", "06-29-2003", "No: 100, Kuliyapitiya", "2.9", "pass")
                stu4.ShowStudent()
                stu5 = BCIUnderGraduates("BSIT241002", "Sithum", "IT", "05-24-2004", "No:78, ja-Ella", "2.5", "pass")
                stu5.ShowStudent()
                
                stu = [stu1, stu2, stu3, stu4, stu5]

                Average.StudentAverage(stu)

                
            elif choice == "2":

                print("\nSchool of Computing Details:\n")
                faculty2 = BCIFaculty("School of Computing")
                faculty2.Show_Faculty()

                print("1.Degree Student Details ")
                print("2.Diploma Student Details ")
                print("3.Short Courses Student Details ")
                choose = input("Select the number in Course Program: ")

                if choose == "1":

                    print("\n\tDigree Details.\n")

                    stu1 = BCIUnderGraduates("BSSE241021", "Clare", "SE", "06-18-2004", "No:15,Sriwikkramarajasingha", "2.4", "Fail")
                    stu2 = BCIUnderGraduates("BSIT241021", "Kevin", "Data Science", "08-11-2004", "No:90,Angampitiya","3.0", "Pass")
                    stu4 = BCIUnderGraduates("BSIT241019", "Chethi", "IT", "06-29-2003", "No: 100, Kuliyapitiya", "2.9", "pass")
                    stu5 = BCIUnderGraduates("BSIT241002", "Sithum", "IT", "05-24-2004", "No:78, ja-Ella", "2.5", "pass")


                    subject1 = ["AI", "R Programming", "Python", "Big Data Analysis", "Machine Learning"]
                    marks1 = {
                        "AI" : 89,
                        "R Programming": 75,
                        "Python": 78,
                        "Big Data Analysis": 68,
                        "Machine Learning": 46
                    }
                    cou1 = Degree(stu2,"BSIT12001","DataScience", 16, subject1, 6)
                    cou1.addSubMarks(marks1)

                    subject2 = ["AI", "Java", "Python", "DataBase", "Java Script"]
                    marks2 = {
                        "AI" : 76,
                        "R Programming": 63,
                        "Python": 49,
                        "Big Data Analysis": 54,
                        "Java Script": 84
                    }
                    cou2 = Degree(stu1,"BSIT12002", "Softwar Engineering ", 20, subject2, 6)
                    cou2.addSubMarks(marks2)

                    subject3 = ["Ethical Hacking", "Cyber Attack", "Python", "Kali Hacking Tools", "System Protecting"]
                    marks3 = {
                        "Ethical Hacking": 65,
                        "Cyber Attack": 56,
                        "Python": 74,
                        "Kali Hacking Tools": 87,
                        "System Protecting": 46
                    }
                    cou3 = Degree(stu4,"BSSE13001", "Cyber Security", 15,subject3, 7)
                    cou3.addSubMarks(marks3)

                    subject4 = ["HTML", "CSS", "Java Script", "Hosting", "React"]
                    marks4 = {
                        "HTML": 68,
                        "CSS": 78,
                        "Java Script": 54,
                        "Hosting": 80,
                        "React": 56
                    }
                    cou4 = Degree(stu5,"BSSE13001", "Front-End Developer", 17,subject4, 7)
                    cou4.addSubMarks(marks4)

                    cou = [cou1, cou2, cou3, cou4]
                    for course in cou:
                        course.showCourse()
                    
                    Average.cou_ave(cou)
                    break

                elif choose == "2":

                    print("\n\tDiploma Ditails.\n")
                    
                    stu3 = BCIUnderGraduates("CGD250009", "Chuuty", "Graphic Design", "07-27-2004", "No:245,Senasuma", "2.6", "Pass")

                    subject5 = ["Photoshop", "Light Room", "Illustrate", "CorelDraw", "3D Animetion"]
                    marks5 = {
                        "Photoshop": 78,
                        "Light Room": 93,
                        "Illustrate": 67,
                        "CorelDraw": 80,
                        "3D Animetion": 57
                    }
                    dip = Diploma(stu3, "DGD12001", "Graphic Design", 2, subject5)
                    dip.addSubMarks(marks5)
                    dip.showCourse()
                    dip.couAve()
                    break
                
                elif choose == "3":

                    print("\n\tShort Courses.\n")

                    subject6 = ["Number System", "Logic gates", "Networking"]
                    sc1 = ShortCourses("SC1234", "Information Communication", 1, subject6)
                    sc1.showCourse()
                    break
                
                else:
                    print("Invalid Number. Try Again....")


            elif choice == "3":
                lec = Lecture("L123", "Dr. Smith",2000, 20)
                lec.show_employee()

            elif choice == "4":
                print("\nFaculty Details:\n")
                faculty1 = BCIFaculty("School of Business")
                faculty1.Show_Faculty()

                faculty2 = BCIFaculty("School of Computing")
                faculty2.Show_Faculty()

                faculty3 = BCIFaculty("School of Psychology")
                faculty3.Show_Faculty()
                break

            elif choice == "5":
                print("\nCampus Information:\n")
                campus = BCICampus("Aspire to Inspire", "Negombo", "031-1234567")
                campus.show_campus_info()
                break

            elif choice == "6":
                print("Exiting the BCI Management System...")
                break
            else:
                print("Invalid choice. Please try again.")
            break
        else:
            print("Invalid username and password, Try again...")

if __name__ == "__main__":
    main()
