class student_USTH():
    def __init__(self,id,name,DOB):
        self.id = id
        self.name = name
        self.DOB = DOB
        self.marks = {}

class course_USTH():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    



n1 = int(input("number of student: "))
list_student = []
for i in range(1,n1 + 1):
    print("input student {}".format(i))
    id = input("input id student: ")
    name = input("name student: ")
    DOB = input("input DOB of student: ")
    students = student_USTH(id,name,DOB)
    list_student.append(students)


n2 = int(input("number of course: "))
list_course = []

for i in range(1,n2+1):
    print("input cousse {}".format(i))
    id = input("input id course: ")
    name = input("input name of couse: ")
    courses = course_USTH(id,name)
    list_course.append(courses)

print("{:<15}{:<15}{:<15}".format("id","name","DOB"))
for student in list_student:
    print("{:<15}{:<15}{:<15}".format(student.id,student.name,student.DOB))


print("\n{:<15}{:<15}".format("id","name"))
for course in  list_course:
    print("{:<15}{:<15}".format(course.id,course.name))

course_id = input("\nEnter the course ID to input marks: ")
selected_course = next((course for course in list_course if course.id == course_id), None)
if selected_course:
    print(f"\nInput marks for course: {selected_course.name}")
    for student in list_student:
        mark = float(input(f"Enter mark for student {student.name} ({student.id}): "))
        student.marks[selected_course.id] = mark
else:
    print("Course not found!")

course_id = input("\nEnter the course ID to view marks: ")
selected_course = next((course for course in list_course if course.id == course_id), None)
if selected_course:
    print(f"\nMarks for course: {selected_course.name}")
    print("{:<15}{:<15}{:<15}".format("Student ID", "Name", "Mark"))
    for student in list_student:
        if course_id in student.marks:
            print("{:<15}{:<15}{:<15}".format(student.id, student.name, student.marks[course_id]))
        else:
            print("{:<15}{:<15}{:<15}".format(student.id, student.name, "No mark"))
else:
    print("Course not found!")