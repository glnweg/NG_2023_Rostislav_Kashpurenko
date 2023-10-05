chislo1 = int(input("Vvedite pervoe chislo: "))
action = input("Vvedite deistvie (+,-,*,/,**,): ")
chislo2 = int(input("Vvedite vtoroe chislo: "))
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
else :
    print("Error")