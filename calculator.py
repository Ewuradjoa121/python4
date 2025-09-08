print("Simple Calculator")
print("Choose operation: +, -, *, /")

operation = input("Enter operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "+":  
    print("Result:", num1 + num2)

else:
    if operation == "-":
        print("Result:", num1 - num2)

    else:
        if operation == "*":
            print("Result:", num1 * num2)

        else:
            if operation == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid operation")