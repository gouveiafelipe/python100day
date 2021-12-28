from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
      "-": subtract,
      "*": multiply,
      "/": divide
}


def calculator():
    print(logo)
    stop_calculator = True

    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    while stop_calculator:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f" {num1} {operation_symbol} {num2}  = {answer}")
        if input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator:  ") == "y":
            num1 = answer
        else:
            stop_calculator = False
            calculator()


calculator()