# src/brute_force_time.py

class BruteForceTime:
    def __init__(self, password: str):
        self.password = password
    
    def estimate_time(self) -> str:
        char_space = self._calculate_charset_space()
        if char_space == 0:  # Prevent division by zero if charset calculation fails
            return "Unable to calculate: Invalid password"

        num_combinations = char_space ** len(self.password)  # Total number of combinations
        guesses_per_second = 1e11  # Adjusted to 100 billion guesses per second
        
        time_to_crack_seconds = num_combinations / guesses_per_second  # Time in seconds
        
        return self._format_time(time_to_crack_seconds)
    
    def _calculate_charset_space(self) -> int:
        # Calculate the character set size based on what types of characters are present
        charset_space = 0
        if any(c.islower() for c in self.password):
            charset_space += 26  # Lowercase letters
        if any(c.isupper() for c in self.password):
            charset_space += 26  # Uppercase letters
        if any(c.isdigit() for c in self.password):
            charset_space += 10  # Digits
        if self._contains_special_characters():
            charset_space += 32  # Special characters (symbols)
        
        return charset_space
    
    def _contains_special_characters(self) -> bool:
        """
        Checks if the password contains any special characters from a predefined set.
        This set can be expanded as needed.
        """
        special_characters = "!@#$%^&*()-_=+[{]};:'\\",<.>/?\\\\|`~"
        return any(c in special_characters for c in self.password)
    
    def _format_time(self, seconds: float) -> str:
        # Format time to a readable string
        if seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            return f"{seconds / 60:.2f} minutes"
        elif seconds < 86400:
            return f"{seconds / 3600:.2f} hours"
        elif seconds < 31536000:
            return f"{seconds / 86400:.2f} days"
        else:
            return f"{seconds / 31536000:.2f} years"