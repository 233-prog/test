def main():
    from_NS= int(input("Choose the current Number System (1 - Binary, 2 - Decimal, 3 - Hexadecimal): "))
    if from_NS not in [1, 2, 3]:
        print("Invalid choice.")
        return

    to_NS = int(input("Choose the desired Number System (1 - Binary, 2 - Decimal, 3 - Hexadecimal): "))
    if to_NS not in [1, 2, 3]:
        print("Invalid choice.")
        return

    value = input("Enter the value to be converted: ")
    if len(value) <= 1 or len(value) >= 8:
        print("Invalid input. The value must be between 1 and 8 in length.")
        return
    
def validate_binary(value):
    if is_string(value):
        for character in value:
            if character != '0' and character != '1':
                return False
        return True
    else:
        return False

def validate_denary(value):
    if is_string(value):
        for character in value:
            if character not in '0123456789':
                return False
        return True
    else:
        return False

def validate_hex(value):
    if is_string(value):
        hex_chars = '0123456789ABCDEFabcdef'
        for character in value:
            if character not in hex_chars:
                return False
        return True
    else:
        return False

if from_NS == 1:  
        if to_NS == 2: 
            result = convert_binary_to_decimal(value)
        elif to_NS == 3: 
            result = convert_binary_to_hex(value)
        else:
            result = value  
    elif from_NS == 2:  
        if to_NS == 1:  
            result = convert_decimal_to_binary(value)
        elif to_NS == 3: 
            result = convert_decimal_to_hex(value)
        else:
            result = value  
    elif from_NS == 3:  
        if to_NS == 1:  
            result = convert_hex_to_binary(value)
        elif to_NS == 2:  
            result = convert_hex_to_decimal(value)
        else:
            result = value 

if __name__ == "__main__":
    main()

exit()
    def validate_binary(value):
    return value(value) and all(char in '01' for char in value)

def validate_decimal(value):
    return value(value) and all('0' <= char <= '9' for char in value)

def validate_hex(value):
    return value(value) and all(char in "0123456789ABCDEFabcdef" for char in value)

def convert_binary_to_decimal(value):
  
def convert_decimal_to_binary(value):
   
def convert_decimal_to_hex(value):
   
def convert_hex_to_decimal(value):

def convert_binary_to_hex(value): 

def convert_hex_to_binary(value):
