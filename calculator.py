num1 = float(input("please insert the first number: "))
num2 = float(input("please insert the scend number: "))
operation = input("please insert your desired operation among: +, -, *, /, **, %: ")

if operation == "+":
    result = (num1) + (num2)
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = (num1) - (num2)
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = (num1) * (num2)
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    result = (num1) / (num2)
    print(f"{num1} / {num2} = {result}")
elif operation == "**":
    result = (num1) ** (num2)
    print(f"{num1} ** {num2} = {result}")
elif operation == "%":
    result = (num1) % (num2)
    print(f"{num1} % {num2} = {result}")
else:
    result = ("the operation inserted by the user wrong! ")