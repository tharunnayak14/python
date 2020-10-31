purse = dict()
purse['money'] = 12
purse['candy'] = 3
print(purse)
purse['you'] = 212
print(purse['you'])
purse['candy'] = purse['candy'] + 2
print(purse)
di = {'hi': 1, 'yo': 2, 'hee': 22}
print(di)
di = {}
print(di)

# counting with dictionaries
# histogram

c = dict()
names = ['cd', 'cd', 'wdw', 'wd', 'wddd']
for name in names:
    if name not in c:
        c[name] = 1
    else:
        c[name] = c[name] + 1
print(c)

# using get method
if name in c:
    x = c[name]
else:
    x = 0
x = c.get(name, 0)

# over and over
count = dict()
for name in names:
    count[name] = count.get(name, 0) + 1
print(count)

# dic and files
count = dict()
line = input('enter text:-')
words = line.split()
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

# for loop in dict
for i in count:
    print(i, count[i])
print(count.keys())  # list of keys
print(count.values())
print(count.items())
print(list(count))

# 2 iteration variables
for a, b in count.items():
    print(a, b)

name = input('Enter file:')
fhand = open(name)

hi = dict()
for line in fhand:
    words = line.split()
    for word in words:
        hi[word] = hi.get(word, 0) + 1
bc = 1
bw = 1
for word, count in hi.items():
    if bc is None or count > bc:
        bw = word
        bc = count
print(bw, bc)