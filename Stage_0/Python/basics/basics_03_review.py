### 练习1
# name,years = input().split()
# years = int(years)
# year = 2026
# print(f'{name}，你今年 {year - years} 岁')

### 练习2
# n = input()
# n = n[::-1]
# print(n)

### 拓展A
# n = input()
# if len(n) > 1:
#     n = n[-1] + n[1:-1] + n[0]
#     print(n)
# else:
#     print(n[-1])

### 拓展B
# n = input()
# print(n[:3])
# print(n[-3:])


### 拓展C
name, years = input().split()
year = 2026
years = int(years)
if year - years >= 18:
    print(f'{name}，你今年 {year - years} 岁，已成年')
else:
    print(f'{name}，你今年 {year - years} 岁，未成年')