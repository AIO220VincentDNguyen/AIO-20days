class Staff:
    def __init__(self, name, age, address, salary, total_time):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.total_time = total_time
    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Address: {self.address}')
        print(f'Salary: {self.salary}')
        print(f'Total time: {self.total_time}')
    def calculate_bonus(self):
        if self.total_time < 100:
            return self.salary * 0
        elif self.total_time >= 100 and self.total_time < 200:
            return int(self.salary * 10 / 100)
        else:
            return int(self.salary * 20 / 100)

# Test case 1
name = 'Anh'
age = 26
address = 'xyz'
salary = 30000000
total_time = 300
nhan_vien_a = Staff('Anh', 26, 'xyz', 30000000, 300)
nhan_vien_a.show_info()
print(f'Bonus: {nhan_vien_a.calculate_bonus()}')
print()
# Test case 2
name = 'Bình'
age = 20
address = 'bcd'
salary = 50000000
total_time = 199
nhan_vien_b = Staff('Bình', 20, 'bcd', 50000000, 199)
nhan_vien_b.show_info()
print(f'Bonus: {nhan_vien_b.calculate_bonus()}')
print()
# Test case 3
name = 'Canh'
age = 30
address = 'yhy'
salary = 10000000
total_time = 99
nhan_vien_c = Staff('Canh', 30, 'yhy', 10000000, 99)
nhan_vien_c.show_info()
print(f'Bonus: {nhan_vien_c.calculate_bonus()}')
print()