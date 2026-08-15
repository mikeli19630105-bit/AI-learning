# 我们先用 Python 最基础的功能：列表（list）
# 列表就是一排有顺序的东西，用方括号括起来

# 定义三杯饮料
pearl_milk_tea = [9, 1, 2, 8]# 珍珠奶茶：[甜, 酸, 苦, 奶]
iced_americano = [1, 2, 9, 1]# 冰美式
lemonade = [2, 9,  1, 1]# 柠檬水

# 打印出来看看
print("珍珠奶茶",pearl_milk_tea)
print("冰美式",iced_americano)
print("柠檬水",lemonade)

# 现在我们来回答一个问题：珍珠奶茶和冰美式，有多不一样？
# 最简单的办法：对应位置相减，看看差多少
difference = []
for i in range(4):# range(4) 产生 0,1,2,3
    diff = pearl_milk_tea[i] - iced_americano[i]
    difference.append(abs(diff))# abs 是取绝对值，只看差多少，不看方向

print("每一维度的差距：", difference)

# 总差距就是把所有差距加起来
total_difference = sum(difference)
print("珍珠奶茶何冰美式的总差距：", total_difference)

# 你自己试试：计算珍珠奶茶和柠檬水的差距
# （在下面写你的代码）