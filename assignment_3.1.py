hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h < 40.0:
    print("h*r")
elif h > 40.0:
    print(40*r+(h-40.0)*r*1.5)
