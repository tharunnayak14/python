score = input("Enter score:-")
try:
    s = float(score)
except:
    s = -1
if s == -1:
    print("Enter numeric input")
elif s > 1.0 or s < 0.1:
    print("Enter number in the range 0.1-1.0")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")
