# W1 D5 第1步提交
# 1. 四个转换函数：int()转化成整数型  float()转化成浮点型  str()转化成字符串 bool()转化成布尔型
# 2. 九个转换结果：
# int("5")   整数5
# int("3.5")   我不确定我猜是整数3
# float("3")   浮点3.0
# str(3.14)    变成字符串3.14
# bool(0)    False
# bool(1)   True
# bool("")   False
# bool("0")    True
# bool("False")    True
# 3. round() 作用：我不知道我几乎没有印象
# 4. round(3.14159, 2)：我不知道我几乎没有印象
# 5. round(2.5) / round(3.5)：我不知道我几乎没有印象

###  bool("0") 是 True，bool("False") 也是 True。只有空字符串 "" 才是 False，任何非空字符串都是 True，哪怕内容是 "0" 或 "False"。这是很多人想当然会错的点。
###  int("3.5") 不是返回 3，是直接报错 ValueError。   原因：int() 只能把“长得像整数的字符串”转成整数，"3.5" 里有小数点，它不认。想从 "3.5" 得到整数，必须先 float("3.5") 变成 3.5，再 int(3.5) 变成 3。

###  round(数字, 小数位数) 用来四舍五入。
###  round(3.14159, 2) → 保留 2 位小数 → 3.14
###  round(3.14159) → 不写第二个参数时，保留到整数 → 3
###  round(3.6) → 4



### 练习1    输入商品价格（小数），输入数量，输出总价（保留 2 位小数）。
# n, nums = input().split()
# n = float(n)
# nums = int(nums)
# print(round(n * nums, 2))


# print(round(2.5))
# print(round(3.5))



### AI补充笔记   四舍六入五取偶
# Python 的 round() 不是“四舍五入”，是“四舍六入五取偶”（也叫银行家舍入，banker's rounding）：
# 当小数部分正好是 .5 时，不往上进，而是向最近的偶数靠：
# round(2.5) → 2（2 是偶数）
# round(3.5) → 4（4 是偶数）
# round(4.5) → 4
# round(5.5) → 6
# 不是 .5 的情况，还是正常四舍五入：
# round(2.4) → 2
# round(2.6) → 3
# 为什么要这么设计？因为处理大量数据时，全部“五入”会让结果整体偏大，银行家舍入能让误差在统计上互相抵消。这是真实工程里的常识，记住它。
# 如果你想做“传统四舍五入”，需要自己处理，或者用 decimal 模块——那是后面的事，今天只要知道 round 有这个特性就行。



###  练习2  输入一个字符串形式的数字列表 "1,2,3,4"，求和。
# n = input().split(',')
# nums = 0
# for i in n:
#     nums += int(i)
# print(nums)


### 拓展A  输入多个商品价格（逗号分隔，如 "3.5,9.99,12"），输出总价，保留 2 位小数。
# n = input().split(',')
# nums = 0
# for i in n:
#     nums += float(i)
# print(round(nums,2))

### 拓展B   输入一个数字列表（逗号分隔），输出平均值，保留 2 位小数。
n = input().split(',')
nums = 0
for i in n:
    nums += float(i)
print(round(nums / len(n), 2))


### 扩展 C  输入一个字符串，输出它的长度和它转换成整数后的两倍。
# n = input()
# print(f'长度 {len(n)}，{2 * int(n)}')