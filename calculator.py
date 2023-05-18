"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


quit = False
while quit == False:
    print("Enter an equation: ")
    input_string = input('> ')
    tokens = input_string.split(' ')
    
    if tokens[0] == "+":
        print(add(int(tokens[1]), int(tokens[2])))
    elif tokens[0] == "-":
        print(subtract(int(tokens[1]), int(tokens[2])))
    elif tokens[0] == "*":
        print(multiply(int(tokens[1]), int(tokens[2])))