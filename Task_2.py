from abc import ABC, abstractmethod

class AbstractUser(ABC):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    @abstractmethod
    def get_details(self):
        pass


class Student(AbstractUser):
    def __init__(self, name, user_id, dept, fees):
        super().__init__(name, user_id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.user_id}, Department: {self.dept}, Fees: {self.fees}"


class Faculty(AbstractUser):
    def __init__(self, name, user_id, salary):
        super().__init__(name, user_id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.user_id}, Salary: {self.salary}"



class TempFaculty(Faculty):
    def __init__(self, name, user_id, salary, duration):
        super().__init__(name, user_id, salary)
        self.duration = duration

    def get_details(self):
        return (f"Temp Faculty: {self.name}, ID: {self.user_id}, "
                f"Salary: {self.salary}, Duration: {self.duration} months")


# Sample objects and output
s1 = Student("Arun", 101, "CSE", 45000)
f1 = Faculty("Meera", 201, 85000)
t1 = TempFaculty("Karthik", 301, 40000, 6)

print(s1.get_details())
print(f1.get_details())
print(t1.get_details())