import re
handle = open('files.txt')
for line in handle:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
# matching and extracting
# for digits
handle = open('files.txt')
for line in handle:
    y = re.findall('[0-9]+', line)
    if y == []: continue
    print(y)
# for vowels
handle = open('files.txt')
for line in handle:
    y = re.findall('[AEIOU]+', line)
    if y == []: continue
    print(y)

# greedy method
# ^F.+?:
# add ? to + or *
# \S+@\S+
# [0-9]+
# [AEIOU]+
# ^find .*(\S+@\S+)
# @([^ ]*)
