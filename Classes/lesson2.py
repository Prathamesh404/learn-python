# Object Oriented Programming in python.

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Nora", "Roberts", 8000)
emp_2 = Employee("Bella", "Graham", 10000)

# print(emp_1.pay)
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.fullname())
# print(emp_2.first)
# print(emp_2.last)
# print(emp_2.pay)
# print(emp_2.fullname())
#
# print(Employee.fullname(emp_1))
# print(Employee.fullname(emp_2))
#
# emp_1.apply_raise()
#
# print(emp_1.pay)
# Key Points to understand.
# "self" is an important argument while instantiating methods.
# It is necessary to notify the instance if we use Class name, to make it understand which instance to run.
