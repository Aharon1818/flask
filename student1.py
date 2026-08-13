class Student:
    def __init__(self, name, roll_number):
        """Initializes the student with a name and roll number."""
        self.name = name
        self.roll_number = roll_number
        self.grades = []  # Starts with an empty list for grades

    def add_grade(self, grade):
        """Adds a new grade to the student's record."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def get_average(self):
        """Calculates and returns the average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Prints the student's details."""
        print(f"Student Name: {self.name}")
        print(f"Roll Number:  {self.roll_number}")
        print(f"Grades:       {self.grades}")
        print(f"Average:      {self.get_average():.2f}")

