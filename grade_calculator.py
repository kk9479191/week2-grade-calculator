# Student Grade Calculator
# Name: Karan Kumar Genaram

def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent!"
    elif avg >= 80:
        return "B", "Very Good!"
    elif avg >= 70:
        return "C", "Good"
    elif avg >= 60:
        return "D", "Need Improvement"
    else:
        return "F", "Fail"

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100")
        except:
            print("Invalid input!")

def main():
    print("\n===== STUDENT GRADE CALCULATOR =====\n")

    # number of students
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            else:
                print("Enter positive number!")
        except:
            print("Invalid input!")

    names = []
    results = []

    for i in range(n):
        print(f"\n--- Student {i+1} ---")

        name = input("Enter name: ")
        while name.strip() == "":
            print("Name cannot be empty!")
            name = input("Enter name: ")

        math = get_marks("Math")
        science = get_marks("Science")
        english = get_marks("English")

        avg = (math + science + english) / 3
        grade, comment = calculate_grade(avg)

        names.append(name)
        results.append((avg, grade, comment))

    # Display Results
    print("\n===== RESULTS =====")
    print(f"{'Name':<15} {'Avg':<10} {'Grade':<10} Comment")
    print("-" * 50)

    for i in range(n):
        print(f"{names[i]:<15} {results[i][0]:<10.2f} {results[i][1]:<10} {results[i][2]}")

    # Statistics
    averages = [r[0] for r in results]

    class_avg = sum(averages) / len(averages)
    highest = max(averages)
    lowest = min(averages)

    print("\n===== STATISTICS =====")
    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Marks: {highest:.2f}")
    print(f"Lowest Marks: {lowest:.2f}")

    print("\nProgram Ended!")

if __name__ == "__main__":
    main()