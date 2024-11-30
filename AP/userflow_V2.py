def validate_binary(value):
    return all(char in '01' for char in value)

def validate_decimal(value):
    return all(char in '1234567890' for char in value)

def validate_hex(value):
    hex_chars = "0123456789ABCDEFabcdef"
    return all(char in hex_chars for char in value)

def convert_binary_to_decimal(value):
    pass

def convert_decimal_to_binary(value):
    pass

def convert_decimal_to_hex(value):
    pass

def convert_hex_to_decimal(value):
    pass

def convert_binary_to_hex(value):
    pass

def convert_hex_to_binary(value):
    pass

def main():
    
    try:
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
            is_valid = validate_binary(value)
        elif from_NS == 2:  
            is_valid = validate_decimal(value)
        elif from_NS == 3: 
            is_valid = validate_hex(value)

        if not is_valid:
            print("Invalid value for the chosen Number System.")
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

    except ValueError:
        print("Invalid input. Please enter numbers for Number System choices.")

if __name__ == "__main__":
    main()
