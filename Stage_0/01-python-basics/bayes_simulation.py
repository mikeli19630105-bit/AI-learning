import random

# ============================
# 贝叶斯推断模拟：检测阳性，真有病的概率是多少？
# ============================

population = 10000    # 1万人
disease_rate = 0.01   # 患病率 1%
test_accuracy = 0.99  # 有病的99%测出阳性
false_positive = 0.01 # 没病的1%误报

# 统计变量
has_disease = 0        # 实际患病人数
test_positive = 0      # 检测阳性总人数
true_positive = 0      # 真阳性（有病且测出阳性）

# 模拟每个人
for i in range(population):
    # 1. 这个人有没有病？
    sick = random.random() < disease_rate

    if sick:
        # 2. 真的有病
        has_disease += 1

        # 3. 检测：99% 概率阳性
        if random.random() < test_accuracy:
            test_positive += 1
            true_positive += 1
    else:
        # 2. 没有病
        # 3. 检测：1% 概率假阳性
        if random.random() < false_positive:
            test_positive += 1

# 打印结果
print("=" * 40)
print("贝叶斯推断模拟结果")
print("=" * 40)
print(f"总人数：{population}")
print(f"实际患病人数：{has_disease}")
print(f"检测阳性总人数：{test_positive}")
print(f"真阳性（有病且测出）：{true_positive}")
print(f"假阳性（没病但测出）：{test_positive - true_positive}")
print(f"如果检测阳性，真正有病的概率：{true_positive / test_positive:.4f}")
print("-" * 40)

if test_positive > 0:
    probability = true_positive / test_positive
    print(f"如果检测阳性，真正有病的概率: {probability:.4f}")
    print(f"≈ {probability * 100:.2f}%")
else:
    print("没有检测阳性的人")