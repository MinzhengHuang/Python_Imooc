# 元祖
name_tuple = ("hmz1", "hmz2")
for name in name_tuple:
    print(name)

# 拆包
user_tuple = ("hmz", 28, 175)
name, age, height = user_tuple
print(name, age, height)

user_tuple = ("hmz", 28, 175, "nanjing")
name, *other = user_tuple
print(name, other)

# tuple不可变不是绝对的，建议不这样做
name_tuple = ("hmz1", [29, 175])
name_tuple[1].append(22)
print(name_tuple)

user_info_dict = {user_tuple: "hmz"}
print(user_info_dict)

