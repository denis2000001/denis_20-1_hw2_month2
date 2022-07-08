class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name
class Person(Company):
    def __init__(self, company_bank, company_name, first_name, last_name,salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def get_salary(self):
        if self.salary <= self.company_bank:
            self.company_bank -= self.salary
            print(f"Сотрудник получил зарплату в размере: {self.salary}$")
        else:
            print("У компании не достаточно средств!")
    def person_info(self):
        print(f"The name - {self.first_name}, the surname - {self.last_name}. Salary is {self.salary}$")
GigaChad = Person(150000, 'GigaChad', 'Roma', 'Sat', 80000)
GigaChad.get_salary()
GigaChad.person_info()