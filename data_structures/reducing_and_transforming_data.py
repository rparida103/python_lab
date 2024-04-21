nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

s2= sum([x * x for x in nums])
print(s2)

from collections import ChainMap
'''
A ChainMap takes multiple mappings and makes them logically appear as one.
If there are duplicate keys, the values from the first mapping get used. 
'''
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b)
print(c)
print(c['x'])

merged = ChainMap(a, b)
print(merged)


