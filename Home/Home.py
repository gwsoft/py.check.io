import datetime
import re


def even_last(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    sum = 0
    if len(array) > 0:
        for i in range(0, len(array)):
           if i % 2 == 0:
               sum = sum + array[i]
        sum = sum * array[len(array)-1]
    return sum
	
def even_last_slice(array: list) -> int:
	last = array[-1] if len(array) > 0 else 0
	return sum(array[::2])*last
	
def three_words(words: str) -> bool:
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

def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    res = ",".join(phrases).replace("right","left")
    return res

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # get rid of invalid chars
    vtext = text.replace('.',' ').replace(',',' ')
    return vtext.split()[0]

def days_diff(a, b):
    date1 = datetime.date(a[0],a[1],a[2])
    date2 = datetime.date(b[0],b[1],b[2])
    diff = date2-date1
    return abs(diff.days)


def count_digits_regex(text: str) -> int:
    # remove all non-digits with regex
    digits = re.sub(r'[^0-9]', '', text)
    return len(digits)

def count_digits_iter(text: str) -> int:
    return sum(c.isdigit() for c in text)

def backward_string_by_word(text: str) -> str:
    pattern = r'(\w+|\s+)'
    words = re.findall(pattern, text)
    rev_w = list(map(lambda w: w[::-1], words))
    return ''.join(rev_w)

def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    bigdict = {}
    for u in data:
        bigdict.update( { u['name']: u['price'] } )
    sort_items = sorted([(value,key) for (key,value) in bigdict.items()], reverse=True)
    out_list = []
    for i in range(limit):
        d = {}
        d.update({ "name": sort_items[i][1], "price": sort_items[i][0] })
        out_list.append( d )
    return out_list

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    ifrom = 0 if text.find(begin) < 0 else text.find(begin)+len(begin)
    ito = len(text) if text.find(end) < 0 else text.find(end)
    return text[ifrom:ito:]

def non_unique_elements(data: list) -> list:
    out = []
    for e in data:
        if data.count(e) > 1:
            out.append(e)
    return out

def popular_words(text: str, words: list) -> dict:
    out = {}
    items = text.lower().split()
    for w in words:
        out[w] = items.count(w)
    return out

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    o = [x.start() for x in re.finditer(symbol,text)]
    return o[1] if len(o)>1 else None
