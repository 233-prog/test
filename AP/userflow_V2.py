def validate_binary(value):
    for char in value:
        if char != '0' and char != '1':
            return False
    return True

def validate_decimal(value):
    for char in value:
        if char not in '0123456789':
            return False
    return True

def validate_hex(value):
    hex_chars = "0123456789ABCDEFabcdef"
    for char in value:
        if char not in hex_chars:
            return False
    return True

def convert_binary_to_decimal(value):
    decimal_value = 0
    position_counter = 0
    for bit in reversed(value):
        decimal_value += int(bit) * (2 ** position_counter)
        position_counter = position_counter + 1
    return decimal_value

def convert_decimal_to_binary(value):
   binary_str = ""
   while decimal_value > 0:
        remainder = decimal_value % 2
        binary_str = binary_str + str(remainder)
        decimal_value = decimal_value // 2  
   #return binary_str[::-1]

def convert_decimal_to_hex(value):
    Hex = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hex_digits = []
    while decimal_value > 0:
        remainder = decimal_value % 16
        hex_digits.append(Hex[remainder])
        decimal_value = decimal_value // 16

def convert_hex_to_decimal(value):
    hex_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# if '0' <= value <= '9':
# elif 'A' <= value <= 'F':

def convert_binary_to_hex(value):
    pass

def convert_hex_to_binary(value):
    pass

def main():
    from_NS = int(input("Choose the current Number System (1 - Binary, 2 - Decimal, 3 - Hexadecimal): "))
    if from_NS not in [1, 2, 3]:
        print("Invalid choice for 'From Number System'. Must be 1, 2, or 3.")
        return

    to_NS = int(input("Choose the desired Number System (1 - Binary, 2 - Decimal, 3 - Hexadecimal): "))
    if to_NS not in [1, 2, 3]:
        print("Invalid choice for 'To Number System'. Must be 1, 2, or 3.")
        return

    if from_NS == to_NS:
        print("From Number System and To Number System cannot be the same.")
        return

    value = input("Enter the value to be converted: ")
    if not (1 <= len(value) <= 8):
        print("Invalid input. The value must be between 1 and 8 in length.")
        return

    is_valid = False
    if from_NS == 1: 
        if validate_binary(value):
            is_valid = True
        else:
            print("Error: The value entered is not a valid binary number.")
    elif from_NS == 2: 
        if validate_decimal(value):
            is_valid = True
        else:
            print("Error: The value entered is not a valid decimal number.")
    elif from_NS == 3: 
        if validate_hex(value):
            is_valid = True
        else:
            print("Error: The value entered is not a valid hexadecimal number.")
    else:
        print("Error: The selected number system is invalid.")
        return

    result = ""
    if from_NS == 1 and to_NS == 2: 
        result = convert_binary_to_decimal(value)
    elif from_NS == 1 and to_NS == 3: 
        result = convert_binary_to_hex(value)
    elif from_NS == 2 and to_NS == 1: 
        result = convert_decimal_to_binary(value)
    elif from_NS == 2 and to_NS == 3: 
        result = convert_decimal_to_hex(value)
    elif from_NS == 3 and to_NS == 1: 
        result = convert_hex_to_binary(value)
    elif from_NS == 3 and to_NS == 2: 
        result = convert_hex_to_decimal(value)

    print(f"From Number System: {from_NS}")
    print(f"To Number System: {to_NS}")
    print(f"Input Value: {value}")
    print(f"Converted Value: {result}")

if __name__ == "__main__":
    main()