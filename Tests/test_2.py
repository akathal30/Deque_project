# read the json file
import json

# root_dir=
with open(r'''E:\Ankit\Python\Learning\deque_project\a11y.json''', encoding='utf-8', errors='ignore') as json_data:
    data = json.load(json_data, strict=False)
print(type(data))
violations_list=data['violations']
print(len(violations_list))
print(violations_list)
