
import json
import os

dir_path = os.path.join(os.getcwd(), 'output')
os.makedirs(dir_path, exist_ok=True)
json_path = os.path.join(dir_path, 'user.json')


User = {
    'name': 'Mike',
    'age': 56,
    'is_active': True,
    'fav_nums': [1,2,3,4,5,6]
    
}

with open(json_path, 'w') as jf:
    # json.dump(User, jf)
    json.dump(User, jf, sort_keys=True, indent=4) #make moore human readble, with a-b sorting of objects and add indentention
    