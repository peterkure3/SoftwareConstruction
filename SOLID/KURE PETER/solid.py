# Importing abstract base classes library
from abc import ABC, abstractmethod

class Employee(ABC):# Abstract class introduced
    def __init__(self, name): #role attribute removed
        self.name = name

    @abstractmethod #@abstractmethod decosrator added to define an abstract method calculate_bonus
    def calculate_bonus(self):
        # pass statement to provide empty method body
        pass
# define class manager to inherit from employee
class Manager(Employee):
    # Override the abstract class method in the employee class
    def calculate_bonus(self):
        return 1000 #Return fixed bonus for managers
    
#define class developer to inherit from Employee
class Developer(Employee):
    # Override the abstract class method in the employee class
    def calculate_bonus(self): 
        return 500 #Return fixed bonus for developers
    
    def code_review(self): #define code_review method
    # Print conducting review statement
        print(f"{self.name} is conducting a code review.")
        
class ReportGenerator(ABC): #Define abstract report generator inheriting from ABC
    @abstractmethod
    def generate_report(self, employee):
        # pass statement to provide empty method body
        pass

class ManagerReportGenerator(ReportGenerator): #define subclass ManagerGeneratorReport inheriting from ReportGenerator
    # Override the abstract method generate_report() defined in the ReportGenerator class
    def generate_report(self, manager):
        print(f"Manager Report: {manager.name}")

class DeveloperReportGenerator(ReportGenerator): #define subclass DeveloperGeneratorReport inheriting from ReportGenerator
    # Override the abstract method generate_report() defined in the ReportGenerator class
    def generate_report(self, developer):
        print(f"Developer Report: {developer.name}")
class BonusCalculator:
    def calculate_bonus(self, employee):
        # Call calculate_bonus() method of the provided employee object
        return employee.calculate_bonus()
class Manager(Employee):
    def calculate_manager_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def calculate_developer_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    report_generator = Report()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()
