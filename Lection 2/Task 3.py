chislo = int(input('Enter number: '))
spisok =  []
for cifra in range(1, chislo + 1):

    if (cifra % 2 == 0) and (cifra % 3 == 0):
        print( cifra"  | 2, 3")
    elif cifra % 2 == 0:
        print( cifra "  | 2")
    elif cifra % 3 == 0:
        print( cifra "  | 3")
    else: 
        print(cifra )
        spisok.append(cifra)
    print('---')
print (spisok)