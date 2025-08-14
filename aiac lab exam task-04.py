import csv

def read_student_marks(filename):
    students = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            try:
                marks = [float(row['Subject1']), float(row['Subject2']), float(row['Subject3'])]
            except ValueError:
                print(f"Invalid marks for student {name}. Skipping.")
                continue
            total = sum(marks)
            average = total / 3
            students.append({
                'Name': name,
                'Total': total,
                'Average': average
            })
    return students

if __name__ == "__main__":
    filename = input("Enter the CSV filename (e.g., students.csv): ")
    try:
        results = read_student_marks(filename)
        print("\nStudent Results:")
        for student in results:
            print(f"Name: {student['Name']}, Total: {student['Total']}, Average: {student['Average']:.2f}")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
