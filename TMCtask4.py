student_grades = {}
def add_student(name, grade):
    if name in student_grades:
        print(f"{name} already exists.")
    else:
        student_grades[name] = grade
        print(f"Added {name} with grade {grade}.")
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} is not found.")
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted.")
    else:
        print(f"{name} is not found.")
def display_all_student():
    if student_grades:
        print("\n----- Student List -----")
        for name, grade in student_grades.items():
            print(f"Name: {name:<15} Grade: {grade}")
    else:
        print("No students found.")
def main():
    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter new grade: "))
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            display_all_student()
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1-5.")
main()