"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        line = line.strip()  # Remove newline character
        parts = line.split(',')  # Split by comma
        parts[2] = int(parts[2])  # Convert student count to int
        subjects.append(parts)  # Add to the list
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display subject details from the data."""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")


main()
