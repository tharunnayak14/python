# opening a file
# handle = open(filename,mode)
# f hand = open('m.txt','r')
xfile = open('m.txt')
for c in xfile:
    print(c)
print("***********************************")

# counting lines

h = open('m.txt')
count = 0
for l in h:
    count = count + 1
print('Line count:-', count)
print("***********************************")

# reading whole file

u = open('m.txt')
inp = u.read()
print(len(inp))
print(inp[:])
print("***********************************")

# searching through a file

p = open('m.txt')
for line in p:
    line = line.rstrip()
    if line.startswith('g'):
        print(line)
print("***********************************")

y = open('m.txt')
for line in y:
    line = line.rstrip()
    if not 'b' in line:
        continue
    print(line)
print("***********************************")
