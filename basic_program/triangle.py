"""Write a program to check if a triangle is valid or not.(Input-3 angles of triangle)."""
a=float(input("Enter First angle of Triangle: "))
b=float(input("Enter Second angle of Triangle: "))
c=float(input("Enter Third angle of Triangle: "))
s=a+b+c
if s==180 and a!=0 and b!=0 and c!=0:
	print("Triangle is valid.")
else:
	print("Triangle is Not valid.")