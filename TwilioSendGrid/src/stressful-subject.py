"""
The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are in uppercase,
and/or ends by at least 3 exclamation marks,
and/or contains at least one of the following “red” words:
"help", "asap", "urgent". Any of those "red" words can be spelled
in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP," they just can't have
any other letters interspersed between them.

Input: Subject line as a string.

Output: Boolean.

Precondition: Subject can be up to 100 letters
"""

import re

def is_stressful(subj):
    """
    recognize stressful subject
    """
    result = False

    # 1st case: all letters are in uppercase
    if subj == subj.upper():
        #print("Found! All uppercase")
        return True

    # 2nd case: ends by at least 3 exclamation marks
    if subj[-3:] == '!!!':
        #print("Found! Three exlamation marks")
        return True

    # 3rd case: contains at least one "red" word
    red_words_patterns = ('^h+e+l+p+$',
                          '^a+s+a+p+$',
                          '^u+r+g+e+n+t+$')
    subj_words = subj.split()
    for x in subj_words:
        x = x.lower()
        # remove unwanted chars from the word
        xrem = x.replace('-','').replace('!','').replace('.','')
        #print('checking the word: ' + xrem)
        # check if the word matches red words patterns
        for pattern in red_words_patterns:
            check = re.match(pattern, xrem)
            if check:
                #print('-> that word matches pattern '  + pattern)
                result = True
                break
    return result

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("We need you A.S.A.P.!!") == True, "Third"
    assert is_stressful("I NEED YOU NOW!") == True, "4th"
    assert is_stressful("What do I need to do???!!!!") == True, "5th"
    print('Done! Go Check it!')
