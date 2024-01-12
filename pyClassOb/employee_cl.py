class Employee:
    def __init__(self, fname, lname, salary): # inicjuje atrybuty dla objektu, self -> atrybut tego wlasnie objektu
        self.fname = fname # atrybut
        self.lname = lname # atrybut
        self.salary = salary # atrybut
    
    def calculate_paycheck(self):
        return self.salary/52 #52 - weekly salary, 52 weeks in a year hashtagamericathings
    
