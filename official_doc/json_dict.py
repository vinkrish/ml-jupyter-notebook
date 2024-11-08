import json

person_dict = {
    'name': 'Alice',
    'age': 30,
    'hobbies': ['reading', 'cycling'],
    'is_active': True
}

# Convert dictionary to JSON string
person_json = json.dumps(person_dict)
print(person_json)
# Output: '{"name": "Alice", "age": 30, "hobbies": ["reading", "cycling"], "is_active": true}'

# Convert JSON string to dictionary
person_dict_new = json.loads(person_json)
print(person_dict_new)
# Output: {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'cycling'], 'is_active': True}

print(type(person_json))
print(type(person_dict_new))
