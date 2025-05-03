# Task 1
def slicing_and_indexing():
    string="Python is amazing!"
    print('First word: '+string[:6])
    print('Amazing part: ' + string[-8:-1])
    print('Reversed string: ' + string[::-1])
slicing_and_indexing()
# Task 2
def string_methods():
    string_1=" hello, python world! "
    print(string_1.strip())
    print(string_1.capitalize())
    print(string_1.replace('world', 'universe'))
    print(string_1.upper())
string_methods()
# Task 3
def palindrome():
    string1=input('Enter a word: ')
    if string1 == string1[::-1]:
        print(f'Yes, \'{string1}\' is a palindrome!')
palindrome()