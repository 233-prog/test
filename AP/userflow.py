def main():
    # Taking user input 
    from_NS = input("Enter the current number system (1 - Binary, 2 - Decimal, 3 - Hexadecimal): ")
    to_NS = input("Enter the number system to covert to (1 - Binary, 2 - Decimal, 3 - Hexadecimal): ")
    
    # =validation
    while True:
        value = input("Enter the value to be converted (1 to 8 characters long): ")
        if 1 <= len(value) <= 8:
            break
        else:
            print("Invalid input: value length must be between 1 and 8 characters.")


            def is_string(value):

    return isinstance(value, str)

def validate_binary(value):
    return is_string(value) and all(char in '01' for char in value)

def validate_decimal(value):
    return is_string(value) and all('0' <= char <= '9' for char in value)

def validate_hex(value):
    return is_string(value) and all(char in "0123456789ABCDEFabcdef" for char in value)

def convert_binary_to_decimal(value):
  

def convert_decimal_to_binary(value):
   
def convert_decimal_to_hex(value):
   
def convert_hex_to_decimal(value):
  

def convert_binary_to_hex(value):
 

def convert_hex_to_binary(value):
   

            
    # Print 
    print(f"From Number System: {from_base}")
    print(f"To Number System: {to_base}")
    print(f"Value: {value}")

if __name__ == "__main__":
    main()
