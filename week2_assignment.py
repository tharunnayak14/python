import re
count = 0
hand = open('files.txt')
for line in hand:
    line = line.rstrip()
    y = re.findall("[0-9]+", line)
    for i in y:
        count += int(i)
print(count)
