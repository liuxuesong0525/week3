#编写程序，生成一个包含50个随机整数的列表，
# 随机整数的范围是从-10到10，
# 然后将列表中所有的正数存为一个新的子列表，
# 负数存为另一个新的子列表。
import random
list=[]
for i in range(50):
    list.append(random.randint(-10,10))
print(list)
list1=[]
list2=[]
for i in list:
    if i>0:
        list1.append(i)
    elif i<0:
        list2.append(i)
print("正数列表",list1)
print("负数列表",list2)