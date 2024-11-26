def main():
    try:
        size = int(input("Enter the size of the array: "))
        if size <= 0:
            print("The size of the array must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for the size.")
        return

    arr = [0.0] * size

    print(f"Enter the elements of the array:")
    for i in range(size):
        while True:
            try:
                arr[i] = float(input(f"Element {i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    try:
        x = int(input("Enter the index of the element to print: ")) 
        print(f"Element at index {x}: {arr[x]:.2f}")
    except IndexError:
        print(f"Index {x} is invalid.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the index.")

if __name__ == "__main__":
    main()
