# 定义一个饮料库
drinks = {
    "珍珠奶茶":[9, 1, 2, 8],
    "冰美式":[1, 2, 9, 1],
    "柠檬水":[2, 9, 1, 1],
    "港式奶茶":[8, 1, 3, 9],
    "拿铁":[3, 1, 5, 9],
}

# 你最喜欢的口味
my_taste = [8, 1, 2, 8] # 我喜欢甜、不酸、不苦、奶味重的

# 遍历所有饮料，找出最像的
beat_match = None
best_distance = float('inf')# 无穷大
#'inf' 是 infinity（无穷大）的缩写。

for name, taste in drinks.items():
#     先拿到所有名字，再一个个取
# for name in drinks:           # 拿名字
#     taste = drinks[name]      # 根据名字取对应的列表
#     然后处理 name 和 taste
    distance = 0
    for i in range(4):
        diff = my_taste[i] - taste[i]
        distance = distance + diff * diff
    print(f"{name} 的距离: {distance}")

    if distance < best_distance:
        best_distance = distance
        best_match = name

print(f"\n最推荐你喝: {best_match} (距离： {best_distance})")

