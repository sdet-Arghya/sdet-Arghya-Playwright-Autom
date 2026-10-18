user_dict = {
    'Name' : 'Dhruti',
    'Age' : '7',
    'City' : 'Brahmapur'
    }
print(user_dict)
#{'Name': 'Dhruti', 'Age': '7', 'City': 'Brahmapur'}
final = (user_dict.get('Age'))
print(final)
#(get function provide the value from key) 7
user_dict.update({'std' : '2nd', 'father' : 'In railways'})
print(user_dict)
#{'Name': 'Dhruti', 'Age': '7', 'City': 'Brahmapur', 'std': '2nd', 'father': 'In railways'}