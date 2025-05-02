# Task 1
def welcome_message(name='John', age = 25, height=5.9):
    print(f'Hello, my name is {name}! Glad to be here! I\'m {age} and {height} feet tall')
welcome_message()
# Task 2
import random
def operations(num1 = random.randint(0,11), num2 = random.randint(1,11)):
    print(f'The sum of {num1} and {num2} is ', num1+num2)
    print(f'{num1} minus {num2} is ', num1-num2)
    print(f'{num1} times {num2} is ', num1*num2)
    print(f'{num1} divided by {num2} is ', num1/num2)
operations()
# Task 3
def number_checker():
    number=float(input('Please, enter a number: '))
    if number>0:
        print("This number is positive. Awesome!")
    elif number<0:
        print("This number is negative. Better luck next time!")
    else:
        print("Zero it is. A perfect balance!")
number_checker()

