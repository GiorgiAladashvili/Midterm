class Person:
    """Base class for demonstrating inheritance."""
    def __init__(self, name):
        self._name = name 


class Student(Person):
    def __init__(self, name, roll_number, grade):
        super().__init__(name)
        self._roll_number = roll_number
        self._grade = grade

    @property
    def roll_number(self):
        return self._roll_number

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        self._grade = new_grade

    def display_info(self):
        print(f"Name: {self._name} | Roll Number: {self._roll_number} | Grade: {self._grade}")


class StudentManager:
    """Main controller"""
    def __init__(self):
        self.students = []
        self.next_roll_number = 1   # Auto-increment roll number

    def add_student(self):
        name = input("Enter student's name: ")

        while True:
            grade = input("Enter grade (A-F): ").upper()
            if grade in ['A', 'B', 'C', 'D', 'E', 'F']:
                break
            print("Invalid grade! Enter A, B, C, D, E, or F.")

        roll = self.next_roll_number
        self.next_roll_number += 1

        student = Student(name, roll, grade)
        self.students.append(student)
        print(f"Student added successfully! Assigned roll number: {roll}\n")

    def view_all(self):
        if not self.students:
            print("No students found.\n")
            return

        print("\n--- All Students ---")
        for stu in self.students:
            stu.display_info()
        print()

    def find_student(self):
        try:
            roll = int(input("Enter roll number: "))
        except ValueError:
            print("Invalid input!\n")
            return

        for stu in self.students:
            if stu.roll_number == roll:
                print("\nStudent found:")
                stu.display_info()
                print()
                return

        print("Student not found.\n")

    def update_grade(self):
        try:
            roll = int(input("Enter roll number to update: "))
        except ValueError:
            print("Invalid input!\n")
            return

        for stu in self.students:
            if stu.roll_number == roll:
                new_grade = input("Enter new grade (A-F): ").upper()
                if new_grade not in ['A', 'B', 'C', 'D', 'E', 'F']:
                    print("Invalid grade!\n")
                    return

                stu.grade = new_grade
                print("Grade updated successfully!\n")
                return

        print("Student not found.\n")


def menu():
    manager = StudentManager()

    while True:
        print("------ Student Management System ------")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student Grade")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            manager.find_student()
        elif choice == "4":
            manager.update_grade()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run program
menu()
