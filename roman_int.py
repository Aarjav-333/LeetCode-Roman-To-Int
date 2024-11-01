# Roman to integer

roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
num = input("Enter a Roman Numeral ")
split_digi = list(num) 
print(split_digi)
output = 0
for i in range(len(split_digi)):
    current_value = roman_values[split_digi[i]]            
    if i == len(split_digi) - 1 or roman_values[split_digi[i]] >= roman_values[split_digi[i + 1]]:  
        output += current_value
    else:
        output -= current_value
print(output)

