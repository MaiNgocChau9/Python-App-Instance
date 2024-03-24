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
def update_student():
    update = input("Enter the name of the student you want to update: ")
    for student in student_list:
        if student.name == update:
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_grade = int(input("Enter new grade: "))
            student.name = new_name
            student.age = new_age
            student.grade = new_grade
            print("Updated successfully")
            break
        else:
            print("Not found")
            break