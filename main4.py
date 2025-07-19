def is_armstrong(num):
    """
    Checks if a given number is an Armstrong number.

    Args:
        num: An integer to check.

    Returns:
        True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to easily find the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    armstrong_sum = 0
    temp_num = num

    # Calculate the sum of each digit raised to the power of num_digits
    while temp_num > 0:
        digit = temp_num % 10  # Get the last digit
        armstrong_sum += digit ** num_digits
        temp_num //= 10  # Remove the last digit

    return armstrong_sum == num

# Example usage:
number_to_check = 153
if is_armstrong(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")

number_to_check = 370
if is_armstrong(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")

number_to_check = 123
if is_armstrong(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")