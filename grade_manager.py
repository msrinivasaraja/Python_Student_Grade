
# ==========================================
# Student Grade Manager
# Week 1 - Day 2 Assignment
# ==========================================

# Step 1: Create an empty list to store students
students = []


# Step 2: Function to calculate student grade
def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"


# Step 3: Function to add a student
def add_student():

    print("\n----- Add Student -----")

    # Get student name
    name = input("Enter student name: ").strip()

    # Validate student name
    if not name:
        print("Error: Student name cannot be empty.")
        return

    # Get student mark
    try:
        mark = int(input("Enter student mark (0-100): "))

    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Validate mark range
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        return

    # Store student information
    student = {
        "name": name,
        "mark": mark,
        "grade": get_grade(mark)
    }

    students.append(student)

    print(f"Student {name} added successfully!")


# Step 4: Function to display student results
def show_results():

    print("\n========== STUDENT RESULTS ==========")

    # Check whether students are available
    if not students:
        print("No student records found.")
        return

    # Print table header
    print(f"{'Name':<20}{'Mark':<12}{'Grade':<10}")
    print("-" * 42)

    # Display each student
    for student in students:

        print(
            f"{student['name']:<20}"
            f"{student['mark']:<12}"
            f"{student['grade']:<10}"
        )

    print("-" * 42)

    # Calculate class statistics
    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display statistics
    print(
        f"Average : {average:<8.1f}"
        f"Highest : {highest:<5}"
        f"Lowest  : {lowest:<5}"
        )

    print("=" * 42)


# Step 5: Main menu function
def main():

    while True:

        print("\n========== STUDENT GRADE MANAGER ==========")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            show_results()

        elif choice == "3":

            print("Thank you for using Student Grade Manager!")
            break

        else:

            print("Invalid choice. Please select 1, 2 or 3.")


# Step 6: Start the application
if __name__ == "__main__":
    main()
