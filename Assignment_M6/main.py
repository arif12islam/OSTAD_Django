import addStudent as AS
import viewStudents as VS
import searchStudent as SS
import removeStudent as RS
import csv

def show_menu():
    print("Welcome to Student Management System")
    # Check if 'students.csv' exists, if not create it
    try:
        with open('students.csv', 'r') as file:
            print(f"Student records loaded from {file.name} successfully!")
    except FileNotFoundError:
        with open('students.csv', 'w', newline='') as new_file:
            fieldnames = ['name', 'roll', 'email', 'dept']
            csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
            csv_writer.writeheader()
            print(f"No file was found. A new {new_file.name} has been created.")

    print("=========== MENU ===========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
while True:
    show_menu()
    choice = input("Choose an option(1-5): ")
    if choice == '1':
        AS.addStudent()
    elif choice == '2':
        VS.viewStudents()
    elif choice == '3':
        SS.searchStudent()
    elif choice == '4':
        RS.removeStudent()
    elif choice == '5':
        break
    else:
        print("Invalid input!")

    
    