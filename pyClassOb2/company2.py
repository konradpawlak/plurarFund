from employee2 import Employee, SalaryEmployee, HourlyEmployee, CommissionEmplyee # 1st -> file name, 2nd -> class name

class Company:
    def __init__(self):
        self.employees = [] # for storing emplyees objects

    def add_employee(self, new_employee): # a method to add new employees to the list
        self.employees.append(new_employee) # add new employees to the list
    
    def display_employees(self):
        print('Current employees:\n')
        for i in self.employees:
            print(i.fname, i.lname,'salary: PLN')
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

    employee1 = SalaryEmployee('Matt','Troyan', 51250)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Raff','Bryon', 35, 55)
    my_company.add_employee(employee2)
    employee3 = CommissionEmplyee('Kriss','Mayan', 31055, 17, 125)
    my_company.add_employee(employee3)
    employee4 = HourlyEmployee('Rikhs','Sakit', 25, 15)
    my_company.add_employee(employee4)


    print(my_company.employees)
    my_company.display_employees()
    my_company.display_weekly_pay()


main()