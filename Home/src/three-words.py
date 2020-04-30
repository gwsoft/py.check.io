def checkio(words: str) -> bool:
	wordlist = words.split(' ')							# convert the input string to an array
	l_sum = 0											# counts consecutive occurences of words
	res = False											# return variable
	for x in wordlist:									# iterate the array
		l_weight = 0 if x.isnumeric() else 1			# check if the element is a word
		l_sum = l_sum + 1 if l_weight == 1 else 0		# .. if it is, then increase word occurences
		if l_sum == 3:									# .. break the loop if this is 3rd word in a row
			res = True
			break
	return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")