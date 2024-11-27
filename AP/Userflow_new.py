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
    return value(value) and all(char in '01' for char in value)

def validate_decimal(value):
    return value(value) and all('0' <= char <= '9' for char in value)

def validate_hex(value):
    return value(value) and all(char in "0123456789ABCDEFabcdef" for char in value)


if __name__ == "__main__":
    main()
