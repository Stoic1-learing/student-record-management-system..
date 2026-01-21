students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")

    student = {
        "id": student_id,
        "name": name,
        "department": department
    }

    students.append(student)
    print("Student added successfully.\n")

def view_students():
    if len(students) == 0:
        print("No student records available.\n")
    else:
        for student in students:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("-----------------------")

def search_student():
    search_id = input("Enter Student ID to search: ")
    for student in students:
        if student["id"] == search_id:
            print("Student Found")
            print("Name:", student["name"])
            print("Department:", student["department"])
            return
    print("Student not found.\n")

def main_menu():
    while True:
        print("STUDENT RECORD MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.\n")

main_menu()
