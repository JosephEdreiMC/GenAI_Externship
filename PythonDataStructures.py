# Task 1
fruits= ['apple', 'banana', 'cantaloupe', 'date', 'fig', 'grape', 'jackfruit']
fruits.append('kiwi')
fruits.remove('apple')
print(fruits[::-1])
# Task 2
info={'name': 'John Smith','age':25, 'city': 'New York'}
info.update({'favorite color':'blue'})
info['city']='Seattle'
print('Keys:  Values:')
for key, value in info.items():
    print(key,',',value)
# Task 3
favorites=('The Ghost Writer',"Eye of the Tiger", 'The Lord of the Rings')
# favorites[0]='Frozen' # It returns an error, so it's a comment
print('Length of tuple: ',len(favorites))

