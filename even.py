def decimal_to_binary(decimal_num):

    if decimal_num == 0:
        return "0"

    binary_num = ""
    decimal_value = int(decimal_num) 
    binary_str = ""
    while decimal_value > 0:
        remainder = decimal_value % 2
        binary_str = binary_str + str(remainder)
        decimal_value = decimal_value // 2 
    return binary_num 

def check_even_odd(binary_num):
  
    last_digit = binary_num[-1]
    if last_digit == '0':
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    decimal_num = int(input("Enter an integer: "))
    binary_num = decimal_to_binary(decimal_num)
    print(f"The number {decimal_num} is {check_even_odd(binary_num)}.")