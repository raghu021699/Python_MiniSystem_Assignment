from functools import reduce

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
    Student("Priya", 55000),
    Student("Karthik", 30000),
    Student("Sneha", 50000),
    Student("Vikram", 40000)
]

total_fees = reduce(lambda acc, x: acc + x.fees, students, 0)
print("Total Fees Collected:", total_fees)

faculty = [
    Faculty("Meera", 80000),
    Faculty("Rohit", 60000),
    Faculty("Lavanya", 75000),
    Faculty("Anil", 50000),
    Faculty("Nisha", 90000)
]

total_salary = reduce(lambda acc, x: acc + x.salary, faculty, 0)
print("Total Salary of Faculty:", total_salary)