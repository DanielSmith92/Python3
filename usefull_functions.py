# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:10:00 2025

@author: danie
"""

""" help function:
    
1. help()
2. Quellcode anzeigen: Mit dem Modul inspect kannst du auch den Quellcode 
   einer Funktion anzeigen lassen:
       
       import inspect
       import dein_modul  # Ersetze `dein_modul` mit dem Namen des Moduls, das die Funktion enthält

        print(inspect.getsource(dein_modul.deine_funktion))
       
"""

# Beispiel:
help(zip)





""" zip function: 
    
The zip() function in Python is a built-in function that aggregates elements 
from two or more iterables (like lists, tuples, or dictionaries) and 
returns an iterator of tuples. Each tuple contains the elements from each 
iterable that share the same index position.    
"""

# Examples:

# Define two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['aa', 'ab', 'ac']

# Use zip to combine them
zipped = zip(list1, list2)
zipped2 = zip(list1, list2, list3)

# Convert to list to display the result
result = list(zipped)
print(result)

result2 = list(zipped2)
print(result2)






""" pandas data frame to dictionary """

def DfToDict(df, keys, werte):
    
    temp = dict(zip(df[keys], df[werte]))
    return temp

import pandas as pd

df = pd.DataFrame([list1, list2])
df2 = pd.DataFrame([list1, list2, list3], columns = ['a', 'b', 'c'])

DfToDict(df2, 'a', 'b')

# df2
# Out[15]: 
#     a   b   c
# 0   1   2   3
# 1   a   b   c
# 2  aa  ab  ac

# DfToDict(df2, 'a', 'b')
# Out[16]: {1: 2, 'a': 'b', 'aa': 'ab'}

