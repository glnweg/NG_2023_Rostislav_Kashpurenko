num = int(input("Enter number: "))

nums = []
for i in range(1, num + 1):
    divider = [str(j) for j in range(1, i + 1) if i % j == 0]
    divider_str = ", ".join(divider)
    print(f"{i:5} | {divider_str}")

    if len(divider) == 2:  
        divider.append(i)

print(divider)