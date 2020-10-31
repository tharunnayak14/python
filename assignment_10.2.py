name = input('Enter file:')
fhand = open(name)
hi = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        hi[time[0]] = hi.get(time[0], 0) + 1
for (k, v) in sorted(hi.items()):
    print(k, v)  # sorting by keys
