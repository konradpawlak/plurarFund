from employee_cl import Employee # 1st -> file name, 2nd -> class name

class Company:
    def __init__(self):
        self.employees = [] # for storing emplyees objects

    def add_employee(self, new_employee): # a method to add new employees to the list
        self.employees.append(new_employee) # add new employees to the list
    
    def display_employees(self):
        print('Current employees:\n')
        for i in self.employees:
            print(i.fname, i.lname,'salary: ', i.salary, 'PLN')
        print('---------------------------------')
    
    def display_weekly_pay(self):
        print('Tygodniowki ponizej:')
        for j in self.employees:
            print('Pracownik: ', j.fname, j.lname)
            print('Tygodniowka:')
            print(f'{j.calculate_paycheck():,.2f} PLN')
            print('-----------------------------')


def main():
    my_company = Company()

    employee1 = Employee('Matt','Troyan', 51250)
    my_company.add_employee(employee1)
    employee2 = Employee('Raff','Bryon', 41250)
    my_company.add_employee(employee2)
    employee3 = Employee('Kriss','Mayan', 61250)
    my_company.add_employee(employee3)

    print(my_company.employees)
    my_company.display_employees()
    my_company.display_weekly_pay()


main()