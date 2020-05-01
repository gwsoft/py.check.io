from typing import Iterable
import math
import re
import string

def backward_string(val: str) -> str:
    result = ''
    for a in range(0, len(val), 1):
        result = result + val[-a-1]
    return result

def remove_all_before(items: list, border: int) -> Iterable:
	if border in items:
		res = items[items.index(border):]
	else:
		res = items
	return res

def is_all_upper(text: str) -> bool:
	allowed_letters = string.ascii_uppercase + ' ' + string.digits
	res = True
	for i in range(0, len(text)):
		if text[i] not in allowed_letters:
			res = False
			break
	return res

def replace_first(items: list) -> Iterable:
	# In a given list the first element should become the last one.
	""" Algorithm:
	Take the first element into a temporary variable
	use the del keyword to remove the specified index
	append the list with the temp variable.
	"""
	if len(items) > 1:
		tmp = items[0]
		del items[0]
		items.append(tmp)
	# An empty list or list with only one element should stay the same.
	return items

def max_digit(number: int) -> int:
    return int(max(list(str(number))))

def split_pairs(a):
    b = []
    for i in range(0,math.ceil((len(a)/2))):
        b.append(str(a[i*2:i*2+2]).ljust(2,'_'))
    return b

def beginning_zeros(number: str) -> int:
    zeros = re.search(r'^(0+)\d*$', number)
    return len(zeros.group(1)) if zeros else 0

def nearest_value(values: set, one: int) -> int:
    # Make sure the input set is sorted
    listval = sorted(values)
    # Quick break for values exceeding the last element of the array
    if one > listval[-1]:
        return listval[-1]
    else:
        for i in range(1, len(listval)):
            if one < listval[i]:
                result = listval[i] if abs(listval[i]-one)<abs(listval[i-1]-one) else listval[i-1]
                break
        return result

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    return text[text.find(begin)+1:text.find(end):]

def between_markers_regex(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    pattern = '.*'+re.escape(begin)+'(.*)'+re.escape(end)+'.*'
    res = re.match(pattern, text)
    return res.group(1) if res else ''

def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    out = ''
    if text[0].islower():
        out = text[0].upper() + text[1::]
    else:
        out = text

    if not text.endswith('.'):
        out = out + '.'
    
    return out


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))
