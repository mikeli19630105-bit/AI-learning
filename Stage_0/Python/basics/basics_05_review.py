###  练习①  输入商品价格（小数）和数量，输出总价保留 2 位小数。
# n, nums = input().split()
# print(round(float(n) * int(nums), 2))


###  练习②    输入 "1,2,3,4"，拆分求和。
# n = input().split(',')
# nums = 0
# for i in n:
#     nums += int(i)
# print(nums)

###  扩展 A   输入逗号分隔的价格，输出总价保留 2 位。
# n = input().split(',')
# nums = 0
# for i in n:
#     nums += float(i)
# print(round(nums, 2))


###  扩展 B    输入逗号分隔的数字，输出平均值保留 2 位。
# n = input().split(',')
# nums = 0
# for i in n:
#     nums += float(i)
# print(round(nums / len(n), 2))

###  扩展 C    输入一个字符串，输出长度和它转换成整数后的两倍。
n = input()
print(f'长度 {len(n)}，{int(n) * 2}')