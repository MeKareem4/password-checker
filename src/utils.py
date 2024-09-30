# src/utils.py

def display_password_criteria(criteria: dict) -> str:
    """
    Nicely formats the password criteria result for display.
    """
    result = []
    result.append(f"Length >= 8: {'Yes' if criteria['length'] else 'No'}")
    result.append(f"Contains Lowercase: {'Yes' if criteria['has_lowercase'] else 'No'}")
    result.append(f"Contains Uppercase: {'Yes' if criteria['has_uppercase'] else 'No'}")
    result.append(f"Contains Digit: {'Yes' if criteria['has_digit'] else 'No'}")
    result.append(f"Contains Special Character: {'Yes' if criteria['has_special_char'] else 'No'}")
    
    return "\\n".join(result)