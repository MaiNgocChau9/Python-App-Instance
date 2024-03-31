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
    for student in student_list:
        if student.name == name:
            student_list.remove(student)
            print("Deleted successfully")
            break
        else:
            print("Not found")
            break

# Display students in student_list
def display_student():
    for student in student_list:
        print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

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

# Main program
while True:
    print("=== MENU ===")
    print("1. Add student")
    print("2. Remove student")
    print("3. Display student")
    print("4. Update student")
    print("5. Exit")
    print("\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = int(input("Enter grade: "))
        add_student(name, age, grade)
    elif choice == 2:
        name = input("Enter name: ")
        remove_student(name)
    elif choice == 3:
        display_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        break