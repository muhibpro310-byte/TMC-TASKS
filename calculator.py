num1 = float(input("First number: "))
op = input("Operator (+ - * /): ")
num2 = float(input("Second number: "))

match op:
    case "+": print("Result:", num1 + num2)
    case "-": print("Result:", num1 - num2)
    case "*": print("Result:", num1 * num2)
    case "/": print("Result:", "Error" if num2 == 0 else num1 / num2)
    case _: print("Invalid operator")