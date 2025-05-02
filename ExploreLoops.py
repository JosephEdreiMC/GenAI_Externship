#  Task 1
def count_down():
    number=int(input('Enter the starting number: '))
    while number >0:
        print(number)
        number -=1
        if number == 0: print('Blast off!')
count_down()
# Task 2
def multiplication_table():
    number=int(input('Enter a number: '))
    for i in range(1,11): print(f'{number} x {i} = {number*i}')
multiplication_table()
# Task 3
def factorial():
    number=int(input('Enter a number: '))
    result=1
    for i in range(1, number+1): result *=i
    print(f'The factorial of {number} is {result}.')
factorial()

