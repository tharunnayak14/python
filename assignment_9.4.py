name = input('Enter file:')
fhand = open(name)
hi = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        hi[words[1]] = hi.get(words[1], 0) + 1
bc = 1
bw = 1
for word, count in hi.items():
    if bc is None or count > bc:
        bw = word
        bc = count
print(bw, bc)
