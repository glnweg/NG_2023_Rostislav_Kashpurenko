gradusi = input ("1 or 2? (1 - Celsius to Fahrenheit, 2 - Fahrenheit to Celsius): ")
if gradusi == "1":
    celsius = int(input ("How many Celsius?\n"))
    print ((celsius * 9/5) + 32 )
elif gradusi == "2":
    fahrenheit = int(input ("How many Fahrenheits?\n"))
    print ((fahrenheit - 32) * 5/9)
else:
    print ("Error")