import csv
def removeStudent():
    term = input("Enter roll number of the student to remove: ")
    found = False
    students = []
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        # Read all records and filter out the one to be removed
        for row in reader:
            if row['roll'] != term:
                students.append(row)
            else:
                found = True
    if not found:
        print(f"No student record with the roll of {term} was found!")
    # If found, rewrite the file without the removed student
    confirm = input(f"Are you sure you want to delete the student with roll {term}?(y/n): ")
    if confirm == 'y':
        with open('students.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Student with roll {term} removed successfully!")
    else:
        print("Operation terminated!")