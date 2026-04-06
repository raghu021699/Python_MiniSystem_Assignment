class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def __repr__(self):
        return f"Student(name='{self.name}', fees={self.fees})"

students = [
    Student("Arun", 45000),
    Student("Priya", 55000),
    Student("Karthik", 30000),
    Student("Sneha", 50000),
    Student("Vikram", 40000)
]

student_names = list(map(lambda x: x.name, students))
print("Student Names:", student_names)
