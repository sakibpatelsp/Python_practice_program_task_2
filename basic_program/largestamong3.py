''' WAP to find the largest among 3 numbers.'''
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
if a>=b>=c or a>=c>=b:
		print("Largest Number is: ",a)
elif b>=c>=a or b>=a>=c:
			print("Largest Number is: ",b)
elif c>=b>=a or c>=a>=b:
			print("Largest Number is: ",c)