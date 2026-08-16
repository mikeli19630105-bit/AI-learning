pearl = [9, 1, 2, 8]
hk_milk_tea = [8, 1, 3, 9]

# 计算"距离"的平方
distance_squared = 0
for i in range(4):
    diff = pearl[i] - hk_milk_tea[i]
    distance_squared = distance_squared + diff * diff

print("距离平方", distance_squared)