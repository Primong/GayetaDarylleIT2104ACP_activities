roman_values = {
    'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000,
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def roman_to_integer(roman):
    for char in roman:
        if char not in roman_values:
            return "Invalid Roman numeral"
    result = 0
    prev_value = 0
    for char in reversed(roman):
        current_value = roman_values[char]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value
    return result

def main():
    roman = input("Enter a Roman numeral: ").strip()
    result = roman_to_integer(roman)
    print(f"The integer value of {roman} is: {result}")

if __name__ == "__main__":
    main()
