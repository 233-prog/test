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
    decimal_value = int(value) 
    binary_str = ""
    while decimal_value > 0:
        remainder = decimal_value % 2
        binary_str = binary_str + str(remainder)
        decimal_value = decimal_value // 2 
    return binary_str[::-1]
  
def convert_decimal_to_hex(value):
    Hex = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hex_digits = []
    decimal_value = int(value)
    while decimal_value > 0:
        remainder = decimal_value % 16
        hex_digits.append(Hex[remainder])
        decimal_value = decimal_value // 16
    return hex_digits[::-1]

def convert_hex_to_decimal(value):
    hex_values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,'6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal_value = 0
    position = 0
    for char in value[::-1]:
        hex_digit_value = hex_values[char.upper()]
        power_of_16 = 16 ** position
        value = hex_digit_value * power_of_16
        decimal_value = decimal_value+ value
        position = position + 1
    return decimal_value

def convert_binary_to_hex(binary_str):  
        HEX_TO_BINARY = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111",'8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"} 
        hex_digits = []
        while binary_str:
            hex_digit = int(binary_str[:4], 2)
            hex_digits.append(hex(hex_digit)[2:].upper())
            binary_str = binary_str[4:]
        return ''.join(hex_digits)

def convert_hex_to_binary(value):
    HEX_TO_BINARY = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
    binary_result = ""
    for char in value:
        binary_result = binary_result + HEX_TO_BINARY[char.upper()]
    return binary_result

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