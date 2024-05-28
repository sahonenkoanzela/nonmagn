class Employee:
    def __init__(self, name, id_number, position, salary):
        self.name = name
        self.id_number = id_number
        self.position = position
        self.salary = salary

    def display_employee_details(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

# Example usage:
employee1 = Employee("John Doe", "12345", "Software Engineer", 80000)
employee1.display_employee_details()
