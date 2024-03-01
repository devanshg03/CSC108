import random
# Exercise Prime Numbers
def prime_stop(stop: int) -> str:
    """Return the prime numbers from n to stop, inclusive, in increasing order.

    Precondition: stop > 0
    """
    # Initializes an empty string to store the result
    result = ''
    # Checks precondition
    if stop <= 0:
        return 'WARNING: Argument must be an integer greater than 0.'
    
    # Iterates through every integer from 2 to stop
    for i in range(2, stop + 1):
        # Checks if the current integer is prime
        if is_prime(i):
            # If the current integer is prime, it is added to the result, along with a space
            result += str(i) + ' '
    # Returns the result, excluding the last space
    return result[:-1]

def is_prime(num: int) -> bool:
    """Returns true if num is prime, otherwise returns false.
    
    >>> is_prime(2)
    True

    >>> is_prime(4)
    False
    """
    # Checks if the number is less than or equal to 1
    if num <= 1:
        # Returns false as 1 and 0 are not prime numbers
        return False
    # Iterates through every integer from 2 to num - 1
    for i in range(2, num):
        # Checks if the current integer is a factor of num
        if num % i == 0:
            return False
    return True

# Exercise – Square Root
def print_nums() -> int:
    for int in range(1, 100000):
        if ((int + 100)**0.5).is_integer() and ((int + 200)**0.5).is_integer():
            print(int)

# Exercise – Repeated User Inputs
def user_input() -> str:
    while True:
        user_input = input("Enter a number: ")
        if user_input == "done":
            break
        elif not user_input.isdigit():
            print("Invalid input")
            
# Exercise – Print a Pattern
def print_pattern(w: int, s: str) -> None:
    for i in range(1, w * 2):
        print((s + ' ') * min(i, w * 2 - i))
            
# Exercise – Fibonacci Sequence
def fibonacci_to_50() -> list[int]:
    sequence = [0, 1]
    while (sequence[-2] + sequence[-1])  < 50:
        sequence.append(sequence[-2] + sequence[-1])
    return sequence
            
# Exercise – Print Hollow Pyramid
def print_pyramid(w: int) -> None:
    for i in range(1, w + 1):
        if i == 1:
            print(' ' * (w - i) + '*' + ' ' * (w - i))
        else:
            print(' ' * (w - i) + '*' + ' ' * (2 * i - 3) + '*' + ' ' * (w - i))

# Exercise – Guess a Number
def take_guess() -> None:
    num = random.randint(1, 10)
    count = 0
    while True:
        guess = int(input("Take a guess: "))
        count += 1
        if guess == num:
            print("Bingo! You found it! It took you " + str(count) + " guesses.")
            break
        elif guess < num:
            print("Your guess is smaller than the target.")
        elif guess > num:
            print("Your guess is greater than the target.")

