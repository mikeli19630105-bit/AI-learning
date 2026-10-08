### 任务一

# print('请输入成绩：')

# n = int(input())
# if 100 >= n >= 90:
#     print('优')
# elif 89 >= n >= 80:
#     print('良')
# elif 79 >= n >= 70:
#     print('中')
# elif 69 >= n >= 60:
#     print('及格')
# else:
#     print('不及格')

### 任务二
# print('请输入第1个数：')
# num1 = int(input())
# print('请输入第2个数：')
# num2 = int(input())
# print('请输入第3个数：')
# num3 = int(input())

# if num2 > num1:
#     num1 = num2
# if num3 > num1:
#     num1 = num3
# print(f'最大值是：{num1}')


### 变式 1：给成绩等级加无效输入判断
print('请输入成绩：')

n = int(input())
if n < 0 or n > 100:
    print('成绩无效')
elif 100 >= n >= 90:
    print('优')
elif 89 >= n >= 80:
    print('良')
elif 79 >= n >= 70:
    print('中')
elif 69 >= n >= 60:
    print('及格')
else:
    print('不及格')



### 变式 2：三个数最大值，不修改原变量
a, b, c = map(int,input().split())
# print(max(a,b,c))  #max  用法

if a >= b and a >= c:
    print(f'最大值是：{a}')
elif b >= a and b >= c:
    print(f'最大值是：{b}')
else:
    print(f'最大值是：{c}')