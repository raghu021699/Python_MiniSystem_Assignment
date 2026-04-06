from abc import ABC, abstractmethod
from functools import reduce

class AbstractUser(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_details(self):
        pass


class Student(AbstractUser):
    def __init__(self, name, fees):
        super().__init__(name)
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, Fees: {self.fees}"

class Faculty(AbstractUser):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, Salary: {self.salary}"

def process_user(users, func):
    return list(map(func, users))

students = [
    Student("Arun", 45000),
    Student("Priya", 55000),
    Student("Karthik", 30000),
    Student("Sneha", 50000),
    Student("Vikram", 40000)
]

faculty = [
    Faculty("Meera", 80000),
    Faculty("Rohit", 60000),
    Faculty("Lavanya", 75000),
    Faculty("Anil", 50000),
    Faculty("Nisha", 90000)
]

all_users = students + faculty

print("1. ALL USER DETAILS:")
for user in all_users:
    print(user.get_details())

sorted_students = sorted(students, key=lambda x: x.fees)
sorted_faculty = sorted(faculty, key=lambda x: x.salary)

print("2. SORTED STUDENTS (by fees):")
for s in sorted_students:
    print(s.get_details())

print("3. SORTED FACULTY (by salary):")
for f in sorted_faculty:
    print(f.get_details())

filtered_students = list(filter(lambda x: x.fees > 50000, students))
filtered_faculty = list(filter(lambda x: x.salary > 70000, faculty))

print("4. FILTERED STUDENTS (fees > 50k):")
for s in filtered_students:
    print(s.get_details())

print("5. FILTERED FACULTY (salary > 70k):")
for f in filtered_faculty:
    print(f.get_details())

total_fees = reduce(lambda acc, x: acc + x.fees, students, 0)
total_salary = reduce(lambda acc, x: acc + x.salary, faculty, 0)

print("7. TOTAL FEES COLLECTED:", total_fees)
print("8. TOTAL FACULTY SALARY:", total_salary)


combined_processing = process_user(
    students,
    lambda x: x.name.upper() if x.fees > 40000 else x.name.lower()
)

print("9. FUNCTIONAL PROGRAMMING OUTPUT (map + lambda + HOF):")
print(combined_processing)