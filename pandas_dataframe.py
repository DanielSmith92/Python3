# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 00:08:58 2025

@author: danie
"""


""" pandas data frame:
https://pandas.pydata.org/docs/getting_started/index.html
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame

"""
import pandas as pd
import numpy as np

# 1. construct data frames

## 1.1. via dictionary

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)
#    col1  col2
# 0     1     3
# 1     2     4


## 1.2. via numpy ndarray

nparray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # jede liste eine Zeile
df2 = pd.DataFrame(nparray, columns=['a', 'b', 'c'])
print(df2)

inputList = [(1, 2, 3), (4, 5, 6), (7.4, 8, 9)]
data = np.array(inputList,dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")])
# i4: 32-Bit-Ganzzahl
df3 = pd.DataFrame(data, columns=['c', 'a'])
# via columns spezifiziert man, welche Spalten im Dataframe enthalten sein 
# sollen, und in welcher Reihenfolge
print(df3)


## 1.3. via other data frame

df1 = pd.DataFrame([1, 2, 3], index=["a", "b", "c"], columns=["x"])
# index: row index
df2 = pd.DataFrame(data=df1, index=["a", "c"])
# filtern des Originaldataframes via 'index' Attribut
df2


# 2. Additional attributes

""" Additional attributes:
    
    
-T: The transpose of the DataFrame.
-at: Access a single value for a row/column label pair.
-attrs: Dictionary of global attributes of this dataset.
-axes: Return a list representing the axes of the DataFrame.
-columns: The column labels of the DataFrame.
-dtypes: Return the dtypes in the DataFrame.
-empty: Indicator whether Series/DataFrame is empty.
-flags: Get the properties associated with this pandas object.
-iat: Access a single value for a row/column pair by integer position.
-iloc: (DEPRECATED) Purely integer-location based indexing for selection by position.
-index: The index (row labels) of the DataFrame.
-loc: Access a group of rows and columns by label(s) or a boolean array.
-ndim: Return an int representing the number of axes / array dimensions.
-shape: Return a tuple representing the dimensionality of the DataFrame.
-size: Return an int representing the number of elements in this object.
-style: Returns a Styler object.
-values: Return a Numpy representation of the DataFrame.

"""

nparray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df1 = pd.DataFrame(nparray, index=["a", "b", "c"], columns=["x", "y", "kl"])
# df1
# Out[73]: 
#    x  y  kl
# a  1  2   3
# b  4  5   6
# c  7  8   9

## Transpose
df1.T

## Get value at specified row/column pair: via [index, column]
df1.at['a','x']
df1.at[4, 'x'] = 10 # can enter new rows by setting new index
df1.at[4, 'b'] = 230 # can enter new column by setting new column
df1.at[40, 'dd'] = 10.2 

## Get value at specified row/column pair: via [number row, number column]
df1.iat[2,1] # checks 3rd row and 2nd column
df1.at[8, 8] = 10 


## Columns
df1.columns

# loc

# iloc


# 3. Methods on data frames
import pandas as pd
import numpy as np

list1 = [1,2,3]
list2 = [10,20,30]
list3 = [-1,-2,-5]
list4 = [2*x for x in list3]

my_array = np.array([list1, list2, list3, list4])
df4 = pd.DataFrame(my_array, columns=['a','b','c'])
# df4
# Out[48]: 
#     a   b   c
# 0   1   2   3
# 1  10  20  30
# 2  -1  -2  -5
# 3  -2  -4 -10


## abs()
df4.abs()

## add_prefix() and add_suffix()
df4.add_prefix('pref_') # add prefix to  columns
# Out[49]: 
#    pref_a  pref_b  pref_c
# 0       1       2       3
# 1      10      20      30
# 2      -1      -2      -5
# 3      -2      -4     -10

df4.add_suffix('_suffix') # add suffix to  columns
# Out[50]: 
#    a_suffix  b_suffix  c_suffix
# 0         1         2         3
# 1        10        20        30
# 2        -1        -2        -5
# 3        -2        -4       -10


## Aggregate using one or more operations over the specified axis
df4.agg(func=np.sum, axis=0) #sum over row
df4.agg(func=np.sum, axis=1) #sum over columns

