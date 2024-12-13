def even(num):

  if num == 0:
    return True

  while num > 1:
    num = num >> 1

  return num == 0

number = int(input("Enter an integer: "))

if even(number):
  print(number, "is even")
else:
  print(number, "is odd")