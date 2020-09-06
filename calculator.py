a = input().replace('.', '').replace(',', '')
# Check if a is not a number
assert a.isdigit(), 'a must be a number'
operator = input()
operators = ['+', '/', '*', '**', '-']
# Check if operator in list of operators (+, -, *, /, **)
assert operator in operators, 'Operator can be +, -, *, **, /'
b = input().replace('.', '').replace(',', '')
# Check if b is not a number
assert b.isdigit(), 'b must be a number'
answer = eval(a + operator + b)
if answer == int(answer):
    print(int(answer))
else:
    print(answer)
