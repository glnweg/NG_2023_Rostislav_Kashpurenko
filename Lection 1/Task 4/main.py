chislo1 = int(input("Enter first number: "))
action = input("Enter operation (+,-,*,/,**,koren'): ")
chislo2 = int(input("Enter second number: "))
if action == "+" :  
    print (chislo1 + chislo2)
elif action == "-" :
    print (chislo1 - chislo2)
elif action == "*" :
    print (chislo1 * chislo2)
elif action == "/" :
    print (chislo1 / chislo2)
elif action == "**" :
    print (chislo1 ** chislo2)
elif action == "koren'" :
    print (chislo1**(1/chislo2))
else :
    print("Error")