### 练习①
### 输入一句话，统计空格个数和单词个数。
# n = input()
# m = n.split()
# num = 0
# for _ in m:
#     num += len(_)
# print(f'空格个数:{len(n) - num}单词个数:{len(m)}')

###  练习②   输入一个文件名，去掉首尾空格并转小写。
# n = input().strip().lower()
# print(n)



### 扩展 A   输入一句话，把所有空格替换成 -
# n = input().replace(' ','-')
# print(n)


### 扩展 B    输入一句逗号分隔的话，拆开后用 | 连起来。
# n = input().split(',')
# print('|'.join(n))

###  扩展 C   输入一句话，输出大写形式和小写形式各一行。
n = input()
print(n.upper())
print(n.lower())
