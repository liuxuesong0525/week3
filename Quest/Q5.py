#	s='The column above illustrates apparently' \
#  ' the polularity of people ' \
#  'doing exercise in a certain year ' \
#  'from 2013 to 2018.Based upon the data,' \
#  'we can see that python is wonderful. ' \
#  'python is wonderful. Python ' \
#对这段文字中的单词进行数字统计，并且进行个数升序
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python'
s=s.split(' ')
d={}
d1={}
for i in s:
    d[i]=s.count(i)
s1=list(d.values())
s1.sort()
s1=set(s1)
s1=list(s1)
for i in s1:
    for j in d:
        if i==d[j]:
            d1[j]=i
print(d1)