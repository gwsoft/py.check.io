"""
Sort the given iterable so that its elements end up in the decreasing
frequency order, that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same
order as the first appearance in the iterable.

Input: Iterable

Output: Iterable
"""

def frequency_sort(items):
    # remove duplicates from the items
    items2 = list(dict.fromkeys(items))

    # create list frequencies using list comprehension
    freq = [items.count(i) for i in items2]

    # create list of tuples (ti,tf), then sort the list according to tf
    # from highest to lowest value
    tuples = [ [items2[r], freq[r]] for r in range(0,len(items2)) ]
    tuples.sort(key=lambda t:t[1], reverse=True)

    # create output list
    res = []
    for ti,tf in tuples:
        res += [ti]*tf    
    return res


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
