
import math


students = []
studentsDict = []
gpas = []

def findGPA(studentObj):
    GPA = 0
    all_grade_points = 0
    all_credits = 0

    for course in studentObj.courses:
        grade_point = course.credit * course.mark
        all_grade_points += grade_point
        all_credits += course.credit
    GPA = all_grade_points/all_credits
    studentObj.gpa = GPA
    return GPA


class Student():
    def __init__(self, Id, name, dob):
        self.name = name
        self.id = Id
        self.dob = dob
        self.courses = []
        self.gpa = None


class Course():
    def __init__(self, Id, name, credit, mark):
        self.name = name
        self.id = Id
        self.mark = math.floor(float(mark))
        self.credit = credit



class Input:

    # input user selection
    def selection(self):
        while True:
            firstSl = print("1.Student Info")
            secondSl = print("2.Course Info")
            # thirdSl = print("3.Mark Info")
            fourthSl = print("4.Exit")

            mySl = input("My Choice: ")

            if mySl == "1":
                return self.studentInput()
            elif mySl == "2":
                return self.courseInput()
            # elif mySl == "3":
            #     return self.markInput()
            elif mySl == "4":
                break


    def studentInput(self):
        studentNum = input("Enter numbers of student: ")
        for i in range(int(studentNum)):
            studentName = input("Enter Student Name:")
            studentID = input("Enter Student ID: ")
            studentDOB = input("Student's DOB:")
            students.append(
                {'student Name': studentName, 'studentID': studentID, 'student DOB': studentDOB})
        print(students)

  

    def courseInput(self):
        courseNum = input("Enter number of courses: ")
        for j in range(int(courseNum)):
            courseName = input("Enter course name:")
            courseInfo = input("ID: ")
            courses.append({'course name': courseName, 'ID': courseInfo})
        print(courses)

    # input grade


my_input = Input()
my_input.selection()


stu1 = Student(1, "longle", 1)
crs1 = Course("c1", "python", 5, 15)
crs2 = Course("c2", "s&s",6, 17)
crs3 = Course("c3", "DSA",8, 30)

stu1.courses.append(crs1)
stu1.courses.append(crs2)
stu1.courses.append(crs3)


stu2 = Student(8, "dhkien",4)
crs4 = Course("c1", "python", 6, 8
crs5 = Course("c2", "s&s",4,8)
crs6 = Course("c3", "DSA", 9.12)
              
for student in students:
    findGPA(student)
for student in students:
    studentsDict.append(vars(student))

newnewStudents = sorted(studentsDict, key=lambda k: k['gpa'], reverse=False)

print(newnewStudents)
