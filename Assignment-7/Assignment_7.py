# ---------------- Person Class ----------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# ---------------- Employee Class ----------------
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)  # Call Person constructor
        self.employee_id = employee_id
        self.salary = salary

    def get_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary}")


# ---------------- Manager Class ----------------
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)  # Call Employee constructor
        self.department = department

    def get_manager_info(self):
        print("\n--- Manager Details ---")
        self.introduce()              # From Person
        self.get_employee_info()      # From Employee
        print(f"Department: {self.department}")

    def conduct_meeting(self):
        print(f"\n{self.name} is conducting a meeting for the {self.department} department.")


# ---------------- Main Program ----------------
if __name__ == "__main__":
    manager1 = Manager("Yatharth Sharma", 19, "EMP101", 75000, "IT")

    manager1.get_manager_info()
    manager1.conduct_meeting()