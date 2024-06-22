# Create class Person
class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Create class Employee inherit from class Person
class Employee(Person):
    def __init__(self, name, phone, annual_salary, year_of_starting_work):
        super().__init__(name, phone)
        self.annual_salary = annual_salary
        self.year_of_starting_work = year_of_starting_work

# Create class StackEmployee
class StackEmployee():
    def __init__(self, capacity):
        self.capacity = capacity 
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError('pop from empty stack')
    def push(self, obj):
        if not self.is_full():
            self.stack.append(obj)
        else:
            raise IndexError('push to full stack')
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError('top from empty stack')

# create object StackEmployee with capacity 5
stack_employee = StackEmployee(5)

# data test
employee1 = Employee("Anh", "1234567890", 50000, 2015)
employee2 = Employee("Binh", "0987654321", 60000, 2016)
employee3 = Employee("Chanh", "5555555555", 80000, 2017)
employee4 = Employee("Dien", "5555555555", 90000, 2018)
employee5 = Employee("Em", "5555555555", 100000, 2019)
employee6 = Employee("Fine", "5555555555", 40000, 2020)

# use stack
print(stack_employee.is_empty())
print()
stack_employee.push(employee1)  
stack_employee.push(employee2)    
print(stack_employee.is_full())
print()
print(stack_employee.top().name) 
print() 
stack_employee.push(employee3)  
print(stack_employee.pop().name)
print() 
print(stack_employee.top().name)
print()
print(stack_employee.is_full())
print()
stack_employee.push(employee3)  
stack_employee.push(employee4)
stack_employee.push(employee5) 
stack_employee.push(employee6)       
print(stack_employee.is_full())
print()