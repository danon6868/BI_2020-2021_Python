try:
    a = float(input('Enter first number'))
    operator = input()
    operators = ['+', '/', '*', '**', '-']
    b = float(input('Enter second number'))
    if operator not in operators:
        raise ValueError
    if operator == '+':
        if (a + b) == int(a + b):
            print(f'Answer is {int(a + b)}')
        else:
            print(f'Answer is {a + b}')
    elif operator == '-':
        if (a - b) == int(a - b):
            print(f'Answer is {int(a - b)}')
        else:
            print(f'Answer is {a - b}')
    elif operator == '*':
        if (a * b) == int(a * b):
            print(f'Answer is {int(a * b)}')
        else:
            print(f'Answer is {a * b}')
    elif operator == '/':
        if b != 0:
            if (a / b) == int(a / b):
                print(f'Answer is {int(a / b)}')
            else:
                print(f'Answer is {a / b}')
        else:
            print('Zerro division error')
    elif operator == '**':
        if (a ** b) == int(a ** b):
            print(f'Answer is {int(a ** b)}')
        else:
            print(f'Answer is {a ** b}')
except ValueError:
    print('a and b should be integers or floats and operator\
           should be +, -, *, / or **.\
           Please check your input')
