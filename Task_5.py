class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def __repr__(self):
        return f"Student(name='{self.name}', fees={self.fees})"


class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Faculty(name='{self.name}', salary={self.salary})"

students = [
    Student("Arun", 45000),
    Student("Priya", 5000),
    Student("Karthik", 30000),
    Student("Sneha", 51000),
    Student("Vikram", 40000)
]

high_fee_students = list(filter(lambda x: x.fees > 50000, students))
print("Students with fees > 50000:")
print(high_fee_students)

faculty = [
    Faculty("Meera", 80000),
    Faculty("Rohit", 60000),
    Faculty("Lavanya", 75000),
    Faculty("Anil", 20000),
    Faculty("Nisha", 90000)
]

high_salary_faculty = list(filter(lambda x: x.salary > 30000, faculty))

print("Faculty with salary > 30000:")
print(high_salary_faculty)