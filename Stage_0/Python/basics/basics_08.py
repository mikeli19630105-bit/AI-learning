###  W2 · D2 任务卡：for + range、break/continue

for i in range(1, 101):
    if i % 7 == 0:
        print(i)


### 列表推导式基本格式   [表达式 for 变量 in 可迭代对象 if 条件]

# nums = [i for i in range(1, 100) if i % 7 == 0]
# print(nums)


# print(*[i for i in range(1, 100) if i % 7 == 0], sep="\n")
###  * —— 解包（unpacking）    前面的 * 把这个列表“拆开”，变成多个独立的位置参数传给 print
###  sep —— 分隔符    
# print 函数可以一次打印多个值，默认它们之间用空格隔开：
# print(1, 2, 3)        # 输出：1 2 3
# sep 是 print 的一个关键字参数，用来指定这些值之间的分隔符。
# 这里 sep="\n" 表示用换行符 \n 作为分隔符：
# print(1, 2, 3, sep="\n")

### 任务 2：计算 n!
print('请输入 n：')
n = int(input())
nums = 1
for i in range(1, n + 1):# 娶不到右边的括号
    nums *= i
print(f'{n}! = {nums}')


### 任务 3（break/continue 专项）
for i in range(1,21):
    if i % 3 == 0:
        continue
    if i > 15:
        break
    print(i)

###  变式 1
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


### 变式 2

n = int(input())
total = 0
for i in range(1, n + 1):
    nums = 1
    for j in range(1, i + 1):
        nums *= j
    print(f"nums = {nums}")
    total += nums
    print(f'total = {total}')

###  变式 3
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)