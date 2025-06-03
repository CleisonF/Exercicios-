from itertools import count

c1 = count(start=5, step=5)
r1 = range(5, 20, 5)
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

print('Count')
for i in c1:
    if i >= 20:
        break

    print(i)
print()

print('Range')
for i in r1:
    if i > 20:
        break
    print(i)