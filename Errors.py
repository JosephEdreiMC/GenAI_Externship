# Task 1
def exceptions():
    while True:
        try:
            number=float(input('Enter a number: '))
            print(f'100 divided by {number} is {100/number}')
            break
        except ValueError: print('Invalid input! Please enter a valid number.')
        except ZeroDivisionError: print('Oops! You cannot divide by zero.')
exceptions()

# Task 2
def types_exceptions():
    try:
        list=[1,2,3,4]
        print(list[4])
    except IndexError: print('IndexError occurred! List index out of range.')
    try:
        dict_={'a':1, 'b':2, 'c':3}
        print(dict_['d'])
    except KeyError: print('KeyError occurred! Key not found in the dictionary.')
    try:
        print('abc'+123)
    except TypeError: print('TypeError occurred! Unsupported operand types.')
types_exceptions()

# Task 3
def using_try_except():
    while True:
        try:
            num1=float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            result=num1/num2
        except ValueError: print('Invalid input! Please enter a valid number.')
        except ZeroDivisionError: print('The second number cannot be zero!')
        else:
            print(f'The result is {result}.')
            break
        finally: print('This block always executes.')
using_try_except()