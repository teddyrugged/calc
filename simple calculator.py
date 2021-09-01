#creating a simple calculator
first_number = float(input("please enter the first_number: "))
operator = input("enter the operator or sign: ")
second_number = float(input("please enter the second_number: "))

if operator =="+":
    print (first_number + second_number)

elif operator == "-":
    print (first_number - second_number)

elif operator == "*":
    print(first_number * second_number)

elif operator == "/":
    print(first_number / second_number)

else:
    print("invalid operator or sign")