gradusi = int(input ("How many degrees?\n"))
option = input ("1 or 2? (1 - Celsius to Fahrenheit, 2 - Fahrenheit to Celsius): ")
if option == "1":
    print ((gradusi * 9/5) + 32 )
elif option == "2":
    print ((gradusi - 32) * 5/9)
else:
    print ("Error")