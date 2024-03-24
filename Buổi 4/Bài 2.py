class Student:
    def __init__(self, name, age, grade):
        
        self.name = name
        self.age = age
        self.grade = grade
        
student_list = []

# Add students to student_list
def add_student(name, age, grade):
    student_list.append(Student(name, age, grade))

# Remove students from student_list
def remove_student(name):
    delete_student = input("Enter the name of the student you want to delete: ")
    for student in student_list:
        if student.name == delete_student:
            student_list.remove(student)
            print("Deleted successfully")
            break
        else:
            print("Not found")
            break

# Display students in student_list
def display_student():
    for student in student_list:
        print(student.name, student.age, student.grade)

# Update students in student_list