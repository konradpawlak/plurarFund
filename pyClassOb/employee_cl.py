class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary/52 #52 - weekly salary, 52 weeks in a year hashtagamericathings
    
