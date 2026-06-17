numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = numb1 + numb2
elif operator == "-":
    result = numb1 - numb2
elif operator == "*":
    result = numb1 * numb2
elif operator == "/":
    result = numb1 / numb2 if numb2 != 0 else "Error: Division by zero"
else:
    result = "Invalid operator!"
print("Result:", result)
