def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

num = int(input("Enter a positive integer: "))

if num < 0:
    print("Please enter a postive integer.")
else:
    result = sum_of_natural_numbers(num)
    print(f"The sum of natural numbers up to {num} is: {result}")
