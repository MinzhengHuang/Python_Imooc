from collections import deque

user_list = ["hmz", "hmz2"]
use_name = user_list.pop()
print(use_name, user_list)

# deque GIL是线程安全的，list不是线程安全的
# user_list = deque(("hmz1", "hmz2"))
user_list = deque(["hmz1", "hmz2"])
print(user_list)

user_deque = deque(["hmz1", 29, 175])
user_deque.appendleft("hmz2")
print(user_deque)

user_deque = deque(["hmz1", 29, 175])
user_deque2 = user_deque.copy()
user_deque2[1] = "hmz3"
print(user_deque, user_deque2)
print(id(user_deque), id(user_deque2))
print(user_deque)

user_deque = deque(["hmz1", ["hmz2", "hmz3"], "hmz3"])
user_deque2 = user_deque.copy()
user_deque2[1].append("hmz1")
print(user_deque, user_deque2)
print(id(user_deque), id(user_deque2))
print(user_deque)

user_deque = deque(["hmz1", ["hmz2", "hmz3"], "hmz3"])
import copy

user_deque2 = copy.deepcopy(user_deque)
user_deque2[1].append("hmz1")
print(user_deque, user_deque2)
print(id(user_deque), id(user_deque2))
print(user_deque)

user_deque = deque(["hmz1", "hmz2", "hmz3"])
user_deque2 = deque(["hmz11", "hmz22", "hmz33"])
user_deque.extend(user_deque2)
print(user_deque, user_deque2)
print(id(user_deque), id(user_deque2))
print(user_deque)

user_deque = deque(["hmz1", "hmz2", "hmz3"])
user_deque.insert(0, "hmz2")
print(user_deque)

user_deque = deque(["hmz1", "hmz2", "hmz3"])
user_deque.reverse()
print(user_deque)
