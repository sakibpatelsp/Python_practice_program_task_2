'''WAP to determine if the seller has made profit or loss.Display amount of profit/loss.(Input: Cost price and selling price).'''
cpr=float(input("Enter Cost Price:"))
spr=float(input("Enter Selling Price: "))
a=spr-cpr
if spr>cpr:
		print("Profit made by seller is: ",a)
elif cpr>spr:
		print("Loss made by seller is: ",a)
elif cpr==spr:
		print("No Profit No Loss made by seller is :",a)