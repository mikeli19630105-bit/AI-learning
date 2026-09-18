# 练习①：秒数换算 X小时X分X秒

# seconds = int(input())
# hours, minutes = 0, 0
# minutes = seconds // 60
# hours = minutes // 60
# minutes = minutes % 60
# seconds = seconds % 60
# print(f"{hours}小时{minutes}分{seconds}秒")


# 练习②：三位数各位之和

# nums = int(input())
# a = nums % 10
# nums = nums // 10
# b = nums % 10
# nums = nums // 10
# sums = a + b + nums
# print(sums)

# 扩展 A：三位数反转

# nums = int(input())
# a = nums % 10 * 100
# nums = nums // 10
# b = nums % 10 * 10
# nums = nums // 10
# sums = a + b + nums
# print(a + b + nums)

# 扩展 B：秒数换算 X天X小时X分X秒

seconds = int(input())
days, hours, minutes = 0, 0, 0
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
hours = hours % 24
minutes = minutes % 60
seconds = seconds % 60
print(f"{days}天{hours}小时{minutes}分{seconds}秒")