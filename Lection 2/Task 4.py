input_string = input("Enter stroke: ")
glasnie = "aeiouAEIOU"
glasnie_stroka = ''.join(char for char in input_string if char in glasnie)
print("vowels:", glasnie_stroka)