studentList =[] 
courseList = []
markList = []



class Student:
    def __init__(self, studentID, studentName, studentDOB):
        self.__studentName = studentName
        self.__studentID = studentID
        self.__studentDOB = studentDOB
   
   def get_studentName(self):
        return self.__studentName
   def get_studentID(self):
        return self.__studentID
   def get_studentDOB(self):
        return self.__studentDOB

class Course:
    def __init__(self, courseID, courseName):
        self.__courseName = courseName
        self.__courseID = courseID
        courseList.append(self)
   
    def get_courseName(self):
        return self.__courseName
    
    def get_courseID(self):
        return self.__courseID


class Mark:
    def __init__(self, studentID, courseID, mark):
        self.__studentID = studentID
        self.__courseID = courseID
        self.__mark = mark
        markList.append(self)

    def get_studentID(self):
        return self.__studentID

    def get_courseID(self):
        return self.__courseID

    def get_mark(self):
        return self.__mark



def studentInput():
    studentNum = input("Enter numbers of student: ")
    for i in range(int(studentNum)):    
        studentName = input("Enter Student Name:")
        studentID = input("Enter Student ID: ")
        studentDOB = input("Student's DOB:")
        studentList.append({'student Name':studentName, 'studentID':studentID, 'student DOB': studentDOB}) 
    print(studentList)


def courseInput():
    courseNum = input("Enter number of courses: ")
    for j in range(int(courseNum)):
        courseName = input("Enter course name:")
        courseInfo = input("ID: ")
        courseList.append({'course name':courseName, 'ID':courseInfo}) 
    print(courseList)
 
def markInput():
        inputID = input("enter Student ID: ")
        inputCourse = input ("Course: ")
        inputMark = input("Mark: ")
        markList.append({'ID':inputID, 'Course':inputCourse, 'Mark':inputMark})
        print(markList)
    


selection()
