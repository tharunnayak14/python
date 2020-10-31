hours = input("Enter Hours:")
try:
    h = float(hours)
except:
    print("Enter numeric input")
rate = input("Enter rate:")
try:
    r = float(rate)
except:
    print("Enter numeric input")
def computepay():

    if h < 40.0:
        return h * r
    elif h > 40.0:
        return 40 * r + (h - 40.0) * r * 1.5


total = computepay()
print("Pay", total)
