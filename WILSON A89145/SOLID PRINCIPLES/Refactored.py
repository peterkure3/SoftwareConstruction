class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Report:
    def generate_report(self, employee):
        if employee.role == "Manager":
           print(f"Manager Report: {manager.name}")
        elif employee.role == "Developer":
             print(f"Developer Report: {developer.name}")

class BonusCalculator:
    def calculate_bonus(self, employee):
        if employee.role == "Manager":
            return 1000
        elif employee.role == "Developer":
           return 500
        
class Manager(Employee):
    
    def manage_team(self):
        print(f"{self.name} is managing the team.")
