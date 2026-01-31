import csv
def addStudent():
    while True:
        name = input("Enter Student Name: ").strip()
        if name.replace(" ", "").isalpha() and len(name) >= 4:
            break
        else:
            print("Name must contain minimum of 4 letters. Please try again.")
    while True:
        roll = input("Enter Roll Number: ").strip()
        if roll.isdigit() and len(roll) > 0:
            with open('students.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['roll'] == roll:
                        print(f"A student with roll number {roll} already exists. Please enter a unique roll number.")
                        roll = None
                        break
                if roll is not None:
                    break
        else:
            print("Roll can't be empty and must be a number. Please enter a valid roll number.")
        
    while True:
        email = input("Enter E-mail: ").strip()
        if len(email) > 0:
            break
        else:
            print("Empty input is not allowed. Please enter an valid email address.")
    while True:
        dept = input("Enter Department: ").strip()
        if len(dept) > 0:
            break
        else:
            print("Empty input is not allowed. Please enter a valid department name.")
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