"""write a program to find age at any particular year """

age_or_year = int(input("Enter your age or year of Birth: "))
s = str(age_or_year)

if age_or_year > 2023:
    print("You are not born yet\n")


elif len(s) == 4:
    ty = int(s)
    r = ty + 100
    print(f"You will turn 100 years old in year {r}\n")

else:
    print("Wrong input")

def calc(i, b):
    total = i - b

    if i <= b:
        return "You enter invaild year"

    else:
        print(f"You will be {total} years old in {i}")

while(True):
    print("Do you want to know your age in particular year")
    print("1 for yes.\n2 for no")
    inp = int(input("Enter your choice: "))
    if inp == 1:
        i = int(input("Enter the year to know age: "))
        b = int(input("Enter the birth year: "))
        calc(i, b)
        break

    elif inp == 2:
        break

    else:
        print("Wrong input")