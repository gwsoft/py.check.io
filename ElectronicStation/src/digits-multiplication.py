"""
You are given a positive integer. Your function should calculate
the product of the digits excluding any zeroes.

For example: The number given is 123405.
The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.
"""

def digits_multiplication(number: int) -> int:
    # List Comprehension
    nonzero = [int(i) for i in list(str(number)) if int(i)>0]
    # Recursive Lambda
    mul = lambda pos: nonzero[0] if pos == 0 else nonzero[pos]*mul(pos-1)
    return mul(len(nonzero)-1)


if __name__ == '__main__':
    print('Example:')
    print(digits_multiplication(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digits_multiplication(123405) == 120
    assert digits_multiplication(999) == 729
    assert digits_multiplication(1000) == 1
    assert digits_multiplication(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
