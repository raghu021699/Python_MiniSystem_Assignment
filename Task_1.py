class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.user_id}")

class Student(User):
    def __init__(self, name, user_id, dept, fees):
        super().__init__(name, user_id)
        self.dept = dept
        self.fees = fees

    def display(self):
        super().display()
        print(f"Department: {self.dept}")
        print(f"Fees: {self.fees}")

class Faculty(User):
    def __init__(self, name, user_id, salary):
        super().__init__(name, user_id)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")

class TempFaculty(Faculty):
    def __init__(self, name, user_id, salary, duration):
        super().__init__(name, user_id, salary)
        self.duration = duration   # duration in months

    def display(self):
        super().display()
        print(f"Duration (months): {self.duration}")

# Sample objects
s1 = Student("Raghu", 101, "CSE", 45000)
f1 = Faculty("Naveen", 201, 85000)
t1 = TempFaculty("Karthik", 301, 40000, 6)

# Display info
s1.display()
f1.display()
t1.display()