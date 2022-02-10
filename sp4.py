print("1.Check if Number is Prime or Not")
print("2.Calculate facrorial of given number")
print("3.Given number is palindrome or not")
print("4.given number is armstomg or not")
print("5.Exit Prog")

def prime():
	num=int(input("\nEnter a Number= "))
	if num>1:		
		for i in range(2,num):
			if num%i==0:
				print(num,"Number is not Prime.")
				break										
			else:
				print(num,"Number is Prime.")
				break
				

def factorial():
	num = int(input("\nEnter a number: "))
	factorial = 1
	if num < 0:
		print("Sorry, factorial does not exist for negative numbers")
	elif num == 0:
		print("The factorial of 0 is 1")
	else:
		for i in range(1,num + 1):
			factorial = factorial*i
		print("The factorial of",num,"is",factorial)

def palindrome():
	n=int(input("\nEnter number:"))
	temp=n
	rev=0
	while(n>0):
	    dig=n%10
	    rev=rev*10+dig
	    n=n//10
	if(temp==rev):
	    print("The number is a palindrome!")
	else:
	    print("The number isn't a palindrome!")
		
def armstrong():
	num = int(input("\nEnter Number="))
	sum = 0
	temp = num
	while temp>0:
		digit = temp%10
		sum += digit ** 3
		temp//=10
	if num == sum:
		print(num,"is an Armstrong Number")
	else:
		print(num,"is not an Armstrong Number")

def ex():
	exit(0)

def default():
    return "Wrong Choice Try again!"

num=3
while num==3:
	switcher = {
	    1: prime,
	    2: factorial,
	    3: palindrome,
	    4: armstrong,
	    5:ex,
	     }

	def switch(i):
	    return switcher.get(i, default)()
    
	print(switch(int(input("Enter your Choice= "))))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

