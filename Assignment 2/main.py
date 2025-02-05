
# Program Name: Assignment2.py  (use the name the program is saved as)
# Course: IT3883/Section W02
# Student Name: Keyvon Thompson
# Assignment Number: Lab#2
# Due Date: 02/05/2025
# Purpose: This program reads in student names and six scores from a file,
#          computes each student’s average grade, then prints the results
#          in descending order by average. 
#          
# Resources Used:
#   1. Python official documentation for file I/O and list sorting
#   2. Class notes on string splitting and type conversion

def main():
    # You can change 'Assignment2Input.txt' to whatever your input file is named
    input_file = 'Assignment2input.txt'

    students = []

    # Read each line from the file
    with open(input_file, 'r') as file:
        for line in file:
            # Remove whitespace and split by space
            parts = line.strip().split()

            # First part is the student's name, the rest are scores
            name = parts[0]
            scores = parts[1:]  # The six scores as strings

            # Convert scores to integers
            scores = list(map(int, scores))

            # Calculate the average
            average = sum(scores) / len(scores)

            # Store as a tuple of (name, average)
            students.append((name, average))

    # Sort by average descending (highest first)
    # We use key=lambda x: x[1] to sort by the average,
    # and reverse=True to get descending order
    students.sort(key=lambda x: x[1], reverse=True)

    # Print results with two decimal places
    for student in students:
        print(f"{student[0]} {student[1]:.2f}")

# Standard Python boilerplate to call main()
if __name__ == "__main__":
    main()