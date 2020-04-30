"""
You need to count the number of digits in a given string.

Input: A Str.

Output: An Int.
"""

import re

def count_digits(text: str) -> int:
    # remove all non-digits with regex
    digits = re.sub(r'[^0-9]', '', text)
    return len(digits)

def count_digits_iter(text: str) -> int:
    digits = sum(c.isdigit() for c in text)
    return digits

if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))
    print(count_digits_iter('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0

    assert count_digits_iter('hi') == 0
    assert count_digits_iter('who is 1st here') == 1
    assert count_digits_iter('my numbers is 2') == 1
    assert count_digits_iter('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
    assert count_digits_iter('5 plus 6 is') == 2
    assert count_digits_iter('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
