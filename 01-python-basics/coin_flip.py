import random

# ============================
# 模拟抛硬币：验证大数定律
# ============================

# 模拟抛硬币
# random.random() 产生 0 到 1 之间的随机小数
# 如果小于 0.5，算正面；否则反面
def flip_coin():
    if random.random() < 0.5:
        return "正面"
    else:
        return "反面"

# 抛 10 次，看看正面出现的比例
heads_count = 0
total = 10

for i in range(total):
    result = flip_coin()
    if result == "正面":
        heads_count += 1

print(f"抛 {total} 次，正面 {heads_count} 次，比例：{heads_count / total :.2f}")

# 抛 1000 次
heads_count = 0
total = 1000
for i in range(total):
    if flip_coin() == "正面":
        heads_count += 1

print(f"抛 {total} 次，正面 {heads_count} 次，比例：{heads_count / total :.4f}")

# 抛 100000 次
heads_count = 0
total = 100000

for i in range(total):
    if flip_coin() == "正面":
        heads_count += 1

print(f"抛 {total} 次，正面 {heads_count} 次，比例: {heads_count/total:.6f}")