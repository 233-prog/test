def main():
    # Taking user input 
    from_base = int(input("Enter the current number system (1 - Binary, 2 - Decimal, 3 - Hexadecimal): "))
    to_base = int(input("Enter the number system to covert to (1 - Binary, 2 - Decimal, 3 - Hexadecimal): "))
    
    # =validation
    while True:
        value = input("Enter the value to be converted (1 to 8 characters long): ")
        if 1 <= len(value) <= 8:
            break
        else:
            print("Invalid input: value length must be between 1 and 8 characters.")
            
    # Print 
    print(f"From Number System: {from_base}")
    print(f"To Number System: {to_base}")
    print(f"Value: {value}")

if __name__ == "__main__":
    main()
