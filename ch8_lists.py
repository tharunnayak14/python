# date 12/05/2020
# lists
from typing import List

friends = ['hi', 'Tharun', 'hello']
print(friends)
print(friends[0])
print([1, 7, [2, 3], 4])  # list in a list
print([])  # empty list
for i in [5, 4, 3, 2, 1]:
    print(i)
print("**********************************")
yo = [1, 2, 3, 4, 5]
yo[2] = 4343  # lists are mutable
print(yo)
print("**********************************")

print(len(friends))

# range function
print(range(4))
print(range(len(friends)))

for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year:', friend)
print("**********************************")

for i in friends:
    print('Happy new year:', i)
print("**********************************")
# manipulating lists
a = [1, 2, 3]  # concatenating lists
b = [4, 5, 6]
c = a + b
print(c)
print("**********************************")
# slicing

print(a[:])
print(a[1:])
print(a[0:1])
print(c[3:])
print("**********************************")
# building list
stuff = list()
stuff.append(1)
stuff.append('bm')
stuff.append('sd')
print(stuff)
print("**********************************")

print(9 in c)
print(3 in c)
print("**********************************")

l = [12, 343, 2323, 23, 23, 3, 332, 32]
l.sort()
print(l)
print(max(l))
print(min(l))
print(sum(l))
print(sum(l) / len(l))
print("**********************************")

# hi = list()
# while True:
#    inp = (input("Enter any value:"))
#    try:
#        val = float(inp)
#    except:
#       if inp == 'done':
#            break
#       else:
#           print("Enter numeric value")
#           quit()
#   hi.append(val)
# print('Average:', (sum(hi))/len(hi))
# print("**********************************")

# strings and lists

abc = 'we like icecream'
v = abc.split()
print(abc)
print(abc[0])
for w in v:
    print(w)
print("**********************************")

me = 'dsad sdsa  :    sdd sd dd hy j'
e = me.split()
print(e)
print(len(e))
y = me.split('d')
print(y)
print(len(y))
print("**********************************")

# double split
mail = 'badavath.tharun.mat19@itbhu.ac.in'
words = mail.split('.')
print(words[1])
print(words[2])
ma = words[2].split('@')
print(ma[1])
print("**********************************")
