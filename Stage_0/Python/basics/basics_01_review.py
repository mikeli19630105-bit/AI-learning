a, b = map(float, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)
print(a % b)
print((a + b) / 2)

a, b = b, a
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)
print(a % b)
print((a + b) / 2)


## 下面是AI补充材料   我的易错点
### // 更准确叫向下取整除法（floor division）。-7 // 2 不是 -3，而是 -4，因为它向下取整，不是简单截断。
### ** 不只平方，是幂运算。a ** b 是 a 的 b 次方，b 可以是 3、0.5、负数，不只是 2。