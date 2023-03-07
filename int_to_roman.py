roman_numerals = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

roman = "MCMXCIV"

result = 0
prev_value = 0
for c in roman:
    value = roman_numerals[c]
    result += value
    if value > prev_value:
        result -= 2 * prev_value
    prev_value = value


print(result)       #? 1994