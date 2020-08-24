# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:32:11 2020

@author: a0970
"""

names=[]
scores=[]
total=0

n=input('班上有幾位同學')
n=int(n)

for i in range(n):
    
    name=input('請輸入同學名字')
    names.append(name)
    
    
    score=input('輸入成績')

    score=int(score)
    scores.append(score)
    
for item in scores:
    total=total+item
    

print('平均分數',(total/n))
          
highest=0
for j in range(n):
    if scores[j]>highest:
        highest=scores[j]
        highestname=names[j]
        
print(highestname,'最高分:',highest)

lowest=100
for j in range(n):        
    if scores[j]<lowest:
        lowest=scores[j]
        lowestname=names[j]

print(lowestname,'最低分:',lowest)