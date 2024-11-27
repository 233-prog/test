def main():
    from_NS= input("Choose the current Number System (1 - Binary, 2 - Decimal, 3 - Hexadecimal): ")
    if from_NS not in [1, 2, 3]:
        print("Invalid choice.")
        return

    to_NS = input("Choose the desired Number System (1 - Binary, 2 - Decimal, 3 - Hexadecimal): ")
    if to_NS not in [1, 2, 3]:
        print("Invalid choice.")
        return

    value = input("Enter the value to be converted: ")
    if len(value) < 1 or len(value) > 8:
        print("Invalid input. The value must be between 1 and 8 in length.")
        return
