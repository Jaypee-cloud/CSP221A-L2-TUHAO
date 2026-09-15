class Employee:

    # Shared by all employees
    tax_rate = 0.10

    def __init__(self, name, base_salary):
        # Unique to each employee
        self.name = name
        self.base_salary = base_salary

    def net_pay(self):
        return self.base_salary - (self.base_salary * Employee.tax_rate)

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["base_salary"])


employee1 = Employee("John", 30000)
employee2 = Employee("Maria", 40000)

print(employee1.name, employee1.net_pay())
print(employee2.name, employee2.net_pay())


# Create employee from dictionary
data = {
    "name": "Peter",
    "base_salary": 50000
}

employee3 = Employee.from_dict(data)

print(employee3.name, employee3.net_pay())


# Change tax rate for everyone
Employee.tax_rate = 0.20

print("\nAfter changing tax rate:")

print(employee1.name, employee1.net_pay())
print(employee2.name, employee2.net_pay())
print(employee3.name, employee3.net_pay())
