x = ('gi', 'yo', 'tharun')
print(x)

# not changable/ not mutable

z = (5, 4, 3)
# z[1] = 7 # gives traceback
print(z)
print(dir(z))
# more efficient than list
(x, y) = (4, 'taryn')
print(x)

# tuple and dict
d = dict()
d['c'] = 2
d['e'] = 4
for (k, v) in d.items():
    print(k, v)
for (k, v) in sorted(d.items()):
    print(k, v) # sorting by keys

d = {'a': 1, 'b': 3, 'c': 3}
d.items()
print(sorted(d.items()))

# sorting by value
t = list()
for (k, v) in d.items():
    t.append((v, k))  # list of tuple
print(t)
t = sorted(t)
print(t)

# 10 most common words

name = input('Enter file:')
fhand = open(name)
hi = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        for word in words:
            hi[word] = hi.get(word, 0) + 1

lst = list()
for key, val in hi.items():
    tup = (val, key)
    lst.append(tup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)

print(sorted([(v, k) for k, v in d.items()]))