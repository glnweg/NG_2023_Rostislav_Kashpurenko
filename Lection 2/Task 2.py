userinp = input("Write elements by spaces: ").split()

for chislo in userinp:
    try:
        int(chislo)
        print(chislo)
    except:
        continue