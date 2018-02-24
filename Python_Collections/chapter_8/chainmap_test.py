from collections import ChainMap

user_dict1 = {"a": "hmz1", "b": "hmz2"}
user_dict2 = {"c": "hmz2", "d": "hmz3"}
new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict)

user_dict1 = {"a": "hmz1", "b": "hmz2"}
user_dict2 = {"b": "hmz2", "d": "hmz3"}
new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict.maps)
new_dict.maps[0]["a"] = "hmz"

for key, value in new_dict.items():
    print(key, value)
