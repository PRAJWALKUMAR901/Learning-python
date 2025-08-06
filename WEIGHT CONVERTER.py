#WEIGHT CONVERTER
WEIGHT = float(input("Enter your weight : "))
UNITS = (input("IS IT IN KILOGRAM OR POUND (K/P) : "))

if UNITS == "K":
    Weight =round(float(WEIGHT*2.2),1)
    units = "Lbs"
elif UNITS == "P":
    Weight =round(float(WEIGHT/2.2),1)
    units = "Kg"
else:
    print("WHAT ARE YOU DOING?")



print(f"YOUR WEIGHT IS {Weight}{units}")
