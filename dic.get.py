dict = {
    'name' : 'mohan',
    'age' : 20,
    'city' : 'Bihar',
    'country' : 'India'
}

# print(dict['name'])
# print('city' in dict)

dict['siwan'] = 'wet'
# print(dict['siwan'])

print(dict.get('age','N/A')) #present in dictionary
print(dict.get('dictr','N/A'))# not present in dict

del dict['siwan']
print(dict.get('siwan','N/A'))