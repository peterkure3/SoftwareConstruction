# Reactoring Employee management system using SOLID principles

## Introduction

This document provides an overview and documentation for the Employee Management System, a Python program designed to manage employees, calculate bonuses, and generate reports.

## Classes

### `Employee`

- **Description**: Represents an abstract base class for all types of employees.
- **Attributes**:
  - `name`: String representing the name of the employee.
- **Methods**:
  - `calculate_bonus()`: Abstract method to calculate the bonus for the employee. Must be implemented by subclasses.

### `Manager`

- **Description**: Represents a subclass of `Employee` for manager employees.
- **Methods**:
  - `calculate_bonus()`: Calculates the bonus for the manager.
  - `manage_team()`: Manages the team under the manager.

### `Developer`

- **Description**: Represents a subclass of `Employee` for developer employees.
- **Methods**:
  - `calculate_bonus()`: Calculates the bonus for the developer.
  - `code_review()`: Conducts a code review.

### `ReportGenerator`

- **Description**: Abstract base class for report generation.
- **Methods**:
  - `generate_report(employee)`: Abstract method to generate a report for the given employee.

### `ManagerReportGenerator`

- **Description**: Concrete implementation of `ReportGenerator` for generating manager reports.
- **Methods**:
  - `generate_report(manager)`: Generates a report for the manager employee.

### `DeveloperReportGenerator`

- **Description**: Concrete implementation of `ReportGenerator` for generating developer reports.
- **Methods**:
  - `generate_report(developer)`: Generates a report for the developer employee.

### `BonusCalculator`

- **Description**: Calculates bonuses for employees based on their roles.

## Usage

1. Instantiate `Manager` and `Developer` objects with respective names.
2. Use `ManagerReportGenerator` and `DeveloperReportGenerator` to generate reports for each employee.
3. Use `BonusCalculator` to calculate bonuses for each employee.
4. Call specific methods like `manage_team()` or `code_review()` for manager or developer employees, respectively.

## Example

```python
if __name__ == "__main__":
    manager = Manager("Alice")
    developer = Developer("Bob")

    report_generators = [ManagerReportGenerator(), DeveloperReportGenerator()]
    for generator in report_generators:
        generator.generate_report(manager)
        generator.generate_report(developer)

    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()
