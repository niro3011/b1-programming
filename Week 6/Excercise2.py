# Exercise 2: Student Grade Analyzer
# 1. Initialize Data Structures
# TODO: Create an empty dictionary to store student names and their grades.
# Keys will be student names (string), values will be lists of grades (integers or floats).
# Example:
grades_db = []


# 2. Function to Add Student Grades
# TODO: Define a function that prompts the user for a student's name and multiple grades.
# Store these grades in the student_grades dictionary.
# Handle cases where a student already exists or is new.
def add_student_grades(grades_db):
    while len(grades_db) <= 6:
        student_name = input("Please put in your Name:")
        student_score = input("Please put in your Score:")
        math_score = input("Please put in your Math-Score")
        history_score = input("Please put in your History-Score")
        programming_score = input ("Please put in your Programming-Score")
        
        student_data = {
            "Name" : (student_name),
            "Score" : (student_score),
            "Math-Score" : (math_score),
            "History-Score" : (history_score),
            "Programming-Score" : (programming_score)
        }

        if student_data in grades_db:
            print("Duplicate detected! Data NOT added.")
            continue
        else:
            grades_db.append(student_data)
            print("Student added")



    print(grades_db)
    return student_data, student_name,student_score
add_student_grades(grades_db)

# 3. Function to Calculate Statistics
# TODO: Define a function that takes a student's name and calculates their:
def calculation(grades_db):
    for student_data in grades_db:
        student_name = student_data["Name"]
        math_score = int(student_data["Math-Score"])
        history_score = int(student_data["History-Score"])
        programming_score = int(student_data["Programming-Score"])
asd
        avg_grade = (math_score + history_score + programming_score) / 3

        # highest grade
        high_grade = max([math_score, history_score, programming_score])

        # lowest grade
        low_grade = min([math_score, history_score, programming_score])

        print(student_name, avg_grade, high_grade, low_grade)

# 4. Function to Generate Full Report
# TODO: Define a function that prints a report for all students, including their:
# - Name
# - All recorded grades
# - Average grade
# - Highest grade
# - Lowest grade
# Also, calculate and display the overall average grade for all students.
# def generate_full_report(grades_db):
# # ... implementation ...
# pass
# 5. Main Program Loop
# TODO: Implement a loop that allows the user to:
# - Add grades for a student
# - View statistics for a specific student
# - Generate a full report for all students
# - Exit the program
# Example usage:
# while True:
# print("\nStudent Grade Analyzer Menu:")
# print("1. Add grades for a student")
# print("2. View statistics for a student")
# print("3. Generate full report")
# print("4. Exit")
# choice = input("Enter your choice: ")
# if choice == '1':
# # ... call add_student_grades ...
# pass
# elif choice == '4':
# break
# # ... other choices ..