str1 = 'hello '
str2 = 'world'
print(str1 + str2)  # concatinate strings
str3 = input("Enter any number:-")
try:
    x = int(str3)
except:
    print("Wrong input")
    quit()
print(x)

fruit = 'banana'
print(fruit[0])  # indexing string
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])
print(fruit[5])
# print(fruit[6])   gives error as 6 is out of range
x = len(fruit)  # gives us length of the string
print('length of string:-', x)
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
print("loop terminated")

for letter in fruit:
    print(letter)
print("loop terminated")

c = 0
for letter in fruit:
    if letter == 'a':  # counting no of 'a' in string
        c = c + 1
print(c)
print("loop terminated")

# slicing string

s = 'badavath tharun'
print(s[0:4])  # not includes 4
print(s[0:21])
print(s[:2])
print(s[8:])
print(s[:])
print(s)

# manipulating strings
a = 'hello'
b = 'tharun'
print(a + b)
print(a + ' ' + b)
print('l' in a)  # checking
print('m' in a)

# string library
greet = 'hello BOB'
zap = greet.lower()  # object method
print(zap)
print('HELLO'.lower())
print(greet.capitalize())
print(greet.find('ll'))  # gives index where its found
print(greet.find('z'))  # not found so returns -1

# search and replace
hi = 'hello tharun'
n = hi.replace('tharun', 'lakshman')  # does not change hi but creates n
print(n)
p = hi.replace('h', 'g')  # replaces all occurences of h by g
print(p)

# stripping whitespace
m = ' dfdf '
print(m.lstrip())
print(m.rstrip())
print(m.strip())

# prefix

line = 'please have coffee'
print(line.startswith('please'))
print(line.startswith('yo'))

# extracting

mail = 'badavath.tharun.mat19@itbhu.ac.in'
s = mail.find('.')
print(s)
q = mail.find('.', s+1)
print(q)
print(mail[s+1:q])
