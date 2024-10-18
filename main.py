unit = int(input("Enter the amount of units: "))


if unit < 50 :
    bill = unit*2.60 + 25

elif unit < 100:
    bill = unit*3.25 + 35

elif unit < 200:
    bill = unit*5.26 + 45

elif unit > 200:
    bill = unit*8.45 + 75

print("Your bill is: ", bill)


