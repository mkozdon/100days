def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def divide(a, b):
    return a / b


operations = {"+": add, "-": sub, "*": multiply, "/": divide}


def new_calc():
    a = int(input(("What's the first number?: ")))
    print("+ - * /")
    op = input("Pick an operation: ")
    b = int(input("What's the second number?: "))
    return [a, b, op]


def calc(params):
    result = operations[params[2]](params[0], params[1])
    print(f"{params[0]} {params[2]} {params[1]} = {result}")
    return result


cont = True
new = True
while new:
    current_value = calc(new_calc())
    while cont:
        user_selection = input(
            f"Type 'y' to continue calculating with {current_value}, or type 'n' to start new calculation, 'q' to quit: "
        )
        if user_selection == "y":
            op = input("Pick an operation: ")
            b = int(input("What's the second number?: "))
            current_value = calc([current_value, b, op])
        elif user_selection == "n":
            cont = False
        elif user_selection == "q":
            cont = False
            new = False
