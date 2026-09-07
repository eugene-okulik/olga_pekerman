my_dict = {
    'tuple': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    'list': ['one', 'two', 'three', 'four', 'five'],
    'dict': {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
        'key5': 'value5',
    },
    'set': {'abc', 13, False, 3.14, 'fffff'}
}
print(my_dict['tuple'][-1])
my_dict['list'].append('six')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'value6'
my_dict['dict'].pop('key1')
my_dict['set'].add('new_value')
my_dict['set'].pop()
              
