TEMP = float(input("ENTER A TEMPERATURE YOU WANT TO CONVERT: "))
UNIT = input("WHAT IS THE UNIT OF THE  TEMPERATURE YOU WANT TO CONVERT (K,C,F)"
             "HERE, K IS KELVIN,C IS CELCIUS AND F IS FAHRENHEIT : ").upper()
CONVERT = input("WHAT ARE GONNA CONVERT IT INTO(K,C,F) :  ").upper()

temperature = None
UNITS = ""

if UNIT == "F":
    if CONVERT == "C":
        temperature = ((TEMP - 32)*(5/9))
        UNITS = "C"
    elif CONVERT == "K":
        temperature = (((TEMP - 32)*(5/9)) + 273.15)
        UNITS = "K"
    elif CONVERT == "F":
        temperature = (TEMP)
        UNITS = "F"

if UNIT == "C":
    if CONVERT == "F":
        temperature = (((9/5) * TEMP) + 32)
        UNITS = "F"
    elif CONVERT == "K":
        temperature = (TEMP + 273.15)
        UNITS = "K"
    elif CONVERT == "C":
        temperature = (TEMP)
        UNITS = "C"

if UNIT == "K":
    if CONVERT == "C":
        temperature = (TEMP - 273.15)
        UNITS = "C"
    elif CONVERT == "F":
        temperature = (((TEMP - 273.15) * (9/5)) + 32)
        UNITS = "F"
    elif CONVERT == "K":
        temperature = (TEMP)
        UNITS = "K"

if UNIT == "":
    print("NO UNIT FOUND")

if temperature is not None:
    print(f"{temperature}{UNITS}")\

else:
    print("INVALID CONVERSION. CHECK YOUR INPUT")



