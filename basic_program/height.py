"""Categorize the person depending on the height.
a. <150	Dwarf
b. =150 	Average heighted
c. >=165	Tall"""
height=float(input("Enter Height of Person: "))
if height==150:
			print("Person having Average height: ",height)
elif height>=165:
			print("Persion having Tall height: ",height)
elif height<150:
			print("Persion having Dwarf height: ",height)
else:
			print("Wrong Choice Try Again!!!")