#list
student = []
course = []
mark = []

#input function
def studentInp():
    studentNum = input("Numbers of student: ")
    for i in range(int(studentNum)):    
        Name = input("Student Name:")
        ID = input("Student ID: ")
        DateOfBirth = input("Student's DOB:")
        student.append({'student Name':Name, 'studentID':ID, 'student DOB': DateOfBirth}) 
    print(student)
        
def courseInp():
    courseNum = input("Number of courses: ")
    for j in range(int(courseNum)):
        Name = input("Course name:")
        courseID = input("ID: ")
        course.append({'course name':Name, 'ID':courseID}) 
    print(course)
    
    
def markInp():
        studentID = input("Student ID: ")
        courseName = input ("Course: ")
        Mark = input("Mark: ")
        mark.append({'ID':studentID, 'Course':courseName, 'Mark':Mark})
        print(mark)
    

#main 
studentInp()
courseInp()
markInp()

        