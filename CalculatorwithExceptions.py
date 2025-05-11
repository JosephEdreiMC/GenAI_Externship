def calculator_exceptions():
    print("Welcome to the Error-Free Calculator!")
    while True:
        print()
        def invalid_command(n):
            if n not in ['1','2','3','4','5']:
                raise ValueError('The entered command is not valid!')
        try:
            operation=input("Choose an operation: "
                "1. Addition 2. Subtraction 3. Multiplication 4. Division 5. ")
            invalid_command(operation)
        except ValueError as e:
            print(e)
        if operation in ['1','2','3']:
            try:
                num1=float(input('Enter the first number: '))
                num2=float(input('Enter the second number: '))
                add, subtract, multi = num1+num2, num1-num2, num1*num2
            except ValueError: print('Invalid input! Please enter a valid number.')
            else:
                if operation =='1': print(f'The sum of {num1} and {num2} is {add}')
                if operation == '2': print(f'The subtraction of {num1} and {num2} is {subtract}')
                if operation == '3': print(f'The multiplication of {num1} and {num2} is {multi}')
        elif operation == '4':
            try:
                num1=float(input('Enter the first number: '))
                num2=float(input('Enter the second number: '))
                divide=num1/num2
            except ValueError: print('Invalid input! Please enter a valid number.')
            except ZeroDivisionError: print('Oops! Division by zero is not allowed.')
            else: print(f'The division of {num1} and {num2} is {divide}')
        elif operation =='5':
            print('Goodbye!')
            break


calculator_exceptions()