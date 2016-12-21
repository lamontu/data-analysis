# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

print("## Create DataFrame using dictionary, key as column name:")
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
print(DataFrame(data))
print(DataFrame(data, columns=['year', 'state', 'pop']))  # designate order
print()
 
print("""## Designate index and column,
    if column not exist, set 'NaN' in this column:""")
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
print(frame2['state'])
print(frame2.year)
print(frame2.ix['three'])
frame2['debt'] = 16.5  # modify the whole column using an element
print(frame2)
frame2.debt = np.arange(5)  # modify the whole column using an array
print(frame2)
print()

print("""## Use Series to designate the index and value for modification,
   the unspecified value set to 'NaN':""")
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)
print()

print("## Assign value to new column:")
frame2['eastern'] = (frame2.state == 'Ohio')
print(frame2)
print(frame2.columns)

print("## DataFrame transpose:")
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}  # No duplicated keys  
frame3 = DataFrame(pop)
print(frame3)
print(frame3.T)
print()

print("## Designate index order:")
print(DataFrame(pop, index=[2001, 2002, 2003]))
print()

print("## Initialize using slice:")
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
print(DataFrame(pdata))
print()

print("## Designate index name and columns names:")
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
print(frame3.values)
print(frame2.values)
