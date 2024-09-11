def extract_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_list = [char for char in s if char in vowels]
    return vowel_list

input_string = input("Enter a string: ")
vowel_list = extract_vowels(input_string)
print (vowel_list)