# src/password_criteria.py

class PasswordCriteria:
    MIN_LENGTH = 8  # Minimum password length
    
    def __init__(self, password: str):
        self.password = password
    
    def evaluate(self) -> dict:
        # Return a dictionary evaluating the password against various criteria
        return {
            "length": len(self.password) >= self.MIN_LENGTH,
            "has_lowercase": any(c.islower() for c in self.password),
            "has_uppercase": any(c.isupper() for c in self.password),
            "has_digit": any(c.isdigit() for c in self.password),
            "has_special_char": self._contains_special_characters()  # Check for special characters
        }
    
    def _contains_special_characters(self) -> bool:
        special_characters = "!@#$%^&*()-_=+[{]};:'\\",<.>/?\\\\|`~"
        return any(c in special_characters for c in self.password)
