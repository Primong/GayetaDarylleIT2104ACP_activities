class Capybara:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

capybaras = [Capybara("Biscoff", "M", 5),]

try:
    test_case = int(input("Enter the test case number: "))
    if test_case < 1 or test_case > 4:
        print("Invalid input. Please enter a number between 1 and 4.")
    else:
        selected_capybara = capybaras[test_case - 1]
        print(f"Test Case 1: Name: {selected_capybara.name}, Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")

except ValueError:
    print("Invalid input. Please enter a valid number.")
