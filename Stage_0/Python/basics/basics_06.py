###  项目需求   
###  循环接收输入，支持 + - * /，输入 q 退出；除数为 0 时打印提示而不是崩溃。
###  在上面基础上加了history，history不会中断运算，可以继续运算


#两数加减乘除运算
# history = []
# while True:
#     m = input()
#     n = m.replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ').split()
#     if n == []:
#         print('输入不合法')
    
#     else:
#         if n[0] == 'history':
#             if history == []:
#                 print('暂无历史')
#             else:
#                 print(history)

#         if n[0] == 'q':
#             break
#         if n[0] != 'history':
#             if len(n) == 1:
#                 print('输入不合法')
#             elif n[1] == '+':
#                 Cal_result = float(n[0]) + float(n[2])
#                 print(Cal_result)
#                 Result = m + ' = ' + str(Cal_result)
#                 history.append(Result)
#             elif n[1] == '-':
#                 Cal_result = float(n[0]) - float(n[2])
#                 print(Cal_result)
#                 Result = m + ' = ' + str(Cal_result)
#                 history.append(Result)
#             elif n[1] == '*':
#                 Cal_result = float(n[0]) * float(n[2])
#                 print(Cal_result)
#                 Result = m + ' = ' + str(Cal_result)
#                 history.append(Result)
#             elif n[1] == '/':
#                 if n[2] == '0':
#                     print('除数不能为0')
#                 else:
#                     Cal_result = float(n[0]) / float(n[2])
#                     print(Cal_result)
#                     Result = m + ' = ' + str(Cal_result)
#                     history.append(Result)
#             else:
#                 print('输入不合法')
# print('out')






### 加强版连续运算
# history = []

# while True:
#     n = input().replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ').split()
#     str1 = ' '.join(n)#用来写history
#     list1 = []#用来记符号
#     list2 = []#用来记需要运算的数字
#     result = 0#用来记忆计算结果
#     real_num = True
#     if n == []:#输入空字符不合法
#         print('输入不合法')
    
#     else:
#         if len(n) == 1 and n[0] == 'q':#用来退出
#             break
#         elif len(n) % 2 == 0 and n != []:#数字加符号一定是奇数否则不合法
#             print('输入不合法')
#         elif n[0] == 'history':
#             if history == []:
#                 print('暂无历史')
#             else:
#                 print(history)
        
#         else:
#             for i in range(1,len(n),2):
#                 list1.append(n[i])
#             for i in range(0,len(n),2):
#                 list2.append(n[i])
        
            
#             if list2[0].isdigit():
#                 result = float(list2[0])
#             for i in range(0,len(list1)):#通过符号来计算
#                 if list2[i + 1].isdigit():
#                     if list1[i] == '+':
#                         result += float(list2[i + 1])
#                     elif list1[i] == '-':
#                         result -= float(list2[i + 1])
#                     elif list1[i] == '*':
#                         result *= float(list2[i + 1])
#                     elif list1[i] == '/':
#                         if list2[i + 1] == '0':
#                             print('除数不能为0')
#                             real_num = False
#                         else:
#                             result /= float(list2[i + 1])
#                     else:
#                         print('只支持+-*/运算')
#             for i in list2:
#                 if i.isdigit():
#                     continue
#                 else:
#                     real_num = False
#                     break

#             if real_num:
#                 print(result)
#                 str_result = str1 + ' = ' + str(result)
#                 history.append(str_result)
#             else:
#                 print('输入正确的数字或者运算式子')
        
                    
# print('out')


