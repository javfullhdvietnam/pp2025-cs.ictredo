class Student_USTH:
    def __init__(self, studentid, studentname, DOB):
        self.__studentid = studentid
        self.__studentname = studentname
        self.__DOB = DOB
        self.__marks = {}  

    def get_studentid(self):
        return self.__studentid

    def get_studentname(self):
        return self.__studentname

    def get_DOB(self):
        return self.__DOB

    def get_mark(self, course_id):
        return self.__marks.get(course_id, None)

    def set_studentmark(self, course_id, mark):
        self.__marks[course_id] = mark

    def __str__(self):
        return "ID: {}, Name: {}, DOB: {}, Marks: {}".format(
            self.__studentid, self.__studentname, self.__DOB, self.__marks
        )


class Course_USTH:
    def __init__(self, courseid, coursename):
        self.courseid = courseid
        self.coursename = coursename

    def get_courseid(self):
        return self.courseid

    def get_coursename(self):
        return self.coursename

    def set_courseid(self, courseid):
        self.courseid = courseid

    def set_coursename(self, coursename):
        self.coursename = coursename

    def __str__(self):
        return "CourseID: {}, CourseName: {}".format(self.courseid, self.coursename)


class UsthSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_student(self):
        num_students = int(input("Input number of students: "))
        for _ in range(num_students):
            studentid = input("Input ID of student: ")
            studentname = input("Input name of student: ")
            DOB = input("Input DOB of student: ")
            self.students.append(Student_USTH(studentid, studentname, DOB))

    def input_courses(self):
        num_courses = int(input("Input number of courses: "))
        for _ in range(num_courses):
            courseid = input("Input course ID: ")
            coursename = input("Input course name: ")
            self.courses.append(Course_USTH(courseid, coursename))

    def list_students(self):
        print("\nStudents:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nCourses:")
        for course in self.courses:
            print(course)

    def input_mark(self):
        self.list_courses()
        courseid = input("Selecting course ID: ")
        for student in self.students:
            mark = float(
                input("Input mark for {} (ID: {}): ".format(student.get_studentname(), student.get_studentid()))
            )
            student.set_studentmark(courseid, mark)

    def show_student_mark(self):
        studentid = input("Select student ID to see marks: ")
        
        student = None
        for s in self.students:
            if s.get_studentid() == studentid:
                student = s  
                break  


        if student:
            courseid = input("Input course ID to see mark: ")
            mark = student.get_mark(courseid)
            if mark is not None:
                print("Mark of {} in course {} is {}".format(student.get_studentname(), courseid, mark))
            else:
                print("Mark not found for the course.")
        else:
            print("Student not found.")

    def main(self):
        self.input_courses()
        self.input_student()
        self.list_courses()
        self.list_students()
        self.input_mark()
        self.show_student_mark()


if __name__ == "__main__":
    system = UsthSystem()
    system.main()
