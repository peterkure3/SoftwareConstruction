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