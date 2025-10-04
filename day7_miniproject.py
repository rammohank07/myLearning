def get_student():
    students = {}
    high_score = 0
    top_name = ''

    try:
        n = int(input("How many students' details required to be entered: "))
    except ValueError:
        print("Invalid number")
        return

    while n > 0:
        s_name = input("Enter Student Name: ")
        marks = input("Enter marks for Maths, Science, English (space separated): ").strip().split()

        if len(marks) != 3:
            print("Marks should be entered for three subjects only. Try again.")
            continue

        try:
            marks = list(map(int, marks))
        except ValueError:
            print("Invalid marks entered. Try again.")
            continue

        students[s_name] = marks
        n -= 1

    print(f"\nStudent Details: {students}\n")

    for key, value in students.items():
        total = sum(value)
        avg_val = total / len(value)
        print(f"{key} → Total: {total}, Average: {avg_val:.2f}")

        if total > high_score:
            high_score = total
            top_name = key

    print(f"\nTop Scorer: {top_name} with marks {high_score}")

get_student()