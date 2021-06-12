import math
import numpy as np
import zval
import pandas as pd
import random


lis=[]
def ci(sample,confidence):
    alpha=1-confidence
    m=np.mean(sample)
    st=np.std(sample)
    alp=1-alpha/2
    l=m-(zval.zval(alp)*(st/math.sqrt(len(sample))))
    h=m+(zval.zval(alp)*(st/math.sqrt(len(sample))))
    lis.append(l)
    lis.append(h)
    print('Significance = ',alpha)
    print('Z{} = {}'.format(alp,zval.zval(alp)))
    print('Mean of sample= {}\n Std of sample = {}'.format(m,st))
    return lis

listt = list(np.logspace(1,100,1000))
size= int(input('ENter sample size\n'))
sample=random.sample(listt,size)
confidence=float(input('ENter confidence\n'))
print(ci(sample,confidence))