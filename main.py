# comparing 2 numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("The larger number is:", larger_number)

# comparing 3 numbers:

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("The largest number is: ", largest_number)

# using max method: (min() method for lowest num)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = max(number1, number2, number3)

print("The largest number is: ", largest_number)
