# 利用索引和切片获取元素
"""
verse=["青青园中葵","朝露带日晞","阳春布德泽","万物生光辉","长恐秋节至","焜黄华叶衰",
       "百川东到海","何时复西归","少壮不努力","老大徒伤悲"]
print(verse[2])        #获取第二个元素(索引）
print(verse[1:6])      #获取第2个到第6个元素（切片）
print(verse[1:6:2])    #获取第2个，第4个和第6个元素（切片）
"""

# 序列相加
'''
verse1 = ["自古逢秋悲寂莫", "我言秋日胜春朝", "晴空一鹤排云上", "便引诗情到碧霄"]
verse2 = ["青青园中葵", "朝霞待日晞", "阳春布德泽", "万物生光辉", "长恐秋节至", "焜黄华叶衰",
          "百川东到海", "何时复西归", "少壮不努力", "老大徒伤悲"]
print(verse1 + verse2)  # 序列相加
print(verse1 * 5)  # 序列相乘

print("晴空一鹤排云上" not in verse1)
# 检查verse1中元素”晴空一鹤排云上“是否存在 语法格式  value in sequence
# value 表示要检查的元素  sequence 表示指定的序列
'''

# 计算序列的长度、最大值、最小值
'''
num = [7, 14, 21, 28, 35, 42, 49, 56, 63]
print("序列num的长度为", len(num))  # len()函数计算列表的长度
print("序列", num, "中最大值为", max(num))    # 用max函数计算列表的最大元素
print("序列", num, "中最小值为", min(num))    # 用min函数计算列表的最小元素

list：将序列转换列表   str ：将序列转
换为字符串  sum ：计算元素和  sorted：将元素进行排序  reversed:反序序列中的元素
enumerate：将序列组合为一个索引序列，多用在for循环
'''

# 列表的创建
'''
print(list(range(10, 20, 2)))   # list函数不仅能通过range对象创建列表，还可以通过其他对象创建列表
verse2 = ["青青园中葵", "朝霞待日晞", "阳春布德泽", "万物生光辉", "长恐秋节至", "焜黄华叶衰",
          "百川东到海", "何时复西归", "少壮不努力", "老大徒伤悲"]
print(verse2[1])    # 获取列表verse2列表1的元素
'''
'''
import datetime
# d定义一个列表
mot = ["星期一c语言考试",
       "星期二思政考试",
       "星期三不知道",
       "星期四不知道",
       "星期五不知道",
       "星期六数学考试",
       "星期天英语考试"]
day = datetime.datetime.now().weekday()
print(mot[day])
'''

'''
直接使用for循环实现遍历列表
print("" * 2, "秋词")
verse = ["自古逢秋悲寂莫", "我言秋日胜春朝", "晴空一鹤排云上", "便引诗情到碧霄"]
for item in verse:
    print(item)
'''

'''
使用for循环和enumerat（）函数实现
for index,item in enumerat(listname):
#输出index和item

index:用于保存元素的索引
item:获取元素的值，输出元素内容时，直接输出该变量即可
listname：为列表名称


print("" * 3, "秋词")
verse = ["自古逢秋悲寂莫", "我言秋日胜春朝", "晴空一鹤排云上", "便引诗情到碧霄"]
for index, item in enumerate(verse):
    print(index, item)
'''
'''
print("" * 3, "长歌行")
verse = ["青青园中葵", "朝霞待日晞", "阳春布德泽", "万物生光辉", "长恐秋节至", "焜黄华叶衰",
         "百川东到海", "何时复西归", "少壮不努力", "老大徒伤悲"]
for index, item in enumerate(verse):
    if index % 2 == 0:  
        print(item + "， ", end='')         
    else:
        print(item + "。")
'''

'''
添加元素
numberlist = []
a = 6
while True:
    if a % 2 == 0:
        a = a / 2
    else:
        a = a * 3 + 1
        numberlist.append(a)
        if a == 1:
            break;
    print("这个列表是", numberlist)
'''

'''修改列表元素
verse = ["长亭外", "古道边", "芳草碧连天"]
print(verse)
verse[2] = "一行白鹭上青天"  # 修改列表第二个元素
print(verse)
'''
'''
verse = ["长亭外", "古道边", "芳草碧连天"]
del verse[1]                       #根据索引删除列表中的元素
verse.remove("芳草碧连天")           #根据元素值删除
print(verse)
'''

