# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count= 0
h = open(fname)
for line in h:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
g = open(fname)
a = 0.0
for line in g:
    if line.startswith('X-DSPAM-Confidence:'):
        a = a + float(line[line.find('0'):])
print('Average spam confidence:', a/count)
