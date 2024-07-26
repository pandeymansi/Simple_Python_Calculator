# import os
# Operations that are to be performed
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def division(a, b):
    return a/b

# Assigning a dictionary to fetch symbols/keys
operations_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}

def calculator():
    # To print only keys in the dictionary
    number1 = float(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)
    
    continue_flag = True
    while continue_flag:
        op_symbol = input("Pick an operation: ")
        number2 = float(input("Enter next number: "))  
        calculator_function = operations_dict[op_symbol]
        output = calculator_function(number1, number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        
        should_continue = input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation else 'x' to exit: ").lower()
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag = False
            # os.system('cls')
            calculator()             # Recursion
        else:
            continue_flag = False
            print("Bye")
calculator()
            