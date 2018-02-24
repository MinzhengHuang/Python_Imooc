from collections import namedtuple

User = namedtuple("User", ["name", "age", "height"])
user = User(name="hmz", age="19", height=175)
print(user.name, user.age, user.height)

User = namedtuple("User", ["name", "age", "height", "edu"])
user_tuple = ("hmz2", 29, 176)
user = User(*user_tuple, "master")
print(user.name, user.age, user.height)

User = namedtuple("User", ["name", "age", "height", "edu"])
user_dict = {
    "name": "hmz3",
    "age": 27,
    "height": 164
}
user = User(**user_dict, edu="master")
print(user.name, user.age, user.height)

User = namedtuple("User", ["name", "age", "height", "edu"])
user_tuple = ("hmz4", 24, 146, "master")
user_dict = {
    "name": "hmz4",
    "age": 24,
    "height": 146,
    "edu": "master"
}
user = User._make(user_tuple)
# user = User._make(user_dict)
print(user.name, user.age, user.height)

User = namedtuple("User", ["name", "age", "height", "edu"])
user_tuple = ("hmz5", 25, 145)
user_list = ["hmz5", 25, 145]
user_dict = {
    "name": "hmz5",
    "age": 25,
    "height": 145,
    "edu": "master"
}
user = User(*user_tuple, edu="master")
name, age, *other = user
print(name, age, other)
user_info_dict = user._asdict()
print(user.name, user.age, user.height)
