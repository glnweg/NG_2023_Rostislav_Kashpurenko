user_input = input("Enter elements by spaces: ")
numbers = user_input.split()
count = len([num for num in numbers if num.isdigit()])
print(count)