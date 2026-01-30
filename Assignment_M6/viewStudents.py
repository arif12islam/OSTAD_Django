import csv
def viewStudents():
    print("===== All Students =====")
    with open('students.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        i=1
        # Iterate through each row and display student details
        for row in reader:
            print(f"\nStudent: {i}")
            print("Name: ", row['name'])
            print("Roll: ", row['roll'])
            print("E-mail: ", row['email'])
            print("Department: ", row['dept'])
            i+=1

