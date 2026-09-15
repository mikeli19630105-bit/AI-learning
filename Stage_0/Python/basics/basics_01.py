## int是整数型  float是浮点型  str是字符串  bool我不知道
## type（）是用来查看类型
## input()得到的是字符串
## 字符串和数字不能直接相加

### 两边类型要匹配。字符串 + 字符串是拼接，数字 + 数字是加法，字符串 + 数字会报 TypeError

### L1 概念解释：bool 是布尔型，表示真 / 假，只有两个值：True 和 False。注意首字母大写，不是字符串 "True"。它常用于条件判断。


##这里是练习1
# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

### 你用了 int()，所以输入 3.5 2 会直接报错。


##这里是练习2
#"5" + 5
#print(type("5"))
#print(type(5))


# W1 D1 第2步-练习②提交
# "5"+5 完整报错：  File "d:\AI-learning\Stage_0\Python\basics\basics_1.py", line 20, in <module>
#     "5" + 5
#     ~~~~^~~
# TypeError: can only concatenate str (not "int") to str
# type("5") 结果：<class 'str'>
# type(5) 结果：<class 'int'>

###  
# 你的白纸解释能抓到“类型不一样”，但还不够精确。
# L1 概念解释：+ 这个符号在不同类型上含义不同。
# 对两个字符串：+ 是拼接
# 对两个数字：+ 是加法
# 一边是 str、一边是 int：+ 不知道按哪种规则做，于是抛 TypeError
# 报错原文 “can only concatenate str (not "int") to str” 意思是：
# 你正在对字符串做拼接，但你给它的另一边不是字符串，而是 int。
# 这句话不需要背，但你要能用自己的话讲清楚：不是 Python 不识别，是 + 对混合类型没有定义好的行为。


##练习3
##题目
# 在练习①的基础上，自己加新需求，至少选 2 个：
# 输出 a ** b
# 输出 a // b
# 输出 a % b
# 输出平均值
# 交换 a 和 b 后，再输出一次和、差、积、商
# 要求：
# 关掉自动补全。
# 不能复制粘贴旧代码后只改一行，要自己重新敲。
# 先自己想清楚每个运算符是什么意思；不懂先记到卡点，不要来问。
# 写完运行一次，确认结果。


##代码
# a, b = map(float, input().split())
# print(a ** b)
# print(a // b)
# print(a % b)
# print((a + b) / 2)
# a, b = b, a
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)




# 今日笔记总结
# W1 D1 第4步提交
# 1. 今天卡在哪：有时候我用了map但是忘记用split（）切割。报错我不太会看，特别是PowerShell的报错我不太理解
# 2. 当时怎么想的：我以为是代码错误，结果是出现了PowerShell报错
# 3. 正确思路：代码逻辑需要多培养
# 4. 今天学到的（bool / type() / input() / 混合类型 + / int与float区别）：bool是判断True和False，int是整数型float是浮点型
# 5. 哪些是凭记忆，哪些是查资料或问 AI：代码的报错是问AI，其他是凭记忆

# W1 D1 第4步-补
# 3. 正确思路（重写，具体到下次怎么做）：用map时需要和split 去匹配。报错要先看最后一行内容，
# TypeError/ValueError 是 python的问题     CategoryInfo/FullyQualifiedErrorId 是PowerShell的问题
# 4. 今天学到的（补全 type() / input() / 混合类型报错 / int与float在除法上的区别）：type是区分类型。input是输入。混合类型报错例如5+“5”数字和字符串。  int与float   /时永远返回浮点型即使可以整除

###  AI补充笔记
# 第 4 条：基本到位，两处再精确一点：
# 混合类型报错
# 你只说了“数字和字符串会报错”。要补上：报错的类型叫 TypeError，报错信息里说的是 can only concatenate str (not "int") to str。记住这个名字，以后看到 TypeError 就往“类型不匹配”上想。
# input()
# 你写“input 是输入”，太浅。要补上：input() 返回的永远是字符串 str，所以想拿数字必须自己用 int() 或 float() 转换。这正是你今天写 map(int/float, ...) 的原因。