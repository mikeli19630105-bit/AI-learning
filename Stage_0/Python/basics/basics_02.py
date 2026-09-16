###  练习1   输入秒数，换算成 “X 小时 X 分 X 秒”。

# hours, minutes = 0, 0
# second = int(input())

# minutes = second // 60
# hours = minutes // 60
# minutes = minutes % 60
# second = second % 60
# print(f"{hours}小时 {minutes}分 {second}秒")

### 练习2   输入一个三位数，输出各位数字之和。

# n = int(input())
# a = n % 10
# n = n // 10
# b = n % 10
# n = n // 10
# c = n % 10
# print(a + b + c)

 
### 练习3   扩展 A    输入一个三位数，输出它的反转数。
### 练习3   扩展 B    在练习①基础上，把秒数换算升级到“天”。

# n = int(input())
# a = n % 10
# n = n // 10
# b = n % 10
# c = n // 10
# nums = a * 100 + b * 10 + c
# print(nums)


second = int(input())
days, hours, minutes= 0, 0, 0
minutes = second // 60
hours = minutes // 60
days = hours // 24
hours = hours % 24
minutes = minutes % 60
second = second % 60

print(f"{days}天 {hours}小时 {minutes}分 {second}秒")
