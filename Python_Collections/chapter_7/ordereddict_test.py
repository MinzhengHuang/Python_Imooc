from collections import OrderedDict

user_dict = OrderedDict()
user_dict["b"] = "hmz2"
user_dict["a"] = "hmz1"
user_dict["c"] = "hmz3"
print(user_dict)
print(user_dict.popitem())
print(user_dict)
print(user_dict.move_to_end("b"))
print(user_dict)
