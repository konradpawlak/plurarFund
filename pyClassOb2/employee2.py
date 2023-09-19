class Employee:
    def __init__(self, fname, lname): # inicjuje atrybuty dla objektu, self -> atrybut tego wlasnie objektu
        self.fname = fname # atrybut
        self.lname = lname # atrybut

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary): # inicjuje atrybuty dla objektu, self -> atrybut tego wlasnie objektu
        super().__init__(fname, lname)
        self.salary = salary # atrybut
    
    def calculate_paycheck(self):
        return self.salary/52 #52 - weekly salary, 52 weeks in a year hashtagamericathings
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate
    
class CommissionEmplyee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate
    
    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck() # robimy tak, zeby nie zginelo poprawne liczenie
        total_commission = self.sales_num*self.com_rate
        return regular_salary + total_commission