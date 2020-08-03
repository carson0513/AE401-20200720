# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:33:36 2020

@author: a0970
"""

import random

x=random.randint(1,10)

c=input("猜一個數字")
c=int(c)

if x ==c:
    print("猜對了")
    
else:
    print("猜錯了˙") 