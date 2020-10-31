# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
f = fh.read()
for line in fh:
    line = line.rstrip()
print(f[:].upper())
