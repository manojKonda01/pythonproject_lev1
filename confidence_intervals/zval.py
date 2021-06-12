import numpy as np
import random
import pandas as pd
import math

url='https://www.sjsu.edu/faculty/gerstman/EpiInfo/z-table.htm'
df=pd.read_html(url)
lst=df[0]
arr=lst.to_numpy()
m=0
n=0
def zval(imp):
    global m,n
    for i in range(1,31):
        if imp>=arr[i][1]:
            if imp<arr[i+1][1]:
                for j in range(1,11):
                    if imp<=arr[i][j]:
                        m=float(arr[i][0])
                        n=float(arr[0][j])
                        break
    return (m+n)