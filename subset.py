# -*- coding: utf-8 -*-
"""
@author: shernandezoa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from itertools import combinations


def top_subsets(vals, sizes=[1]):
    
    for size in sizes:
        
        
        
        pass
    
 
def remove_outliers(df, q=0.05):
    upper = df.quantile(1-q)
    lower = df.quantile(q)
    mask = (df < upper) & (df > lower)
    return df[mask]


def plt_pd(df: pd.DataFrame(), cols=[], title='Title', minval=0, maxval=1):
    plt.figure()
    df.plot.bar(ylim=[minval, maxval], title=title)
    plt.plot(np.full_like(df.to_numpy(), df.mean()), 'r--')
    

# --------------------------------------------------------------- #
minval = 0
maxval = 100
size = 50 

vals_np = np.random.randint(minval, maxval, size=size)
top_subsets(vals_np, [5])

# 

# vals_np = 

# 

vals_df = pd.DataFrame({'Original': vals_np}, index=np.arange(size))
vals_df2 = remove_outliers(vals_df, 0.1)


plt_pd(vals_df, ['Original'], 'Original values', minval, maxval)
plt_pd(vals_df2, ['Original'], 'Values without outliers', minval, maxval)

plt.figure()
vals_df2.boxplot()