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

files = 'abcdefgh'
ranks = '12345678'

def safe_pawns(pawns: set) -> int:
    defenders = {}      # The dictionary consisting of all possible
                        # squares for every pawn, where a defending pawn can
                        # be placed.
    safe_pawns = set()  # The output set consisting of pawns having at least
                        # one defending pawn.

    for p in pawns:
        idx_file = files.index(p[0])
        idx_rank = ranks.index(p[1])
        # Each pawn can have two possible defenders
        # on its left-bottom diagonal and/or its right-bottom diagonal
        p_defenders = set()
        # The row (rank) == 0 is not protected, a pawn has not got defenders there (if it
        # only could be placed on this row).
        if idx_rank > 0 and idx_rank < 8:
            if idx_file > 0 and idx_file < 7:
                p_defenders.add(files[idx_file+1] + ranks[idx_rank-1])
                p_defenders.add(files[idx_file-1] + ranks[idx_rank-1])
            # pawn on the leftmost column
            elif idx_file == 0:
                p_defenders.add(files[idx_file+1] + ranks[idx_rank-1])
            # pawn on the rightmost column
            elif idx_file == 7:
                p_defenders.add(files[idx_file-1] + ranks[idx_rank-1])
            defenders[p] = p_defenders

    # For every pawn check if its defenders' squares are physically filled with another pawn.
    # If so, add the pawn to the output set.
    for k,v in defenders.items():
        for i in range(len(v)):
            if list(v)[i] in pawns:
                safe_pawns.add(k)

    return len(safe_pawns)


MONTHS = {1:'January', 2:'February', 3:'March', \
          4:'April', 5:'May', 6:'June', \
          7:'July', 8:'August', 9:'September', \
          10:'October', 11:'November', 12:'December' }

def date_time(time: str) -> str:
    pattern = r'^(?P<dd>\d{2}).(?P<mm>\d{2}).(?P<yyyy>\d{4}) (?P<hh>\d{2}):(?P<mi>\d{2})$'
    o = re.match(pattern, time)
    time = "%s %s %s year %s %s %s %s" % (int(o.group('dd')), \
		     MONTHS[int(o.group('mm'))], \
		     o.group('yyyy'), \
		     int(o.group('hh')), \
		     ('hours','hour')[o.group('hh')=='01'], \
		     int(o.group('mi')), \
		     ('minutes','minute')[o.group('mi')=='01'])
    return time
