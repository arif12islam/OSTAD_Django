import csv
def searchStudent():
    term = input("Enter search term (name/email/roll): ")
    print("search result:")
    found = False
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        i=1
        # Iterate through each row and check for the search term
        for row in reader:
            if term in row['roll'].lower() or row['name'].lower() or row['email'].lower():
                print(f"Student: {i}")
                print("Name: ", row['name'])
                print("Roll: ", row['roll'])
                print("E-mail: ", row['email'])
                print("Department: ", row['dept'])
                found = True
                i+=1

        if not found:
            print("no match found!")