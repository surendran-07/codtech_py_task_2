class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        """Add a new student."""
        if name in self.students:
            print(f"Student {name} already exists.")
        else:
            self.students[name] = {}
            print(f"Student {name} added.")

    def add_grades(self, name, grades_info):
        """Add or update a student's grades for multiple subjects."""
        if name not in self.students:
            print(f"Student {name} not found.")
            return
        
        for subject, grades in grades_info.items():
            if subject not in self.students[name]:
                self.students[name][subject] = []
            self.students[name][subject].extend(grades)
            print(f"Grades added for {name} in {subject}: {grades}")

    def calculate_average(self, name):
        """Calculate the average grade for a student."""
        if name not in self.students:
            print(f"Student {name} not found.")
            return None

        all_grades = []
        for grades in self.students[name].values():
            all_grades.extend(grades)

        if not all_grades:
            print(f"No grades available for {name}.")
            return None

        return sum(all_grades) / len(all_grades)

    def print_report(self):
        """Print all student grades and averages."""
        if not self.students:
            print("No students to display.")
            return

        for student, subjects in self.students.items():
            print(f"\n{student}'s Grades:")
            total_grades = []
            for subject, grades in subjects.items():
                print(f"  {subject}: {grades}")
                total_grades.extend(grades)

            if total_grades:
                average = sum(total_grades) / len(total_grades)
                print(f"  Average: {average:.2f}")
            else:
                print("  No grades recorded.")


def main():
    tracker = GradeTracker()

    while True:
        print("\nGrade Tracker Options:")
        print("1. Add Student")
        print("2. Add Grades")
        print("3. Calculate Average Grade")
        print("4. Print Report")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            name = input("Enter student's name: ").strip()
            tracker.add_student(name)
        elif choice == '2':
            name = input("Enter student's name: ").strip()
            try:
                grades_info = {}
                while True:
                    subject = input("Enter subject (or type 'done' to finish): ").strip()
                    if subject.lower() == 'done':
                        break
                    grades = list(map(float, input(f"Enter grades for {subject} separated by spaces: ").split()))
                    grades_info[subject] = grades
                tracker.add_grades(name, grades_info)
            except ValueError:
                print("Invalid input. Please enter numerical grades separated by spaces.")
        elif choice == '3':
            name = input("Enter student's name: ").strip()
            average = tracker.calculate_average(name)
            if average is not None:
                print(f"{name}'s average grade: {average:.2f}")
        elif choice == '4':
            tracker.print_report()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
