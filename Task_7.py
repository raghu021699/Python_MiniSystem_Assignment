# Classes
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def __repr__(self):
        return f"Student(name='{self.name}', fees={self.fees})"


def process_user(users, func):
    return list(map(func, users))

students = [
    Student("Arun", 45000),
    Student("Priya", 55000),
    Student("Karthik", 30000),
    Student("Sneha", 50000),
    Student("Vikram", 40000)
]


names = process_user(students, lambda x: x.name)
print("Names:", names)

fees = process_user(students, lambda x: x.fees)
print("Fees:", fees)
