# Exercise 2: Student Grade Analyzer

# 1. Initialize Data Structures
grades_db = []

# 2. Function to Add Student Grades
def add_student_grades(grades_db):
    """Add a new student with their grades to the database."""
    student_name = input("Please enter student name: ")
    
    # Check if student already exists
    for student in grades_db:
        if student["Name"].lower() == student_name.lower():
            print(f"Student '{student_name}' already exists!")
            update = input("Do you want to update their grades? (yes/no): ")
            if update.lower() == 'yes':
                grades_db.remove(student)
                break
            else:
                return
    
    # Get grades with validation
    try:
        math_score = float(input("Enter Math score: "))
        history_score = float(input("Enter History score: "))
        programming_score = float(input("Enter Programming score: "))
        
        student_data = {
            "Name": student_name,
            "Math-Score": math_score,
            "History-Score": history_score,
            "Programming-Score": programming_score
        }
        
        grades_db.append(student_data)
        print(f"✓ Student '{student_name}' added successfully!")
        
    except ValueError:
        print("✗ Error: Please enter valid numbers for grades.")

# 3. Function to Calculate Statistics
def calculate_statistics(grades_db, student_name):
    """Calculate and display statistics for a specific student."""
    found = False
    
    for student_data in grades_db:
        if student_data["Name"].lower() == student_name.lower():
            found = True
            name = student_data["Name"]
            math_score = student_data["Math-Score"]
            history_score = student_data["History-Score"]
            programming_score = student_data["Programming-Score"]
            
            # Calculate statistics
            avg_grade = (math_score + history_score + programming_score) / 3
            high_grade = max(math_score, history_score, programming_score)
            low_grade = min(math_score, history_score, programming_score)
            
            # Display results
            print("\n" + "="*50)
            print(f"Statistics for {name}")
            print("="*50)
            print(f"Math Score:        {math_score:.2f}")
            print(f"History Score:     {history_score:.2f}")
            print(f"Programming Score: {programming_score:.2f}")
            print("-"*50)
            print(f"Average Grade:     {avg_grade:.2f}")
            print(f"Highest Grade:     {high_grade:.2f}")
            print(f"Lowest Grade:      {low_grade:.2f}")
            print("="*50)
            break
    
    if not found:
        print(f"✗ Student '{student_name}' not found in database.")

# 4. Function to Generate Full Report
def generate_full_report(grades_db):
    """Generate and display a complete report for all students."""
    if not grades_db:
        print("✗ No students in database yet.")
        return
    
    print("\n" + "="*70)
    print("FULL STUDENT REPORT")
    print("="*70)
    
    total_avg = 0
    
    for student_data in grades_db:
        name = student_data["Name"]
        math_score = student_data["Math-Score"]
        history_score = student_data["History-Score"]
        programming_score = student_data["Programming-Score"]
        
        # Calculate statistics
        avg_grade = (math_score + history_score + programming_score) / 3
        high_grade = max(math_score, history_score, programming_score)
        low_grade = min(math_score, history_score, programming_score)
        total_avg += avg_grade
        
        # Display individual student report
        print(f"\nStudent: {name}")
        print(f"  Math: {math_score:.2f} | History: {history_score:.2f} | Programming: {programming_score:.2f}")
        print(f"  Average: {avg_grade:.2f} | Highest: {high_grade:.2f} | Lowest: {low_grade:.2f}")
        print("-"*70)
    
    # Calculate and display overall average
    overall_avg = total_avg / len(grades_db)
    print(f"\nOVERALL CLASS AVERAGE: {overall_avg:.2f}")
    print(f"Total Students: {len(grades_db)}")
    print("="*70)

# 5. Main Program Loop
def main():
    """Main program loop with menu interface."""
    print("Welcome to Student Grade Analyzer!")
    
    while True:
        print("\n" + "="*50)
        print("STUDENT GRADE ANALYZER MENU")
        print("="*50)
        print("1. Add grades for a student")
        print("2. View statistics for a student")
        print("3. Generate full report")
        print("4. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student_grades(grades_db)
            
        elif choice == '2':
            if not grades_db:
                print("✗ No students in database yet.")
            else:
                student_name = input("Enter student name: ")
                calculate_statistics(grades_db, student_name)
                
        elif choice == '3':
            generate_full_report(grades_db)
            
        elif choice == '4':
            print("\nThank you for using Student Grade Analyzer!")
            print("Goodbye!")
            break
            
        else:
            print("✗ Invalid choice. Please enter 1, 2, 3, or 4.")

main()