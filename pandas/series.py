# -*- coding: utf-8 -*-

from pandas import Series

print("## Create Series using array:")
obj = Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)
print()

print("## Designate the index of a Series:")
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)
print(obj2['a'])
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])  # a list in []
print(obj2[obj2 > 0])
print('b' in obj2)
print('e' in obj2)

print("## Create Series using dictionary:")
sdata = {'Ohio': 45000, 'Texas': 71000, 'Oregon': 16000, 'Utah':5000}
print("### obj3 = Series(sdata):")
obj3 = Series(sdata)
print(obj3)
print()

print("""### Create Series using dictionary and extra index,
    the uncompatible part set to 'NaN':""")
print("### obj4 = Series(sdata, index=states):")
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
print(obj4)
print()

print("## Series addition on same index:")
print(obj3 + obj4)
print()

print("## Designate Series name and index name:")
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
print()

print("## Replace index:")
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
