from collections import Counter

users = ["hmz1", "hmz2", "hmz3", "hmz1", "hmz2", "hmz2"]
user_counter = Counter(users)
print(user_counter)

users = ["hmz1", "hmz2", "hmz3", "hmz1", "hmz2", "hmz2"]
user_counter = Counter("skjhdasdh")
print(user_counter)

users = ["hmz1", "hmz2", "hmz3", "hmz1", "hmz2", "hmz2"]
user_counter = Counter("skjhdasdh")
user_counter.update("hsmz")
print(user_counter)

users = ["hmz1", "hmz2", "hmz3", "hmz1", "hmz2", "hmz2"]
user_counter = Counter("skjhdasdh")
user_counter2 = Counter("hmz")
user_counter.update(user_counter2)
print(user_counter)

users = ["hmz1", "hmz2", "hmz3", "hmz1", "hmz2", "hmz2"]
user_counter = Counter("skjhdasdh")
user_counter2 = Counter("hmz")
user_counter.update(user_counter2)
print(user_counter.most_common(2))
print(user_counter)
