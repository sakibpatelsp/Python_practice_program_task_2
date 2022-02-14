"""7. Write a program to calculate simple interest.Accept values from user.(si=pnr/100)"""
p=float(input("Enter Principal value :"))
r=float(input("Enter Rate of Interest: "))
t=float(input("Enter time Duration : "))
simpleI=((p*r*t)/100)
print("Simple Interest is :",simpleI)