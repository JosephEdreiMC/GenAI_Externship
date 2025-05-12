def empty_entry(string):
    if string=='': raise TypeError('You cannot enter an empty input!')
def valid_option(option):
    if option not in ['1','2','3','4']: raise ValueError('Invalid option! \
    Please enter one of the listed commands')
def new_expense(current_dict):
    while True:
        try:
            description = input('Enter expense description: ')
            empty_entry(description)
        except TypeError as a:
            print(a)
        else:
            try:
                category = input('Enter category: ')
                empty_entry(description)
            except TypeError as b:
                print(b)
            else:
                try:
                    amount = float(input('Enter amount: '))
                    empty_entry(amount)
                except ValueError:
                    print('Invalid amount. Please enter a number.')
                except TypeError as c:
                    print(c)
                else:
                    print('Expense added successfully.')
                    expense = (description, amount)
                    current_dict.setdefault(category, [])
                    current_dict[category].append(expense)
                    break
def view_expenses(data):
    for category in list(data.keys()):
        print('Category: ',category)
        for expense in data[category]:
            print(f'- {expense[0]}: ${expense[1]}')
def view_summary(data):
    print('Summary:')
    totals={}
    for category in list(data.keys()):
        total=0
        for expense in data[category]:
            total+=expense[1]
        totals[category]=total
    for category, total in totals.items():
        print(f'{category}: ${total}')

def finance_tracker(data={}):
    '''
    :param data: Dictionary. Category:list((description, item)) format
    '''
    finances=data # Accepts a predefined dictionary
    print('Welcome to the Personal Finance Tracker!')
    while True:
        print('What would you like to do?')
        print('1. Add Expense')
        print('2. View All Expenses')
        print('3. View Summary')
        print('4. Exit')
        try:
            option=input('Choose an option: ')
            valid_option(option)
        except ValueError as a:
            print(a)
        else:
            if option=='1':
                new_expense(data)
            elif option=='2':
                view_expenses(data)
            elif option=='3':
                view_summary(data)
            else:
                print('Goodbye!')
                break
    return data
balance_log=finance_tracker()
# Uncomment the lines below to save the produced transactions dictionary:
# import pickle
# with open("expenses.pkl", "wb") as file:
#     pickle.dump(balance_log, file)

