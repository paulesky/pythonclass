print("Welcome to my simple calculation")

num = float(input("Enter a valid Number"))

operation = input("Enter an operation (+, -, *, /): ")

num2 = float(input("Enter another valid Number"))

# now let us add the operation

if operation == "+":
    result = num + num2
elif operation == "-":
    result = num - num2
elif operation == "*":
    result = num * num2
elif operation == " /":
    result = num / num2
    
print("The final result is :", result)