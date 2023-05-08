import json
import os

dir_path = os.path.join(os.getcwd(), 'output')
os.makedirs(dir_path, exist_ok=True)
json_path = os.path.join(dir_path, 'user.json')


user = {
    'name': 'Make',
    'age': 56,
    'is_active': True, 
    'fav_nums': [1,2,3,4,5,6,7],
}
user_str = json.dumps(user)
print(type(user_str))
print(user_str)
