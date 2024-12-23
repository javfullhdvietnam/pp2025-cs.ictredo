students = []
courses = []
def infor_student():
    number_student = int(input("input number students: "))
    for i in range(number_student):
        student_id = input("input student id: ")
        student_name = input("input student name: ")
        student_DOB = input("input student DOB: ")
        students.append({
            "id":student_id,
            "name": student_name,
            "student_DOB": student_DOB,
            "mark": {}
        })

def infor_courses():
    number_courses = int(input("input number courses: "))
    for i in range(number_courses):
        courses_id = input("input course id: ")
        course_name = input("input course name: ")
        courses.append({
            "id": courses_id,
            "name": course_name
        })

def input_marks():
    list_course()
    course_id = input("select id course: ")
    for student in students:
        marks  = float(input("input marks: "))
        student['mark'][course_id] = marks

def list_student():
    print("\n Student: ")
    for student in students:
        print("ID: {},Name: {},student_DOB {}".format(student['id'],student['name'],student['student_DOB']))
    
def list_course():
    print("\n Course: ")
    for course in courses:
        print('ID course: {}, Name course: {}'.format(course['id'],course['name']))

def show_student_mark():
    student_id = input("input student id to see mark: ")
    student = None

    for s in students:
        if s['id'] == student_id:
            student = s
            break
    
    if student:
        course_id = input("input course ID mark: ")
        mark = student['mark'].get(course_id,None)
        if mark is not None:
            print("mark of {}in {} is {}".format(student['name'],course_id,mark))
        else:
            print("mark not found")
    else:
        print("student not found")

def main():
    infor_courses()
    infor_student()
    input_marks()
    list_student()
    list_course()
    show_student_mark()

if __name__ == "__main__":
    main()