'''Accept Marital status  and print Miss or Mrs in front of name.'''
a=str(input("Enter Name: "))
b=str(input("Enter Marital Status If Married Type 'yes' if not then type 'no': "))
if b=='yes' :
		print("Mrs.",a)
elif b=='n':
		print("Miss.",a)
elif b!='n'  or  b!='y':
		print("Wrong Choices")				
else:
				print("Wrong Choice")
				exit(0)