'''Unpacking works with any object that happens to be iterable'''

p = (4, 5)
x, y = p

print(f"x: {x}, y: {y}")

s = 'Hello'
a, b, c, d, e = s
print(f"a: {a}, e: {e}")

'''Discard certain elements'''
l = [1, 2, 3, 4]
_, _, _, n4 = l
print(n4)

first, *middle, last = l
print(f"First: {first}, Last: {last}")
print(*middle)



