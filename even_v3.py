def even(value):
    if value == 0:
        return True
    
    while value > 0:
        value = value - 2
        
    return value == 0

number = int(input("Enter an integer: "))
if even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")