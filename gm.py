name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))
numbers = [num1, num2, num3]

# num is even or odd and store it in a list
even_odd = []
for num in numbers:
    if num % 2 == 0:
        even_odd.append((num, "even"))
    else:
        even_odd.append((num, "odd"))

#Print num is even or odd
print(f"\nHello, {name}! Let's explore your favorite numbers:")
for num, status in even_odd:
    print(f"The number {num} is {status}.")

# Print square
squares = []
for num in numbers:
    squares.append((num, num ** 2))
for num, square in squares:
    print(f"The number {num} and its square: ({num}, {square})")

# sum of num
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}")

# Check if sum prime num
is_prime = True
if sum_numbers <= 1:
    is_prime = False
else:
    for i in range(2, int(sum_numbers ** 0.5) + 1):
        if sum_numbers % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Wow, {sum_numbers} is a prime number!")
else:
    print(f"{sum_numbers} is not a prime number.")
