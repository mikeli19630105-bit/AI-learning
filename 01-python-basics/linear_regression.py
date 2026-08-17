# Day 5: 什么是"学习"？—— 让 AI 自己找到身高和体重的规律
# 数据：身高和体重（真实值）
data = [
    (160, 55),
    (170, 65),
    (180, 75),
    (165, 60),
    (175, 70)
]

# AI 一开始随机猜一个公式：体重 = a * 身高 + b
# 我们让 a=0, b=0 开始（完全不懂）
a = 0.0
b = 0.0

# 学习率：每次调整多少（步子大小）
learning_rate = 0.0001

# 让 AI 猜 1000 次，每次根据误差调整
for epoch in range(1000):
    total_error = 0

    for height, true_weight in data:
        # 1. AI 的猜测
        guess = a * height + b

         # 2. 计算误差（猜得怎么样？）
        error = guess - true_weight
        
        # 3. 调整 a 和 b（这就是"学习"！）
        # 如果猜高了，就减小 a 和 b；猜低了，就增大
        a = a - learning_rate * error * height
        b = b - learning_rate * error

        total_error = total_error + abs(error)

    # 每 100 轮打印一次进度
    if epoch % 100 == 0:
       print(f"第 {epoch} 轮： a={a:.4f}, b={b:.4f}, 总误差={total_error:.2f}")

print(f"\n最终模型： 体重 = {a:.4f} * 身高 + {b:.4f}")
print("真实规律大概是： 体重 = 1 * 身高 - 105")

# 预测一个 172cm 的人
prediction = a * 172 + b
print(f"预测 172cm 的人体重： {prediction:.2f} kg")
