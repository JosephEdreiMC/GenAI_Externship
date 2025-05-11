# Task 1
def greet_user(name):
    print('Hello, '+ name+'! Welcome aboard.')
greet_user('Alice')
def add_numbers(num1, num2):
    return num1+num2
num1, num2 = 5,10
print(f'The sum of {num1} and {num2} is {add_numbers(num1, num2)}')

# Task 2
def describe_pet(pet_name:str, animal_type='dog'):
    print(f'I have a {animal_type} named {pet_name}.')
describe_pet('Buddy')
describe_pet('Whiskers','cat')

# Task 3
def make_sandwich(*args):
    print('Making a sandwich with the following ingredients: ')
    for i in args:
        print(' - '+i)
make_sandwich('Lettuce','Tomato','Cheese')

# Taks 4
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=5
print(f'Factorial of {n} is {factorial(n)}.')
def fibonacci(n):
    if n==1: return 1
    elif n==2: return 1
    else: return fibonacci(n-2)+fibonacci(n-1)
n=6
print(f'The {n}th Fibonacci number is {fibonacci(n)}.')