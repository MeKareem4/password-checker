# src/password_checker.py

from .password_criteria import PasswordCriteria
from .brute_force_time import BruteForceTime

class PasswordChecker:
    def __init__(self, password: str):
        self.password = password
        self.criteria = PasswordCriteria(password)
        self.brute_force_calculator = BruteForceTime(password)
        
    def check_strength(self):
        # First, validate password based on criteria
        criteria_result = self.criteria.evaluate()
        # Calculate brute force time based on criteria
        brute_force_time = self.brute_force_calculator.estimate_time()
        
        return {
            "criteria_met": criteria_result,
            "brute_force_time": brute_force_time
        }