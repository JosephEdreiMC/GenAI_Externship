inventory=dict()
def inventory_manager():
    while True:
        print('Welcome to the Inventory Manager!')
        print('Current inventory:')
        value_inventory=0
        for item, amounts in inventory.items():
            print('Item: ', item, ', Quantity: ',amounts[0],', Price: $',amounts[1])
            value_inventory += amounts[0]*amounts[1]
            print('Total value of inventory: ',value_inventory)
        action=input("Enter 'a' to add a new item, 'r' to remove an item, 'u' to update the quantity or price of an item, or 'exit' to exit the program. ")
        if action=='a':
            new_item=input('Enter the name of the new item: ')
            new_amount=int(input('Enter the amount: '))
            new_cost=float(input('Entre the cost: '))
            inventory.update({new_item:(new_amount, new_cost)})
        if action=='r':
            remove_item=input('Enter the name of the item to be removed:')
            inventory.pop(remove_item)
        if action=='u':
            item=input('Enter the name of the item to be modified: ')
            new_amount=int(input('Enter the new amount: '))
            new_cost=float(input('Enter the new cost: '))
            inventory[item]=(new_amount, new_cost)
        if action=='exit':
            break
inventory_manager()
