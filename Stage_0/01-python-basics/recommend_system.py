# ============================
# 奶茶推荐系统 v1.0
# ============================

# 1. 定义饮料数据库（名称 -> [甜, 酸, 苦, 奶]）
drinks = {
    "珍珠奶茶": [9, 1, 2, 8],
    "冰美式": [1, 2, 9, 1],
    "柠檬水": [2, 9, 1, 1],
    "港式奶茶": [8, 1, 3, 9],
    "拿铁": [3, 1, 5, 9],
    "抹茶拿铁": [5, 1, 4, 8],
    "乌龙茶": [2, 2, 6, 2],
    "草莓奶昔": [9, 3, 1, 9],
}

# 2. 计算两个向量的距离（欧几里得距离的平方）
def distance(v1, v2):
    total = 0
    for i in range(len(v1)):
        diff = v1[i] - v2[i]
        total = total + diff * diff
    return total

# 3. 推荐函数：根据用户喜好，推荐最像的3款
def recommend(user_taste, top_n = 3):
    results = []
    for name, taste in drinks.items():
        d = distance(user_taste, taste)
        results.append((d, name))

    # 按距离排序（从小到大，距离越小越像）
    results.sort()

    print("\n=== 推荐结果 ===")
    for i in range(min(top_n, len(results))):
        d, name = results[i]
        print(f"{i + 1}. {name} (距离： {d:.2f})")

# 4. 运行！
print("欢迎来到奶茶推荐系统！")
print("请给以下维度打分（0-10）：")

# 用 float() 接收输入，支持小数
sweet = float(input("你喜欢多甜？（0=不甜，10=超甜）:"))
sour = float(input("你喜欢多酸？（0=不酸，10=超酸）:"))
bitter = float(input("你喜欢多苦？（0=不苦，10=超苦）:"))
milk = float(input("你喜欢奶味多重？（0=没有，10=超浓）:"))

my_taste = [sweet, sour, bitter, milk]
recommend(my_taste)