# Devansh's Function
def question3(num1: int, num2: int) -> None:
    """
    Prints a pattern of num1 and difference of num1 and num2, decrementing num1 by 1 for each line, until it reaches 1.

    Precondition: num1 and num2 must be between 1 and 9 and num12 > num1

    >>> question3(1,3)
    1 22

    >>> question3(8,9)
    88888888 1
    7777777 22
    666666 333
    55555 4444
    4444 55555
    333 666666
    22 7777777
    1 88888888
    """
    # Condition to check the base case of the recursive function
    if num1 == 0:
        return None
    # Print one line of values
    print(str(num1) * num1 + ' ' + str(num2 - num1) * (num2 - num1))
    # Call the recursive function
    question3(num1 - 1, num2)

# Alvin's Function
def Q3(a, b):
    if (1 <= a < b <= 9):
        def countdown(c, d):
            print(str(c)*c, str(d)*d, sep=' ')
            if c == 1: 
                return
            else: 
                countdown(c - 1, d + 1)                
        countdown(a, b-a)        
    else:
        print('Please make sure the two arguments are between 1 and 9, and that the 2nd argument is greater than the 1st one.')