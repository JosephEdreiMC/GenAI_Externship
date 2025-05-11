# Auxiliary functions
def factorial(n):
    if n==1: return 1
    else: return n*factorial(n-1)
def fibonacci(n):
    if n==1: return 1
    elif n==2: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)
def menu_recursions():
    while True:
        option=input('Choose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Exit: ')
        try: isinstance(int(option), int) and int(option) in [1,2,3]
        except:
            print('Make sure to choose a valid option (1, 2, or 3).')
            continue
        if int(option)==1:
            number=input('Enter a number to find its factorial: ')
            try: isinstance(int(number), int)
            except:
                print('You need to enter a positive integer')
                continue
            print(f'The factorial of {int(number)} is {factorial(int(number))}')
        elif int(option)==2:
            number=input('Enter the position of the Fibonacci number: ')
            try: isinstance(int(number), int)
            except:
                print('You need to enter a positive integer')
                continue
            print(f'The {int(number)}th Fibonacci number is {fibonacci(int(number))}')
        elif int(option) ==3: break
        else: print('Make sure to choose a valid option (1, 2, or 3).')
menu_recursions()
