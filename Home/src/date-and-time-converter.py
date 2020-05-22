import re

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

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
