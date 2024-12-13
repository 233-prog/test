def decimal_to_binary(decimal_num):
    """Converts a decimal number to its binary representation.

    Args:
        decimal_num: The decimal number to convert.

    Returns:
        The binary representation of the decimal number as a string.
    """

    if decimal_num == 0:
        return "0"

    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2

    return binary_num 

def check_even_odd(binary_num):
    """Checks if a binary number represents an even or odd decimal number.

    Args:
        binary_num: The binary number as a string.

    Returns:
        "Even" if the number is even, "Odd" otherwise.
    """

    last_digit = binary_num[-1]
    if last_digit == '0':
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    decimal_num = int(input("Enter a decimal number: "))
    binary_num = decimal_to_binary(decimal_num)
    parity = check_even_odd(binary_num)
    print(f"The binary representation of {decimal_num} is {binary_num}")
    print(f"The number {decimal_num} is {parity}.")