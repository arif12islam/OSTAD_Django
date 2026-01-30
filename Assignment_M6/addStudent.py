import csv
def addStudent():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    email = input("Enter E-mail: ")
    dept = input("Enter Department: ")
    # Append the new student record to 'students.csv'
    with open('students.csv', 'a', newline='') as file:
        fieldnames = ['name', 'roll', 'email', 'dept']
        csv_writer = csv.DictWriter(file, fieldnames = fieldnames)
        if file.tell() == 0:
            csv_writer.writeheader()
        
        csv_writer.writerow({
            'name': name,
            'roll': roll,
            'email': email,
            'dept': dept
        })
    print("Student record added successfully!")