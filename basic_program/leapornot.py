'''Find out if a given year is a leap year or not.'''
y=int(input("Enter value for year: "))
if((y % 400 == 0) or (y % 100 != 0) and (y%4== 0)):   
			print(" Year",y," is a leap Year")
else:  
			print ("Year",y," is not a leap Year")