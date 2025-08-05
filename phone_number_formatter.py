

"""
Phone Number Formatter
----------------------
Formats a raw phone number input into a standardized format:
e.g., (123) 456-7890

Supports 10-digit US phone numbers, ignoring common separators.
"""

import re

def format_phone_number(raw_number):
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', raw_number)

    # Check if the number has 10 digits
    if len(digits) != 10:
        return None

    # Format: (123) 456-7890
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    return formatted

def main():
    raw_number = input("Enter a 10-digit US phone number: ").strip()
    formatted_number = format_phone_number(raw_number)

    if formatted_number:
        print(f"Formatted Phone Number: {formatted_number}")
    else:
        print("Invalid input. Please enter exactly 10 digits.")

if __name__ == "__main__":
    main()
