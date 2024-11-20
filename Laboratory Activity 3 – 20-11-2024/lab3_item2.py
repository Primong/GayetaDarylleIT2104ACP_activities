def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n

def main():
    try:
        n = int(input("Enter a number: "))
        if is_perfect_number(n):
            print(f"{n} is a perfect number.")
        else:
            print(f"{n} is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
