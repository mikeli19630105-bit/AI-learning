#  1. 导入
import math
###  from math import factorial
#  2.基本用法
print(math.factorial(5))   # 120
print(math.factorial(0))   # 1
print(math.factorial(1))   # 1

#  3. 参数要求   math.factorial(n) 的参数 n 必须是非负整数（int）

# math.factorial(-1)   # ValueError: factorial() not defined for negative values
# math.factorial(3.0)  # ValueError: factorial() only accepts integral values

# 4. 返回值
# print(math.factorial(20))  # 2432902008176640000
# print(math.factorial(50))  # 一个很长的整数



# 5. 实际例子
# 计算排列数
# import math

# n = 5
# k = 2
# result = math.factorial(n) // math.factorial(n - k)
# print(result)  # 20


# 计算组合数
# import math

# n = 5
# k = 2
# result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
# print(result)  # 10


# 不过 Python 3.8+ 提供了 math.comb(n, k) 和 math.perm(n, k)，可以直接算组合和排列，更方便：
# print(math.comb(5, 2))  # 10
# print(math.perm(5, 2))  # 20

# 6. 和循环写法的对比
# 自己用循环写阶乘：
# def my_factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# print(my_factorial(5))  # 120
# math.factorial 是 C 实现的，速度更快，而且处理大数也很高效。所以实际开发中优先用它。

