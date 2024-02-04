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
class ReportGenerator(ABC): #Define abstract report generator inheriting from ABC
    @abstractmethod
    def generate_report(self, employee):
        # pass statement to provide empty method body
        pass

class BonusCalculator:
    def calculate_bonus(self, employee):
        if employee.role == "Manager":
            return employee.calculate_manager_bonus()
        elif employee.role == "Developer":
            return employee.calculate_developer_bonus()

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
