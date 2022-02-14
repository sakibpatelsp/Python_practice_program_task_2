'''WAP to accept coordinates of a point and determine in which Quadrant it lies.'''
x=(float(input("Enter Value of X-axis: ")))
y=(float(input("Enter Value of Y-axis: ")))
if x>0 and y>0:
			print("Coordinate x= ",x,"and y=",y, "coordinate Lies in First Quadrant")
elif x<0 and y>=0:
			print("Coordinate x= ",x,"and y=",y, " coordanate Lies in Second Quadrant")
elif x>=0 and y<0:
			print("Coordinate x= ",x,"and y=",y, "coordinate lies in Third Quadrant")
elif x<0 and y<0:
			print("Coordinate x= ",x,"and y=",y, "coordinate lies in Fourth Quadrant")
elif x==0 and y==0:
			print("Coordinate x= ",x,"and y=",y, "coordinate in Origin")
else:
			print("Wrong Choice!!!")