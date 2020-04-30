import string

def is_all_upper(text: str) -> bool:
	allowed_letters = string.ascii_uppercase + ' ' + string.digits
	res = True
	for i in range(0, len(text)):
		if text[i] not in allowed_letters:
			res = False
			break
	return res


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
