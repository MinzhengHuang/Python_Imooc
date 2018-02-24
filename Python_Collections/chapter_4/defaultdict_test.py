from collections import defaultdict

user_dict = {}
users = ["hmz1", "hmz2", "hmz3", "hmz1", "hmz2", "hmz2"]
for user in users:
    user_dict.setdefault(user, 0)
    user_dict[user] += 1
print(user_dict)


default_dict = defaultdict(int)
users = ["hmz1", "hmz2", "hmz3", "hmz1", "hmz2", "hmz2"]
for user in users:
    defaultdict[user] += 1
print(user_dict)
