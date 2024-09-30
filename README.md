# Password Checker

## Overview
This project provides a password checker tool that estimates how long it would take to brute-force crack a password and evaluates password strength based on common criteria (length, lowercase, uppercase, digits, and special characters).

## Usage

```python
from src.password_checker import PasswordChecker

checker = PasswordChecker("YourPassword123!")
result = checker.check_strength()

print(result)



### Running the Project

1. Clone the project to your local machine.
2. Install any necessary dependencies.
3. Use the `PasswordChecker` class to check password strength and estimate cracking time.
4. Run unit tests to verify the functionality.

This structure is professional and modular, allowing for easy testing, modification, and further development.