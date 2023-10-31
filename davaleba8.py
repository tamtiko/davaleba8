class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Average Grade: {self.average_grade()}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def show_student_details(self, student_id):
        if student_id in self.students:
            self.students[student_id].display_details()
        else:
            print("Student not found.")

    def show_student_average_grade(self, student_id):
        if student_id in self.students:
            print(f"Average grade for {self.students[student_id].name}: {self.students[student_id].average_grade()}")
        else:
            print("Student not found.")