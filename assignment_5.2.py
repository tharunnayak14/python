large = -1
small = None
while True:
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        n = int(num)
    except:
        print("Invalid input")
        continue
    if n > large:
        large = n
    if small is None:
        small = n
    elif n < small:
        small = n
print("Maximum is", large)
print("Minimum is", small)
