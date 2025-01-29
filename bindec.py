def binary_to_decimal(binary_num):
    # Initialize the decimal number to 0
    decimal_num = 0
    
    # Loop through each digit in the binary number
    for digit in binary_num:
        # Multiply the current decimal value by 2 and add the binary digit
        decimal_num = (decimal_num * 2) + int(digit)
    
    return decimal_num

# Input: binary number as a string
binary_input = input("Enter a binary number: ")

# Validation: ensure the input contains only 0 and 1
if all(char in '01' for char in binary_input):
    # Convert to decimal
    decimal_result = binary_to_decimal(binary_input)
    print(f"Decimal equivalent of binary {binary_input} is {decimal_result}")
else:
    print("Invalid input. Please enter a valid binary number containing only 0s and 1s.")
