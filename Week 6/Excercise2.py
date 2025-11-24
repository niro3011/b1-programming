grades_db = []

def add_student_grades(grades_db):
    # Erlaubt beliebig viele Schüler, nicht nur 7
    while True:
        student_name = input("Please put in your Name (or type EXIT to stop): ")
        if student_name.lower() == "exit":
            break
        
        math_score = input("Please put in your Math-Score: ")
        history_score = input("Please put in your History-Score: ")
        programming_score = input("Please put in your Programming-Score: ")
        
        student_data = {
            "Name": student_name,
            "Math-Score": math_score,
            "History-Score": history_score,
            "Programming-Score": programming_score
        }

        if student_data in grades_db:
            print("Duplicate detected! Data NOT added.")
            continue
        else:
            grades_db.append(student_data)
            print("Student added")

    print(grades_db)


def calcstatistics(grades_db):
    enteredname = input("Please enter the name for the student you want the statistics for: ")

    for student_data in grades_db:
        if student_data["Name"] == enteredname:
            math_score = int(student_data["Math-Score"])
            history_score = int(student_data["History-Score"])
            programming_score = int(student_data["Programming-Score"])
            
            # average grade
            avg_grade = (math_score + history_score + programming_score) / 3
            # highest grade
            high_grade = max([math_score, history_score, programming_score])
            # lowest grade
            low_grade = min([math_score, history_score, programming_score])

            print(f"\nStatistics for {enteredname}:")
            print(f"Math: {math_score}")
            print(f"History: {history_score}")
            print(f"Programming: {programming_score}")
            print(f"Average: {avg_grade:.2f}")
            print(f"Highest Grade: {high_grade}")
            print(f"Lowest Grade: {low_grade}")
            return
    
    print("Student not found.")


def fullreport(grades_db):
    print("\n===== FULL REPORT =====")

    total_avg = 0
    count = 0

    for student_data in grades_db:
        math_score = int(student_data["Math-Score"])
        history_score = int(student_data["History-Score"])
        programming_score = int(student_data["Programming-Score"])

        all_avg = (math_score + history_score + programming_score) / 3
        total_avg += all_avg
        count += 1

    if count > 0:
        overall_avg = total_avg / count
        print(f"\nOverall class average: {overall_avg:.2f}")
    else:
        print("No data available.")
        return

    subjects = {
        "Math-Score": "Mathe",
        "History-Score": "Geschichte",
        "Programming-Score": "Programmieren"
    }

    for key, label in subjects.items():
        scores = [(s["Name"], int(s[key])) for s in grades_db]

        min_score = min(scores, key=lambda x: x[1])[1]
        max_score = max(scores, key=lambda x: x[1])[1]

        min_students = [name for name, score in scores if score == min_score]
        max_students = [name for name, score in scores if score == max_score]

        print(f"\n📘 {label}:")
        print(f"   Lowest score:  {min_score} (Students: {', '.join(min_students)})")
        print(f"   Highest score: {max_score} (Students: {', '.join(max_students)})")



while True:
    print("\n==== MENU ====")
    print("1. Add grades for students")
    print("2. View statistics for one student")
    print("3. Generate full report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student_grades(grades_db)
    elif choice == '2':
        calcstatistics(grades_db)
    elif choice == '3':
        fullreport(grades_db)
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")