fname = input('Enter file name: ')
fh = open(fname)
ls = list()
count = 0
for i in fh:
    i = i.rstrip()
    if i.startswith('From') and not i.startswith('From:'):
        count = count + 1
        ee = i.split()
        print(ee[1])
print('There were', count , 'lines in the file with From as the first word')
