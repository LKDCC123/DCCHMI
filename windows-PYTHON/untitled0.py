# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 18:59:52 2022

@author: QHX
"""
import pandas as pd

data = pd.read_table('20220217_163322.dat', sep='\t')   
aa = data.xs('Period', 1)     
print('aa')
print('bb')                  
# aa = data[data.header.isin(lineEdit.text())].values[:,0]
