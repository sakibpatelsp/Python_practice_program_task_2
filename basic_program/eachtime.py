"""6. WAP to assign different type of values to one variable at different instance of and print its type each time"""
while True:
	i=str(input("Press B or b to Proceed else press any key to exit Program: "))
	if i=='B'or i=='b':
		inp = input("Assign value to variable a: ")
		print("Variable A:", inp,type(inp))
	else:
		exit("Program Exit")